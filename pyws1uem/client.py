"""WorkspaceOneAPI Client Module

The module handles all basic methods to interact with the API.
Basic HTTP Method calls are defined here (GET, POST, PUT, PATCH, DELETE)
and static methods for error checking, building the client object
and constructing header values.

In Case of errors in the response the requests will raise an exception
using the WorkspaceOneAPIError Class.
"""

from __future__ import print_function, absolute_import
from base64 import b64encode
from typing import Any, Dict, List, Union
from http.client import HTTPConnection
from httpx import AsyncClient, Client as SyncClient, Response
from httpx._types import VerifyTypes, TimeoutTypes
from httpx._client import UseClientDefault, USE_CLIENT_DEFAULT
from httpx._config import DEFAULT_TIMEOUT_CONFIG

from pyws1uem.error import WorkspaceOneAPIError

# Enabling debugging at http.client level (requests->urllib3->http.client)
# you will see the REQUEST, including HEADERS and DATA, and RESPONSE with
# HEADERS but without DATA.
# the only thing missing will be the response.body which is not logged.
HTTPConnection.debuglevel = 0

_Params = Union[Dict[str, Any], str, bytes]
SerializableType = Union[
    str, int, float, bool,
    List["SerializableType"],
    Dict[str, "SerializableType"]
]
RestResponseType = Union[SerializableType, int]

# TODO: programing using library should be able to set logging level
# TODO: Implement logging to using config
# https://docs.python.org/3/howto/logging.html#configuring-logging
# TODO: sett logging correctly for a library
# https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True


