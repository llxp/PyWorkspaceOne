"""
Module to access the WorkspaceONE UEM /mem API Endpoint

This module sets basic parameters that are needed to
correctly connect to /mem API Endpoints
"""

from ..client import Client
from ..rest import Rest


class MEM(Rest):
    """
    Base MEM class

    Workspace ONE UEM REST APIs enables you to manage emails on devices.
    Through these APIs, you can retreive email management device details
    and apply compliance policies to devices.
    """

    def __init__(self, client: Client):
        """
        Initialize the MEM class

        :param client: Client object
        """
        Rest.__init__(self, client=client, module='mem')


# TODO: Implement
