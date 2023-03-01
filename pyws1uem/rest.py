"""
Module to access the WorkspaceONE UEM /mdm API Endpoint

This module sets basic parameters that are needed to
correctly connect to /mdm API Endpoints
"""


from typing import Any, Dict
from pyws1uem.client import Client, _Params, RestResponseType
from httpx import Response


class Rest(object):
    """
    Base Rest class for all endpoints
    """

    def __init__(self, client: Client, module: str):
        self.client = client
        self._module = module

    def _get(
        self,
        path: str = "",
        version: str = "",
        params: _Params = {},
        header: Dict[str, str] = {}
    ) -> RestResponseType:
        """GET requests for base endpoints"""
        response = self.client.get(
            module=self._module,
            path=path,
            version=version,
            params=params,
            header=header
        )
        return response

    def _post(
        self,
        path: str = "",
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: Dict[str, str] = {}
    ) -> RestResponseType:
        """POST requests for base endpoints"""
        return self.client.post(
            module=self._module,
            path=path,
            version=version,
            params=params,
            data=data,
            json=json,
            header=header
        )

    def _post_no_error_check(
        self,
        module: str = 'system',
        path: str = "",
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: Dict[str, str] = {}
    ) -> Response:
        """
        POST requests with no error check when none json is returned
        """
        return self.client.post_no_error_check(
            module=module,
            path=path,
            version=version,
            params=params,
            data=data,
            json=json,
            header=header
        )

    def _put(
        self,
        path: str = "",
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: Dict[str, str] = {}
    ) -> RestResponseType:
        """PUT requests for base endpoints"""
        return self.client.put(
            module=self._module,
            path=path,
            version=version,
            params=params,
            data=data,
            json=json,
            header=header
        )

    def _patch(
        self,
        path: str = "",
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: Dict[str, str] = {}
    ) -> RestResponseType:
        """Patch requests for base endpoints"""
        return self.client.patch(
            module=self._module,
            path=path,
            version=version,
            params=params,
            data=data,
            json=json,
            header=header
        )

    def _delete(
        self,
        path: str = "",
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: Dict[str, str] = {}
    ) -> RestResponseType:
        """DELETE requests for base endpoints"""
        return self.client.delete(
            module=self._module,
            path=path,
            version=version,
            params=params,
            header=header
        )

    # ----------------------------------------------------------------
    # Async methods
    # ----------------------------------------------------------------

    async def _async_get(
        self,
        path: str = "",
        version: str = "",
        params: _Params = {},
        header: Dict[str, str] = {}
    ) -> RestResponseType:
        """GET requests for base endpoints"""
        return await self.client.async_get(
            module=self._module,
            path=path,
            version=version,
            params=params,
            header=header
        )

    async def _async_post(
        self,
        path: str = "",
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: Dict[str, str] = {}
    ) -> RestResponseType:
        """POST requests for base endpoints"""
        return await self.client.async_post(
            module=self._module,
            path=path,
            version=version,
            params=params,
            data=data,
            json=json,
            header=header
        )

    async def _async_post_no_error_check(
        self,
        module: str = 'system',
        path: str = "",
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: Dict[str, str] = {}
    ) -> Response:
        """
        POST requests with no error check when none json is returned
        """
        return await self.client.async_post_no_error_check(
            module=module,
            path=path,
            version=version,
            params=params,
            data=data,
            json=json,
            header=header
        )

    async def _async_put(
        self,
        path: str = "",
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: Dict[str, str] = {}
    ) -> RestResponseType:
        """PUT requests for base endpoints"""
        return await self.client.async_put(
            module=self._module,
            path=path,
            version=version,
            params=params,
            data=data,
            json=json,
            header=header
        )

    async def _async_patch(
        self,
        path: str = "",
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: Dict[str, str] = {}
    ) -> RestResponseType:
        """Patch requests for base endpoints"""
        return await self.client.async_patch(
            module=self._module,
            path=path,
            version=version,
            params=params,
            data=data,
            json=json,
            header=header
        )

    async def _async_delete(
        self,
        path: str = "",
        version: str = "",
        params: _Params = {},
        data: Any = None,
        json: Any = None,
        header: Dict[str, str] = {}
    ) -> RestResponseType:
        """DELETE requests for base endpoints"""
        return await self.client.async_delete(
            module=self._module,
            path=path,
            version=version,
            params=params,
            header=header
        )
