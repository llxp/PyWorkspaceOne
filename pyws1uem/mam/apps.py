"""
Module to manage smartgroups (add and remove)
"""

from .mam import MAM
from ..client import Client


class Apps(MAM):
    """
    Base Apps Class

    Contains REST-API Calls to retrieve and manage apps
    """

    def __init__(self, client: Client):
        """
        Initialize Apps Class

        :param client: Client Object
        """
        MAM.__init__(self, client)

    def get_app(self, app_id: str):
        """
        Get a specific app
        """
        return self._get(path=f'/apps/internal/{app_id}')
