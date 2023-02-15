"""
Module to manage device tags (add and remove)
"""

from pyws1uem.client import Client, RestResponseType
from pyws1uem.mdm.mdm import MDM


class Tags(MDM):
    """
    Base Tags Class

    Contains REST-API Calls to add Devices to specific tags
    to trigger dependent actions, such as
    installing profiles, apps or trigger compliance actions.
    """

    def __init__(self, client: Client):
        MDM.__init__(self, client)

    def add_device_tag(self, tag_id: int, device_id: str) -> RestResponseType:  # noqa: E501
        """Add a tag to a given device

        :param str tag_id: The ID of the Tag in WorkspaceOneUEM
        :param str device_id: The ID of the Device in WorkspaceOneUEM
        :return: Status of the executed command (Accepted/Failed) as json
        :rtype: Union[dict, int]
        """
        path = f'/tags/{str(tag_id)}/adddevices'
        device_to_add = {
            "BulkValues": {
                "Value": [
                    device_id
                ]
            }
        }
        return self._post(path=path, json=device_to_add)

    async def add_device_tag_async(self, tag_id: int, device_id: str) -> RestResponseType:  # noqa: E501
        """Add a tag to a given device

        :param str tag_id: The ID of the Tag in WorkspaceOneUEM
        :param str device_id: The ID of the Device in WorkspaceOneUEM
        :return: Status of the executed command (Accepted/Failed) as json
        :rtype: Union[dict, int]
        """
        path = f'/tags/{str(tag_id)}/adddevices'
        device_to_add = {
            "BulkValues": {
                "Value": [
                    device_id
                ]
            }
        }
        return await self._async_post(path=path, json=device_to_add)

    def remove_device_tag(self, tag_id: int, device_id: str) -> RestResponseType:  # noqa: E501
        """Remove a tag from a given device

        :param str tag_id: The ID of the Tag in WorkspaceOneUEM
        :param str device_id: The ID of the Device in WorkspaceOneUEM
        :return: Status of the executed command (Accepted/Failed) as json
        :rtype: Union[dict, int]
        """
        path = f'/tags/{tag_id}/removedevices'
        device_to_add = {
            "BulkValues": {
                "Value": [
                    device_id
                ]
            }
        }
        return self._post(path=path, json=device_to_add)

    async def remove_device_tag_async(self, tag_id: int, device_id: str) -> RestResponseType:  # noqa: E501
        """Remove a tag from a given device

        :param str tag_id: The ID of the Tag in WorkspaceOneUEM
        :param str device_id: The ID of the Device in WorkspaceOneUEM
        :return: Status of the executed command (Accepted/Failed) as json
        :rtype: Union[dict, int]
        """
        path = f'/tags/{tag_id}/removedevices'
        device_to_add = {
            "BulkValues": {
                "Value": [
                    device_id
                ]
            }
        }
        return await self._async_post(path=path, json=device_to_add)

    def check_device_tag(
        self,
        tag_id: int,
        device_id: str = "",
        device_uuid: str = ""
    ) -> bool:
        """
        Get a list of devices for the given tags
        and check if a specific device, defined by it's UUID,
        has the tag already assigned

        :param str tag_id: The ID of the Tag in WorkspaceOneUEM
        :param str device_id (optional):
            The DeviceID of the Device in WorkspaceOneUEM.
            Defaults to None.
        :param str device_uuid (optional):
            The UUID of the Device in WorkspaceOneUEM.
            Defaults to None.
        :return: True if the tag is assigned / False if not
        :rtype: bool
        """
        path = f'tags/{tag_id}/devices'
        response = self._get(path=path)
        if (
            response and
            isinstance(response, dict) and
            'Device' in response and
            isinstance(response['Device'], list)
        ):
            for device in response['Device']:
                if (
                    isinstance(device, dict) and
                    (
                        str(device['DeviceId']) == str(device_id)
                        or str(device['DeviceUuid']) == str(device_uuid)
                    )
                ):
                    return True
        return False

    async def check_device_tag_async(
        self,
        tag_id: int,
        device_id: str = "",
        device_uuid: str = ""
    ) -> bool:
        """
        Get a list of devices for the given tags
        and check if a specific device, defined by it's UUID,
        has the tag already assigned

        :param str tag_id: The ID of the Tag in WorkspaceOneUEM
        :param str device_id (optional):
            The DeviceID of the Device in WorkspaceOneUEM.
            Defaults to None.
        :param str device_uuid (optional):
            The UUID of the Device in WorkspaceOneUEM.
            Defaults to None.
        :return: True if the tag is assigned / False if not
        :rtype: bool
        """
        path = f'tags/{tag_id}/devices'
        response = await self._async_get(path=path)
        if (
            response and
            isinstance(response, dict) and
            'Device' in response and
            isinstance(response['Device'], list)
        ):
            for device in response['Device']:
                if (
                    isinstance(device, dict) and
                    (
                        str(device['DeviceId']) == str(device_id)
                        or str(device['DeviceUuid']) == str(device_uuid)
                    )
                ):
                    return True
        return False
