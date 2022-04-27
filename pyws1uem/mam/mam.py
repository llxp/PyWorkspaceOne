"""
Module to access the WorkspaceONE UEM /mam API Endpoint

This module sets basic parameters that are needed to
correctly connect to /mam API Endpoints
"""

from ..client import Client
from ..rest import Rest


class MAM(Rest):
    """
    Base MAM class

    Workspace ONE UEM REST APIs allows you to manage the end-to-end
    functionalities of Mobile Application Management (MAM) features.
    Using these APIs, you can upload internal and public applications,
    assign, and manage applications on the devices.
    """

    def __init__(self, client: Client):
        """
        Initialize the MAM class

        :param client: Client
        """
        Rest.__init__(self, client=client, module='mam')
