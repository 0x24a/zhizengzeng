from typing import Mapping
from httpx import URL, Request
from httpx._client import Client
from openai import *
from openai._base_client import DEFAULT_MAX_RETRIES
from openai._types import NOT_GIVEN, NotGiven, Timeout
from httpx import request
from typing import Union, Callable



class ZhiZengZeng(OpenAI):
    def __init__(
        self,
        *,
        api_key: str | None = None,
        organization: str | None = None,
        base_url: str | URL | None = "https://flag.smarttrot.com/v1",
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        super().__init__(
            api_key=api_key,
            organization=organization,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
            http_client=http_client,
            _strict_response_validation=_strict_response_validation,
        )
        if not self.connected:
            raise ConnectionError("Cannot connect to ZhiZengZeng API. Try checking your internet connection?")
        self.get_balance()
    @property
    def connected(self) -> bool:
        #send ping to server
        try:
            self._client.send(Request("GET", self.base_url.__str__()))
            return True
        except:
            return False

    def get_balance(self) -> float:
        balance = request("POST", self.base_url.__str__()+"/dashboard/billing/credit_grants", headers={"Content-Type":"application/json","Authorization": f"Bearer {self.api_key}"}).json().get("grants", {}).get("available_amount", None)
        if balance is None:
            raise APIError(body=balance,message="Cannot get balance from zhizengzeng API. You can get your API key from http://gpt.zhizengzeng.com/#/my", request=balance)
        return balance
    @property
    def balance(self) -> float:
        return self.get_balance()
    def _detect_api_key_vaild(self,function) -> Callable:
        def wrapper(*args, **kwargs):
            if self.get_balance() is None:
                raise AuthenticationError(response=None,body=None,message="ZhiZengZeng API key is not set/invalid. You can get your API key from http://gpt.zhizengzeng.com/#/my")
            return function(*args, **kwargs)
        return wrapper
    