"""
Module to access the WorkspaceONE UEM /system API Endpoint

This module sets basic parameters that are needed to
correctly connect to /system API Endpoints
"""

from pyws1uem.rest import Rest
from pyws1uem.client import Client


class System(Rest):
    """
    Base System class

    Workspace ONE UEM REST APIs allows you to manage
    all the core functionalities around console administration where you can:
    - Create and assign administrator accounts
      so admins can easily manage users and devices.
    - Create, manage, and view device enrollment user's.
        Identify users and establish permissions using organization groups.
    - Group sets of users into user groups which act as filters
      (in addition to organization groups)
      for assigning profiles and applications.
    - Extract particular values from the devices
      and return it to Workspace ONE UEM.
      These attributes can then be associated with other rules
      to further assign to the devices.
    """
    def __init__(self, client: Client):
        Rest.__init__(self, client=client, module='system')
