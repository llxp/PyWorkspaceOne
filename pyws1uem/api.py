from .system import Info, Users, Groups
from .mdm import Smartgroups, Tags, Devices, Profiles
from .mam import Apps
from .client import Client


class WorkspaceOneAPI(object):
    """
    Class for building a WorkspaceONE UEM API Object
    """

    def __init__(
        self,
        env: str,
        apikey: str,
        username: str,
        password: str,
        verify: str = None
    ):
        """
        Initialize an AirWatchAPI Client Object.

        :param  env: Base URL of the AirWatch API Service
                apikey: API Key to authorize
                username: Admin username
                password: corresponding pasword
                verify: manual SSL certificat
        """
        self.client = Client(env, apikey, username, password, verify=verify)
        self.groups = Groups(self.client)
        self.devices = Devices(self.client)
        self.smartgroups = Smartgroups(self.client)
        self.users = Users(self.client)
        self.info = Info(self.client)
        self.tags = Tags(self.client)
        self.apps = Apps(self.client)
        self.profiles = Profiles(self.client)
