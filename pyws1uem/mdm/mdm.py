"""
Module to access the WorkspaceONE UEM /mdm API Endpoint

This module sets basic parameters that are needed to
correctly connect to /mdm API Endpoints
"""


from pyws1uem.client import Client
from pyws1uem.rest import Rest


class MDM(Rest):
    """
    Base MDM class

    Workspace ONE UEM REST APIs allows you
    to manage all the functionalities of Mobile Device Management (MDM).
    The functionalities that are included but not limited to are
    device commands, retrieval of compliance, profile, network, location,
    smartgroups, and event log details.
    """

    def __init__(self, client: Client):
        """
        Initialize the MDM class

        :param client: Client object
        """
        Rest.__init__(self, client=client, module='mdm')