class Client(object):
    """
    Class for building a WorkspaceONE UEM API Object
    """

    def __init__(
        self,
        env: str,
        apikey: str,
        username: str,
        password: str,
        verify: VerifyTypes = "",
        timeout: TimeoutTypes = DEFAULT_TIMEOUT_CONFIG
    ):
        """
        Initialize an AirWatchAPI Client Object.

        :param  env: Base URL of the AirWatch API Service
                apikey: API Key to authorize
                username: Admin username
                password: corresponding pasword
                verify: manual SSL certificate
        """
        self.env = env
        self.apikey = apikey
        self.username = username
        self.password = password
        self.verify = verify
        self.timeout = timeout

    def get(
        self,
        module: str,
        path: str,
        version: str = "",
        params: _Params = {},
        header: dict = {},
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> RestResponseType:
        """
        Sends a GET request to the API. Returns the response object.
        """
        header_tmp: Dict[str, str] = self._build_header(self.username, self.password, self.apikey, header)  # noqa: E501
        header_tmp.update({"Content-Type": "application/json"})
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            with SyncClient(verify=self.verify, timeout=self.timeout) as client:  # noqa: E501
                api_response = client.get(
                    endpoint,
                    params=params,
                    headers=header_tmp,
                    timeout=timeout,
                )
                response = self._check_for_error(api_response)
                return response
        except WorkspaceOneAPIError as api_error:
            raise api_error

    def post(
        self,
        module: str,
        path: str,
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: dict = {},
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> RestResponseType:
        """
        Sends a POST request to the API. Returns the response object.
        """
        header_tmp = self._build_header(self.username, self.password, self.apikey, header)  # noqa: E501
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            with SyncClient(verify=self.verify, timeout=self.timeout) as client:  # noqa: E501
                api_response = client.post(
                    endpoint,
                    params=params,
                    data=data,
                    json=json,
                    headers=header_tmp,
                    timeout=timeout,
                )
            return self._check_for_error(api_response)
        except WorkspaceOneAPIError as api_error:
            raise api_error

    def post_no_error_check(
        self,
        module: str,
        path: str,
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: dict = {},
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        """
        Sends a POST request to the API.
        Returns the response object without error checking.
        """
        header_tmp = self._build_header(self.username, self.password, self.apikey, header)  # noqa: E501
        endpoint = self._build_endpoint(self.env, module, path, version)
        with SyncClient(verify=self.verify, timeout=self.timeout) as client:  # noqa: E501
            return client.post(
                endpoint,
                params=params,
                data=data,
                json=json,
                headers=header_tmp,
                timeout=timeout,
            )

    def put(
        self,
        module: str,
        path: str,
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: Dict[str, str] = {},
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> RestResponseType:
        """
        Sends a PUT request to the API. Returns the response object.
        """
        header_tmp = self._build_header(self.username, self.password, self.apikey, header)  # noqa: E501
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            with SyncClient(verify=self.verify, timeout=self.timeout) as client:  # noqa: E501
                api_response = client.put(
                    endpoint,
                    params=params,
                    data=data,
                    json=json,
                    headers=header_tmp,
                    timeout=timeout,
                )
                return self._check_for_error(api_response)
        except WorkspaceOneAPIError as api_error:
            raise api_error

    def patch(
        self,
        module: str,
        path: str,
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: dict = {},
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> RestResponseType:
        """
        Sends a Patch request to the API. Returns the response object.
        """
        header_tmp = self._build_header(self.username, self.password, self.apikey, header)  # noqa: E501
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            with SyncClient(verify=self.verify, timeout=self.timeout) as client:  # noqa: E501
                api_response = client.patch(
                    endpoint,
                    params=params,
                    data=data,
                    json=json,
                    headers=header_tmp,
                    timeout=timeout,
                )
                api_response = self._check_for_error(api_response)
                return api_response
        except WorkspaceOneAPIError as api_error:
            raise api_error

    def delete(
        self,
        module: str,
        path: str,
        version: str = "",
        params: _Params = {},
        header: Dict[str, str] = {},
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> RestResponseType:
        """
        Sends a DELETE request to the API. Returns the response object.
        """
        header_tmp = self._build_header(self.username, self.password, self.apikey, header)  # noqa: E501
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            with SyncClient(verify=self.verify, timeout=self.timeout) as client:  # noqa: E501
                api_response = client.delete(
                    endpoint,
                    params=params,
                    headers=header_tmp,
                    timeout=timeout,
                )
                api_response = self._check_for_error(api_response)
                return api_response
        except WorkspaceOneAPIError as api_error:
            raise api_error

    @staticmethod
    def _check_for_error(response: Response) -> RestResponseType:
        """
        Checks the response for json data, then for an error, then for
        a status code
        """
        if response.headers.get("Content-Type") in (
            "application/json",
            "application/json; charset=utf-8",
        ):
            json = response.json()
            if isinstance(json, dict):
                if json.get("errorCode"):
                    raise WorkspaceOneAPIError(json_response=json)
                else:
                    return json
            else:
                return json
        else:
            return response.status_code

    @staticmethod
    def _build_endpoint(base_url, module, path: str = "", version: str = ""):
        """
        Builds the full url endpoint for the API request
        """
        if not base_url.startswith("https://"):
            base_url = "https://" + base_url
        if base_url.endswith("/"):
            base_url = base_url[:-1]
        if version:
            url = f"{base_url}/api/v{version}/{module}"
        else:
            url = f"{base_url}/api/{module}"
        if path:
            if path.startswith("/"):
                return f"{url}{path}"
            else:
                return f"{url}/{path}"
        return url

    @staticmethod
    def _build_header(username: str, password: str, token: str, header: Dict[str, str] = {}) -> Dict[str, str]:  # noqa: E501
        """
        Build the header with base64 login, AW API token,
        and accept a json response
        """
        header_tmp: Dict[str, str] = {}
        if header:
            header_tmp = header
        username_password = f"{username}:{password}"
        username_password_bytes = username_password.encode("ascii")
        hashed_auth = b64encode(username_password_bytes).decode("utf-8")
        header_tmp.update({"Authorization": f"Basic {hashed_auth}"})
        header_tmp.update({"aw-tenant-code": token})
        if not header_tmp.get("Accept"):
            header_tmp.update({"Accept": "application/json"})
        return header_tmp

    # ----------------------------------------------------------------
    # Async methods
    # ----------------------------------------------------------------

    async def async_get(
        self,
        module: str,
        path: str,
        version: str = "",
        params: _Params = {},
        header: dict = {},
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> RestResponseType:
        """
        Sends a GET request to the API. Returns the response object.
        """
        header_tmp: Dict[str, str] = self._build_header(self.username, self.password, self.apikey, header)  # noqa: E501
        header_tmp.update({"Content-Type": "application/json"})
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            async with AsyncClient(verify=self.verify, timeout=self.timeout) as client:  # noqa: E501
                api_response = await client.get(
                    endpoint,
                    params=params,
                    headers=header_tmp,
                    timeout=timeout,
                )
                return self._check_for_error(api_response)
        except WorkspaceOneAPIError as api_error:
            raise api_error

    async def async_post(
        self,
        module: str,
        path: str,
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: dict = {},
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> RestResponseType:
        """
        Sends a POST request to the API. Returns the response object.
        """
        header_tmp = self._build_header(self.username, self.password, self.apikey, header)  # noqa: E501
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            async with AsyncClient(verify=self.verify, timeout=self.timeout) as client:  # noqa: E501
                api_response = await client.post(
                    endpoint,
                    params=params,
                    data=data,
                    json=json,
                    headers=header_tmp,
                    timeout=timeout,
                )
            return self._check_for_error(api_response)
        except WorkspaceOneAPIError as api_error:
            raise api_error

    async def async_post_no_error_check(
        self,
        module: str,
        path: str,
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: dict = {},
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        """
        Sends a POST request to the API.
        Returns the response object without error checking.
        """
        header_tmp = self._build_header(self.username, self.password, self.apikey, header)  # noqa: E501
        endpoint = self._build_endpoint(self.env, module, path, version)
        async with AsyncClient(verify=self.verify, timeout=self.timeout) as client:  # noqa: E501
            return await client.post(
                endpoint,
                params=params,
                data=data,
                json=json,
                headers=header_tmp,
                timeout=timeout,
            )

    async def async_put(
        self,
        module: str,
        path: str,
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: Dict[str, str] = {},
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> RestResponseType:
        """
        Sends a PUT request to the API. Returns the response object.
        """
        header_tmp = self._build_header(self.username, self.password, self.apikey, header)  # noqa: E501
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            async with AsyncClient(verify=self.verify, timeout=self.timeout) as client:  # noqa: E501
                api_response = await client.put(
                    endpoint,
                    params=params,
                    data=data,
                    json=json,
                    headers=header_tmp,
                    timeout=timeout,
                )
                return self._check_for_error(api_response)
        except WorkspaceOneAPIError as api_error:
            raise api_error

    async def async_patch(
        self,
        module: str,
        path: str,
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: dict = {},
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> RestResponseType:
        """
        Sends a Patch request to the API. Returns the response object.
        """
        header_tmp = self._build_header(self.username, self.password, self.apikey, header)  # noqa: E501
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            async with AsyncClient(verify=self.verify, timeout=self.timeout) as client:  # noqa: E501
                api_response = await client.patch(
                    endpoint,
                    params=params,
                    data=data,
                    json=json,
                    headers=header_tmp,
                    timeout=timeout,
                )
                return self._check_for_error(api_response)
        except WorkspaceOneAPIError as api_error:
            raise api_error

    async def async_delete(
        self,
        module: str,
        path: str,
        version: str = "",
        params: _Params = {},
        header: Dict[str, str] = {},
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> RestResponseType:
        """
        Sends a DELETE request to the API. Returns the response object.
        """
        header_tmp = self._build_header(self.username, self.password, self.apikey, header)  # noqa: E501
        endpoint = self._build_endpoint(self.env, module, path, version)
        try:
            async with AsyncClient(verify=self.verify, timeout=self.timeout) as client:  # noqa: E501
                api_response = await client.delete(
                    endpoint,
                    params=params,
                    headers=header_tmp,
                    timeout=timeout,
                )
                return self._check_for_error(api_response)
        except WorkspaceOneAPIError as api_error:
            raise api_error
