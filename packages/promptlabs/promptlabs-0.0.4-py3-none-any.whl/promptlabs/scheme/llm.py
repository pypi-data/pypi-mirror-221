import warnings
import os
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union, Mapping
from abc import ABC, abstractmethod

from pydantic import BaseModel, Extra, Field, root_validator, validator

def get_from_dict_or_env(
    data: Dict[str, Any], key: str, env_key: str, default: Optional[str] = None
) -> str:
    """Get a value from a dictionary or an environment variable."""
    if key in data and data[key]:
        return data[key]
    else:
        return get_from_env(key, env_key, default=default)
    
def get_from_env(key: str, env_key: str, default: Optional[str] = None) -> str:
    """Get a value from a dictionary or an environment variable."""
    if env_key in os.environ and os.environ[env_key]:
        return os.environ[env_key]
    elif default is not None:
        return default
    else:
        raise ValueError(
            f"Did not find {key}, please add an environment variable"
            f" `{env_key}` which contains it, or pass"
            f"  `{key}` as a named parameter."
        )


class BaseLLM(BaseModel, ABC):
    @abstractmethod
    def generate(
        self,
        messages: List[Dict[str, Any]],
    ) -> Tuple[bool, Dict[str,Any]]:
        pass

class ChatOpenAI(BaseLLM):
    client: Any  #: :meta private:
    model_name: str = Field(default="gpt-3.5-turbo", alias="model")
    """Model name to use."""
    temperature: float = 0.7
    """What sampling temperature to use."""
    openai_api_key: Optional[str] = None
    max_tokens: Optional[int] = None
    """Maximum number of tokens to generate."""
    
    
    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and python package exists in environment."""
        values["openai_api_key"] = get_from_dict_or_env(
            values, "openai_api_key", "OPENAI_API_KEY"
        )
        try:
            import openai

        except ImportError:
            raise ValueError(
                "Could not import openai python package. "
                "Please install it with `pip install openai`."
            )
        try:
            values["client"] = openai.ChatCompletion
        except AttributeError:
            raise ValueError(
                "`openai` has no `ChatCompletion` attribute, this is likely "
                "due to an old version of the openai package. Try upgrading it "
                "with `pip install --upgrade openai`."
            )
            
        return values
    
    def generate(
        self,
        messages: List[Dict[str, Any]],
    ) -> Tuple[bool, Dict[str,Any]]:
        openai_params = self._client_params
        try:
            response = self.client.create(messages=messages, **openai_params)
        except Exception as e:
            return (False, {"error_log" : str(e)})
        try:
            if response['choices'][0]['finish_reason'] == 'stop':
                return (True, {"response" : response})
        except Exception as e:
            return (False, {"error_log" : str(e), "response" : response})
    
    @property
    def _client_params(self) -> Mapping[str, Any]:
        """Get the parameters used for the openai client."""
        openai_creds: Dict[str, Any] = {
            "api_key": self.openai_api_key,
            "model": self.model_name,
        }
        return {**openai_creds, **self._default_params}
    
    @property
    def _default_params(self) -> Dict[str, Any]:
        """Get the default parameters for calling OpenAI API."""
        return {
            "model": self.model_name,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }