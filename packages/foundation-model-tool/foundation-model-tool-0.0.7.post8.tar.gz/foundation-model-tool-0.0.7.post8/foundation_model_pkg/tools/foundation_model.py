import json
import re
import urllib.request

# import uuid
from abc import abstractmethod
from enum import Enum
from typing import Any, Dict, List, Mapping, Optional

# from urllib.request import HTTPError

from jinja2 import Template

from promptflow import ToolProvider, tool
from promptflow.connections import CustomConnection

# from promptflow.contracts.types import PromptTemplate
from promptflow.core.tools_manager import register_builtins

# from ..core.contracts import StoreStage
# from ..core.logging.utils import LoggingUtils
# from ..core.utils.retry_utils import retry_and_handle_exceptions
# from .contracts.telemetry import StoreToolEventCustomDimensions, StoreToolEventNames
# from .utils.logging import ToolLoggingUtils
# from .utils.pf_runtime_utils import PromptflowRuntimeUtils


class ModelFamily(str, Enum):
    LLAMA = "LLaMa"
    DOLLY = "Dolly"
    GPT2 = "GPT-2"
    FALCON = "Falcon"


class API(str, Enum):
    CHAT = "chat"
    COMPLETION = "completion"


class ContentFormatterBase:
    """Transform request and response of AzureML endpoint to match with
    required schema.
    """

    """
  Example:
      .. code-block:: python

          class ContentFormatter(ContentFormatterBase):
              content_type = "application/json"
              accepts = "application/json"

              def format_request_payload(
                  self,
                  prompt: str,
                  model_kwargs: Dict
              ) -> bytes:
                  input_str = json.dumps(
                      {
                          "inputs": {"input_string": [prompt]},
                          "parameters": model_kwargs,
                      }
                  )
                  return str.encode(input_str)

              def format_response_payload(self, output: str) -> str:
                  response_json = json.loads(output)
                  return response_json[0]["0"]
  """
    content_type: Optional[str] = "application/json"
    """The MIME type of the input data passed to the endpoint"""

    accepts: Optional[str] = "application/json"
    """The MIME type of the response data returned form the endpoint"""

    @staticmethod
    def escape_special_characters(prompt: str) -> str:
        """Escapes any special characters in `prompt`"""
        escape_map = {
            "\\": "\\\\",
            '"': '\\"',
            "\b": "\\b",
            "\f": "\\f",
            "\n": "\\n",
            "\r": "\\r",
            "\t": "\\t",
        }

        # Replace each occurrence of the specified characters with their escaped versions
        for escape_sequence, escaped_sequence in escape_map.items():
            prompt = prompt.replace(escape_sequence, escaped_sequence)

        return prompt

    @abstractmethod
    def format_request_payload(self, prompt: str, model_kwargs: Dict) -> bytes:
        """Formats the request body according to the input schema of
        the model. Returns bytes or seekable file like object in the
        format specified in the content_type request header.
        """

    @abstractmethod
    def format_response_payload(self, output: bytes) -> str:
        """Formats the response body according to the output
        schema of the model. Returns the data type that is
        received from the response.
        """


class OSSContentFormatter(ContentFormatterBase):
    """Content handler for LLMs from the OSS catalog."""

    def format_request_payload(self, prompt: str, model_kwargs: Dict) -> bytes:
        input_str = json.dumps(
            {
                "inputs": {"input_string": [ContentFormatterBase.escape_special_characters(prompt)]},
                "parameters": model_kwargs,
            }
        )
        return str.encode(input_str)

    def format_response_payload(self, output: bytes) -> str:
        response_json = json.loads(output)
        return response_json[0]["0"]


class HFContentFormatter(ContentFormatterBase):
    """Content handler for LLMs from the HuggingFace catalog."""

    def format_request_payload(self, prompt: str, model_kwargs: Dict) -> bytes:
        input_str = json.dumps(
            {
                "inputs": [ContentFormatterBase.escape_special_characters(prompt)],
                "parameters": model_kwargs,
            }
        )
        return str.encode(input_str)

    def format_response_payload(self, output: bytes) -> str:
        response_json = json.loads(output)
        return response_json[0]["generated_text"]


class DollyContentFormatter(ContentFormatterBase):
    """Content handler for the Dolly-v2-12b model"""

    def format_request_payload(self, prompt: str, model_kwargs: Dict) -> bytes:
        input_str = json.dumps(
            {
                "input_data": {"input_string": [ContentFormatterBase.escape_special_characters(prompt)]},
                "parameters": model_kwargs,
            }
        )
        return str.encode(input_str)

    def format_response_payload(self, output: bytes) -> str:
        response_json = json.loads(output)
        return response_json[0]


