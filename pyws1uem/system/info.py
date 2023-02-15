"""
Module to get the general system information
of the accessed WorkspaceONE UEM environment
"""

from pyws1uem.client import Client
from pyws1uem.system.system import System


class Info(System):
    """
    Base Info Class, inherited from the System class
    """
    def __init__(self, client: Client):
        System.__init__(self, client)

    def get_environment_info(self):
        """
        Get information like system-version from the UEM environment

        Returns:
            dict: System Information in JSON-format
        """
        return System._get(self, path="/info")

    async def get_environment_info_async(self):
        """
        Get information like system-version from the UEM environment

        Returns:
            dict: System Information in JSON-format
        """
        return await System._async_get(self, path="/info")
