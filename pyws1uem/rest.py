"""
Module to access the WorkspaceONE UEM /mdm API Endpoint

This module sets basic parameters that are needed to
correctly connect to /mdm API Endpoints
"""


from typing import Any
from .client import Client


class Rest(object):
    """
    Base Rest class for all endpoints
    """

    def __init__(self, client: Client, module: str):
        self.client = client
        self._module = module

    def _get(
        self,
        path: str = None,
        version: str = None,
        params: dict = None,
        header: dict = None
    ):
        """GET requests for base endpoints"""
        return self.client.get(
            module=self._module,
            path=path,
            version=version,
            params=params,
            header=header
        )

    def _post(
        self,
        path: str = None,
        version: str = None,
        params: dict = None,
        data: Any = None,
        json: Any = None,
        header: dict = None
    ):
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
        path: str = None,
        version: str = None,
        params: dict = None,
        data: Any = None,
        json: Any = None,
        header: dict = None
    ):
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
        path=None,
        version=None,
        params=None,
        data=None,
        json=None,
        header=None
    ):
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
        path=None,
        version=None,
        params=None,
        data=None,
        json=None,
        header=None
    ):
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
        path=None,
        version=None,
        params=None,
        data=None,
        json=None,
        header=None
    ):
        """DELETE requests for base endpoints"""
        return self.client.delete(
            module=self._module,
            path=path,
            version=version,
            params=params,
            data=data,
            json=json,
            header=header
        )