class LlamaContentFormatter(ContentFormatterBase):
    """Content formatter for LLaMa"""

    def __init__(self, api: API, chat_history: Optional[str] = ""):
        super().__init__()
        self.api = api
        self.chat_history = chat_history

    @staticmethod
    def validate_role(role: str) -> None:
        valid_roles = {"system", "user", "assistant"}
        if role not in valid_roles:
            valid_roles_str = ",".join([f"'{role}:\\n'" for role in valid_roles])
            error_message = f"""The Chat API requires a specific format for prompt definition, and the prompt should
            include separate lines as role delimiters: {valid_roles_str}. Current parsed role '{role}' does not
            meet the requirement. If you intend to use the Completion API, please select the appropriate API type
            and deployment name. If you do intend to use the Chat API, please refer to the guideline at
            https://aka.ms/pfdoc/chat-prompt or view the samples in our gallery that contain 'Chat' in the name."""
            raise Exception(error_message)

    @staticmethod
    def parse_chat(chat_str: str) -> List[Dict[str, str]]:
        # LLaMa only supports below roles.
        separator = r"(?i)\n*(system|user|assistant)\s*:\s*\n"
        chunks = re.split(separator, chat_str)
        chat_list = []
        for chunk in chunks:
            last_message = chat_list[-1] if len(chat_list) > 0 else None
            if last_message and "role" in last_message and "content" not in last_message:
                last_message["content"] = chunk
            else:
                if chunk.strip() == "":
                    continue
                role = chunk.strip().lower()
                # appends consecutive user messages together to support system hack
                if last_message and last_message.get("role", "") == "user" and role not in {"user", "assistant"}:
                    last_message["content"] += chunk
                    continue
                # Check if prompt follows chat api message format and has valid role.
                LlamaContentFormatter.validate_role(role)
                if last_message and last_message.get("role", "") == "user" and role == "user":
                    continue
                # system role not officially supported, so we hack a solution by making system role the user role
                new_message = {"role": role} if role != "system" else {"role": "user"}
                chat_list.append(new_message)

        return chat_list

    def format_request_payload(self, prompt: str, model_kwargs: Dict) -> bytes:
        """Formats the request according the the chosen api"""
        request_payload = (
            Template('{"input_data": {"input_string":{{history}},"parameters": {{model_kwargs}}}}').render(
                history=json.dumps(LlamaContentFormatter.parse_chat(self.chat_history)),
                model_kwargs=json.dumps(model_kwargs),
            )
            if self.api == API.CHAT
            else Template('{"input_data": {"input_string": ["{{prompt}}"], "parameters": {{model_kwargs}}}}').render(
                prompt=ContentFormatterBase.escape_special_characters(prompt),
                model_kwargs=json.dumps(model_kwargs),
            )
        )
        print(request_payload)
        return str.encode(request_payload)

    def format_response_payload(self, output: bytes) -> str:
        """Formats response"""
        print(json.loads(output))
        return json.loads(output)["output"] if self.api == API.CHAT else json.loads(output)[0]["0"]


class ContentFormatterFactory:
    """Factory class for supported models"""

    def get_content_formatter(
        model_family: ModelFamily, api: API, chat_history: Optional[List[Dict]] = []
    ) -> ContentFormatterBase:
        if model_family == ModelFamily.LLAMA:
            return LlamaContentFormatter(chat_history=chat_history, api=api)
        elif model_family == ModelFamily.DOLLY:
            return DollyContentFormatter()
        elif model_family == ModelFamily.GPT2:
            return OSSContentFormatter()
        elif model_family == ModelFamily.FALCON:
            return HFContentFormatter()


class AzureMLOnlineEndpoint:
    """Azure ML Online Endpoint models.

    Example:
        .. code-block:: python

            azure_llm = AzureMLModel(
                endpoint_url="https://<your-endpoint>.<your_region>.inference.ml.azure.com/score",
                endpoint_api_key="my-api-key",
                content_formatter=content_formatter,
            )
    """  # noqa: E501

    endpoint_url: str = ""
    """URL of pre-existing Endpoint. Should be passed to constructor or specified as
        env var `AZUREML_ENDPOINT_URL`."""

    endpoint_api_key: str = ""
    """Authentication Key for Endpoint. Should be passed to constructor or specified as
        env var `AZUREML_ENDPOINT_API_KEY`."""

    content_formatter: Any = None
    """The content formatter that provides an input and output
    transform function to handle formats between the LLM and
    the endpoint"""

    model_kwargs: Optional[Dict] = None
    """Key word arguments to pass to the model."""

    def __init__(
        self,
        endpoint_url: str,
        endpoint_api_key: str,
        content_formatter: ContentFormatterBase,
        model_kwargs: Optional[Dict] = None,
    ):
        self.endpoint_url = endpoint_url
        self.endpoint_api_key = endpoint_api_key
        self.content_formatter = content_formatter
        self.model_kwargs = model_kwargs

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        _model_kwargs = self.model_kwargs or {}
        return {
            **{"model_kwargs": _model_kwargs},
        }

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "azureml_endpoint"

    def _call_endpoint(self, body: bytes) -> bytes:
        """call."""

        headers = {
            "Content-Type": "application/json",
            "Authorization": ("Bearer " + self.endpoint_api_key),
        }

        req = urllib.request.Request(self.endpoint_url, body, headers)
        response = urllib.request.urlopen(req, timeout=50)
        result = response.read()
        return result

    def __call__(
        self,
        prompt: str,
        stop: Optional[List[str]] = json.dumps({}),
        **kwargs: Any,
    ) -> str:
        """Call out to an AzureML Managed Online endpoint.
        Args:
            prompt: The prompt to pass into the model.
            stop: Optional list of stop words to use when generating.
        Returns:
            The string generated by the model.
        Example:
            .. code-block:: python
                response = azureml_model("Tell me a joke.")
        """
        _model_kwargs = self.model_kwargs or {}

        body = self.content_formatter.format_request_payload(prompt, _model_kwargs)
        endpoint_response = self._call_endpoint(body)
        response = self.content_formatter.format_response_payload(endpoint_response)
        return response


class FoundationModel(ToolProvider):
    REQUIRED_KEYS = ["endpoint_url", "endpoint_api_key", "model_family"]

    def __init__(self, connection: CustomConnection):
        super().__init__()

        for key in self.REQUIRED_KEYS:
            accepted_keys = ",".join([key for key in self.REQUIRED_KEYS])
            if key not in connection:
                raise KeyError(
                    f"""Required key `{key}` not found in given custom connection.
                      Required keys are: {accepted_keys}."""
                )
        try:
            self.model_family = ModelFamily[connection.model_family]
        except KeyError:
            accepted_models = ",".join([model.name for model in ModelFamily])
            raise KeyError(
                f"""Given model_family '{connection.model_family}' not recognized.
                  Supported models are: {accepted_models}."""
            )
        self.connection = connection

        # logging_config = ToolLoggingUtils.generate_config(tool_name=self.__class__.__name__)
        # self.__logger = LoggingUtils.sdk_logger(__package__, logging_config)
        # self.__logger.update_telemetry_context({StoreToolEventCustomDimensions.TOOL_INSTANCE_ID: str(uuid.uuid4())})

        # self.__logger.telemetry_event_started(
        #     event_name=StoreToolEventNames.INIT,
        #     store_stage=StoreStage.INITIALIZATION,
        # )
        # self.__logger.telemetry_event_completed(event_name=StoreToolEventNames.INIT)
        # self.__logger.flush()

    # @retry_and_handle_exceptions(HTTPError)
    @tool
    def foundation_model(
        self,
        prompt: str,
        api: API,
        model_kwargs: Optional[Dict] = {},
        **kwargs,
    ) -> str:
        prompt = Template(prompt, trim_blocks=True, keep_trailing_newline=True).render(**kwargs)

        content_formatter = ContentFormatterFactory.get_content_formatter(
            model_family=self.model_family,
            api=api,
            chat_history=prompt,
        )

        llm = AzureMLOnlineEndpoint(
            endpoint_url=self.connection.endpoint_url,
            endpoint_api_key=self.connection.endpoint_api_key,
            content_formatter=content_formatter,
            model_kwargs=model_kwargs,
        )

        # pf_context = PromptflowRuntimeUtils.get_pf_context_info_for_telemtry()

        # @LoggingUtils.log_event(
        #     package_name=__package__,
        #     event_name=StoreToolEventNames.FOUNDATION_MODEL,
        #     scope_context=pf_context,
        #     store_stage=StoreStage.SEARVING,
        #     logger=self.__logger,
        #     flush=True,
        # )
        def _do_llm(llm: AzureMLOnlineEndpoint, prompt: str) -> str:
            return llm(prompt)

        return _do_llm(llm, prompt)


register_builtins(FoundationModel)
