"""
Module to manage all core functionalities
for WorkspaceONE UEM Organization Groups
"""

import json
from typing import Any, Union
from pyws1uem.system.system import System
from pyws1uem.client import Client


class Groups(System):
    """
    Sub-Class to manage Groups, inherited from the base System class
    """
    jheader = {'Content-Type': 'application/json'}

    def __init__(self, client: Client):
        System.__init__(self, client)

    def search(self, **kwargs):
        """
        Returns the Groups matching the search parameters
        """
        return self._get(path='/groups/search', params=kwargs)

    async def search_async(self, **kwargs):
        """
        Returns the Groups matching the search parameters
        """
        return await self._async_get(path='/groups/search', params=kwargs)

    def get_id_from_groupid(self, groupid: str) -> Union[str, None]:
        """
        Returns the OG ID for a given Group ID

        :param str groupid: The Group ID of the OG
        :return: The OG ID
        :rtype: str
        """
        response = self.search(groupid=str(groupid))
        if (
            isinstance(response, dict) and
            'LocationGroups' in response and
            isinstance(response['LocationGroups'], list) and
            len(response['LocationGroups']) != 0
        ):
            locationGroups = response['LocationGroups']
            if (
                isinstance(locationGroups[0], dict) and
                'Id' in locationGroups[0] and
                isinstance(locationGroups[0]['Id'], dict) and
                'Value' in locationGroups[0]['Id'] and
                isinstance(locationGroups[0]['Id']['Value'], str)
            ):
                return locationGroups[0]['Id']['Value']
        return None

    async def get_id_from_groupid_async(self, groupid: str) -> Union[str, None]:  # noqa: E501
        """
        Returns the OG ID for a given Group ID

        :param str groupid: The Group ID of the OG
        :return: The OG ID
        :rtype: str
        """
        response = await self.search_async(groupid=str(groupid))
        if (
            isinstance(response, dict) and
            'LocationGroups' in response and
            isinstance(response['LocationGroups'], list) and
            len(response['LocationGroups']) != 0
        ):
            locationGroups = response['LocationGroups']
            if (
                isinstance(locationGroups[0], dict) and
                'Id' in locationGroups[0] and
                isinstance(locationGroups[0]['Id'], dict) and
                'Value' in locationGroups[0]['Id'] and
                isinstance(locationGroups[0]['Id']['Value'], str)
            ):
                return locationGroups[0]['Id']['Value']
        return None

    def get_groupid_from_id(self, groupid: str) -> Union[str, None]:
        """
        Returns the Group ID for a given ID
        """
        response = self._get(path=f'/groups/{groupid}')
        if (
            isinstance(response, dict) and
            'GroupId' in response and
            isinstance(response['GroupId'], str)
        ):
            return response['GroupId']
        return None

    async def get_groupid_from_id_async(self, groupid: str) -> Union[str, None]:  # noqa: E501
        """
        Returns the Group ID for a given ID
        """
        response = await self._async_get(path=f'/groups/{groupid}')
        if (
            isinstance(response, dict) and
            'GroupId' in response and
            isinstance(response['GroupId'], str)
        ):
            return response['GroupId']
        return None

    def get_uuid_from_groupid(self, groupid: str) -> Union[str, None]:
        """
        Returns the OG UUID for a given Group ID
        """
        response = self._get(path=f'/groups/{groupid}')
        if (
            isinstance(response, dict) and
            'Uuid' in response and
            isinstance(response['Uuid'], str) and
            len(response['Uuid']) != 0
        ):
            return response['Uuid']
        return None

    async def get_uuid_from_groupid_async(self, groupid: str) -> Union[str, None]:  # noqa: E501
        """
        Returns the OG UUID for a given Group ID
        """
        response = await self._async_get(path=f'/groups/{groupid}')
        if (
            isinstance(response, dict) and
            'Uuid' in response and
            isinstance(response['Uuid'], str) and
            len(response['Uuid']) != 0
        ):
            return response['Uuid']
        return None

    def create(self, parent_id: str, ogdata: Any):
        """
        Creates a Group and returns the new ID
        """
        return self._post(path=f'/groups/{parent_id}', data=ogdata, header=self.jheader)  # noqa: E501

    async def create_async(self, parent_id: str, ogdata: Any):
        """
        Creates a Group and returns the new ID
        """
        return await self._async_post(path=f'/groups/{parent_id}', data=ogdata, header=self.jheader)  # noqa: E501

    def create_customer_og(self, groupid: Union[str, None], name: Union[str, None] = None) -> Union[str, None]:  # noqa: E501
        """
        Creates a Customer type OG, with a given Group ID and Name,
        and returns the new ID
        """
        new_og = {
            'GroupId': str(groupid),
            'Name': str(name),
            'LocationGroupType': 'Customer'
        }
        if name is None:
            new_og['Name'] = str(groupid)
        response = self.create(parent_id="7", ogdata=json.dumps(new_og))
        if (
            isinstance(response, dict) and
            'Value' in response and
            isinstance(response['Value'], str)
        ):
            return response['Value']
        return None

    async def create_customer_og_async(self, groupid: Union[str, None], name: Union[str, None] = None) -> Union[str, None]:  # noqa: E501
        """
        Creates a Customer type OG, with a given Group ID and Name,
        and returns the new ID
        """
        new_og = {
            'GroupId': str(groupid),
            'Name': str(name),
            'LocationGroupType': 'Customer'
        }
        if name is None:
            new_og['Name'] = str(groupid)
        response = await self.create_async(parent_id="7", ogdata=json.dumps(new_og))  # noqa: E501
        if (
            isinstance(response, dict) and
            'Value' in response and
            isinstance(response['Value'], str)
        ):
            return response['Value']

    def create_child_og(
        self,
        parent_groupid: str,
        groupid: str,
        og_type: Union[str, None] = None,
        name: Union[str, None] = None
    ) -> Union[str, None]:
        """
        Creates a Child OG for a given Parent Group ID, with a given Type,
        Group ID, and Name, and returns the new ID
        """
        pid = self.get_id_from_groupid(parent_groupid)
        if pid is None:
            return None
        new_og = {
            'GroupId': str(groupid),
            'Name': str(name),
            'LocationGroupType': str(og_type)
        }
        if name is None:
            new_og['Name'] = str(groupid)
        if og_type is None:
            new_og['LocationGroupType'] = 'Container'
        response = self.create(parent_id=pid, ogdata=json.dumps(new_og))
        if (
            isinstance(response, dict) and
            'Value' in response and
            isinstance(response['Value'], str)
        ):
            return response['Value']
        return None

    async def create_child_og_async(
        self,
        parent_groupid: str,
        groupid: str,
        og_type: Union[str, None] = None,
        name: Union[str, None] = None
    ) -> Union[str, None]:
        """
        Creates a Child OG for a given Parent Group ID, with a given Type,
        Group ID, and Name, and returns the new ID
        """
        pid = await self.get_id_from_groupid_async(parent_groupid)
        if pid is None:
            return None
        new_og = {
            'GroupId': str(groupid),
            'Name': str(name),
            'LocationGroupType': str(og_type)
        }
        if name is None:
            new_og['Name'] = str(groupid)
        if og_type is None:
            new_og['LocationGroupType'] = 'Container'
        response = await self.create_async(parent_id=pid, ogdata=json.dumps(new_og))  # noqa: E501
        if (
            isinstance(response, dict) and
            'Value' in response and
            isinstance(response['Value'], str)
        ):
            return response['Value']
        return None
