"""
Module to manage devices in the WorkspaceONE /mdm context.
"""

from typing import Dict, Union
from pyws1uem.client import RestResponseType
from pyws1uem.mdm.mdm import MDM


class Devices(MDM):
    """
    A class to manage devices of the Mobile Device Management (MDM) context
    of the WorkspaceONE UEM API.
    """

    def __init__(self, client):
        MDM.__init__(self, client)

    def search(self, **kwargs) -> RestResponseType:
        """
        Returns the Device information matching the search parameters.
        """
        return self._get(path='/devices', params=kwargs)

    async def search_async(self, **kwargs) -> RestResponseType:
        """
        Returns the Device information matching the search parameters.
        -> Async version
        """
        return await self._async_get(path='/devices', params=kwargs)

    def searchv2(self, **kwargs) -> RestResponseType:
        """
        Returns the Device information matching the search parameters
        with v2 endpoint.
        """
        _header = {'Accept': 'application/json;version=2'}
        return self._get(path='/devices/search', header=_header, params=kwargs)  # noqa: E501

    async def searchv2_async(self, **kwargs) -> RestResponseType:
        """
        Returns the Device information matching the search parameters
        with v2 endpoint.
        -> Async version
        """
        _header = {'Accept': 'application/json;version=2'}
        return await self._async_get(path='/devices/search', header=_header, params=kwargs)  # noqa: E501

    def searchv3(self, **kwargs) -> RestResponseType:
        """
        Returns the Device information matching the search parameters
        with v3 endpoint.
        """
        _header = {'Accept': 'application/json;version=3'}
        return self._get(path='/devices/search', header=_header, params=kwargs)  # noqa: E501

    async def searchv3_async(self, **kwargs) -> RestResponseType:
        """
        Returns the Device information matching the search parameters
        with v3 endpoint.
        -> Async version
        """
        _header = {'Accept': 'application/json;version=3'}
        return await self._async_get(path='/devices/search', header=_header, params=kwargs)  # noqa: E501

    def search_all(self, **kwargs) -> RestResponseType:
        """
        Returns the Devices matching the search parameters.
        """
        response = self._get(path='/devices/search', params=kwargs)
        return response

    async def search_all_async(self, **kwargs) -> RestResponseType:
        """
        Returns the Devices matching the search parameters.
        -> Async version
        """
        response = await self._async_get(path='/devices/search', params=kwargs)
        return response

    def extensive_search(self, **kwargs) -> RestResponseType:
        """
        Full device details search with many attributes included.

        :param int organizationgroupid (optional):
                OrganizationGroup to be searched,
                user's OG is considered if not sent.
                Defaults to None.
        :param str platform (optional): Device platform. Defaults to None.
        :param str startdatetime (optional):
                Filters devices such that devices with
                last seen after this date will be returned.
                Defaults to None.
        :param str enddatetime (optional):
                Filters devices such that devices with
                last seen till this date will be returned.
                Defaults to None.
        :param int deviceid (optional): Device Identifier. Defaults to None.
        :param str customattributeslist (optional):
                Custom attribute names.
                Defaults to None.
        :param str enrollmentstatus (optional):
                Filters devices based on EnrollmentStatus
                [
                    Enrolled,
                    EnterpriseWipePending,
                    DeviceWipePending,
                    Unenrolled
                ].
                Defaults to None.
        :param str statuschangestarttime (optional):
                Filters the devices for which EnrollmentStatus has changes
                from enrollmentstatuschangefrom datetime.
                This filter is only for
                Enrolled and Unenrolled enrollment status.
                Defaults to None.
        :param str statuschangeendtime (optional):
                Filters the devices for which EnrollmentStatus has changes
                till enrollmentstatuschangeto datetime.
                This filter is only for
                Enrolled and Unenrolled enrollment status.
                Defaults to None.
        :param int page (optional):
                Specific page number to get. 0 based index.
                Defaults to 0.
        :param int pagesize (optional):
                Maximumm records per page.
                Defaults to 500.
        :param str macaddress (optional): MAC address. Defaults to None.

        :return: API paged of devices that meet the search requirements.
        :rtype: Union[dict, int, None]
        """
        return self._get(path='/devices/extensivesearch', params=kwargs)  # noqa: E501

    async def extensive_search_async(self, **kwargs) -> RestResponseType:
        """
        The same as extensive_search but async.
        """
        return await self._async_get(path='/devices/extensivesearch', params=kwargs)  # noqa: E501

    def get_details_by_alt_id(
        self,
        serialnumber: str = "",
        macaddress: str = "",
        udid: str = "",
        imeinumber: str = "",
        easid: str = ""
    ) -> Union[RestResponseType, None]:
        """
        Returns the Device information matching the search parameters.

        :param serialnumber: Serial number of the device.
        :param macaddress: MAC address of the device.
        :param udid: UDID of the device.
        :param imeinumber: IMEI number of the device.
        :param easid: EAS ID of the device.
        :return: Device information.
        :rtype: Union[dict, int, None]
        """
        if serialnumber:
            response = self.search(searchby='Serialnumber', id=str(serialnumber))  # noqa: E501
        elif macaddress:
            response = self.search(searchby='Macaddress', id=str(macaddress))
        elif udid:
            response = self.search(searchby='Udid', id=str(udid))
        elif imeinumber:
            response = self.search(searchby='ImeiNumber', id=str(imeinumber))
        elif easid:
            response = self.search(searchby='EasId', id=str(easid))
        else:
            return None
        return response

    async def get_details_by_alt_id_async(
        self,
        serialnumber: str = "",
        macaddress: str = "",
        udid: str = "",
        imeinumber: str = "",
        easid: str = ""
    ) -> Union[RestResponseType, None]:
        """
        The same as get_details_by_alt_id but async.
        """
        if serialnumber:
            response = await self.search_async(searchby='Serialnumber', id=str(serialnumber))  # noqa: E501
        elif macaddress:
            response = await self.search_async(searchby='Macaddress', id=str(macaddress))  # noqa: E501
        elif udid:
            response = await self.search_async(searchby='Udid', id=str(udid))
        elif imeinumber:
            response = await self.search_async(searchby='ImeiNumber', id=str(imeinumber))  # noqa: E501
        elif easid:
            response = await self.search_async(searchby='EasId', id=str(easid))
        else:
            return None
        return response

    def get_id_by_alt_id(
        self,
        serialnumber: str = "",
        macaddress: str = "",
        udid: str = "",
        imeinumber: str = "",
        easid: str = ""
    ) -> Union[int, None]:
        """
        Get the DeviceID
        by specifying another ID of the Device in WorkspaceOneUEM

        :param str serialnumber (optional):
                Serialnumber of the Device.
                Defaults to an empty string.
        :param str macaddress (optional):
                Primary MAC-Address of the Device.
                Defaults to an empty string.
        :param str udid (optional):
                DeviceUdid generated by WorkspaceOneUEM.
                Defaults to an empty string.
        :param str imeinumber (optional):
                IMEI Number of the Device (mobile).
                Defaults to an empty string.
        :param easid (optional):
                EasID of the Device (mobile).
                Defaults to an empty string.

        :return: DeviceID as an integer value
        :rtype: int
        """
        response = self.get_details_by_alt_id(serialnumber, macaddress, udid, imeinumber, easid)  # noqa: E501
        if (
            response and
            isinstance(response, dict) and
            'Id' in response and
            isinstance(response['Id'], dict) and
            'Value' in response['Id'] and
            isinstance(response['Id']['Value'], int)
        ):
            return response['Id']['Value']
        return None

    async def get_id_by_alt_id_async(
        self,
        serialnumber: str = "",
        macaddress: str = "",
        udid: str = "",
        imeinumber: str = "",
        easid: str = ""
    ) -> Union[int, None]:
        """
        The same as get_id_by_alt_id but async.
        """
        response = await self.get_details_by_alt_id_async(serialnumber, macaddress, udid, imeinumber, easid)  # noqa: E501
        if (
            response and
            isinstance(response, dict) and
            'Id' in response and
            isinstance(response['Id'], dict) and
            'Value' in response['Id'] and
            isinstance(response['Id']['Value'], int)
        ):
            return response['Id']['Value']
        return None

    def clear_device_passcode(self, device_id: str) -> RestResponseType:  # noqa: E501
        """
        Clear the passcode on a device

        :param str device_id: The device ID
        :return: JSON API response as a dict
        :rtype: dict
        """
        return self._post(path=f'/devices/{device_id}/clearpasscode')  # noqa: E501

    async def clear_device_passcode_async(self, device_id: str) -> RestResponseType:  # noqa: E501
        """
        The same as clear_device_passcode but async.
        """
        return await self._async_post(path=f'/devices/{device_id}/clearpasscode')  # noqa: E501

    def send_commands_for_device_id(self, command: str, device_id: str) -> RestResponseType:  # noqa: E501
        """
        Commands for devices selecting device based on id

        :param str command: The command to send
        :param str device_id: The device ID
        :return: JSON API response as a dict
        :rtype: dict
        """
        path = f'/devices/{device_id}/commands'
        command = f'command={command}'
        return self._post(path=path, params=command)

    async def send_commands_for_device_id_async(self, command: str, device_id: str) -> RestResponseType:  # noqa: E501
        """
        The same as send_commands_for_device_id but async.
        """
        path = f'/devices/{device_id}/commands'
        command = f'command={command}'
        return await self._async_post(path=path, params=command)

    def send_commands_by_id(self, command: str, searchby: str, device_id: str) -> RestResponseType:  # noqa: E501
        """
        Commands for devices selecting device based on id

        :param str command: The command to send
        :param str searchby: The searchby parameter
        :param str device_id: The device ID
        :return: JSON API response as a dict
        :rtype: dict
        """
        _path = '/devices/commands'
        _query = f'command={command}&searchBy={searchby}&id={device_id}'
        return self._post(path=_path, params=_query)

    async def send_commands_by_id_async(self, command: str, searchby: str, device_id: str) -> RestResponseType:  # noqa: E501
        """
        The same as send_commands_by_id but async.
        """
        _path = '/devices/commands'
        _query = f'command={command}&searchBy={searchby}&id={device_id}'
        return await self._async_post(path=_path, params=_query)

    def get_details_by_device_id(self, device_id: int) -> RestResponseType:  # noqa: E501
        """
        device details by device id

        :param str device_id: The device ID
        :return: JSON API response as a dict
        :rtype: dict
        """
        return self._get(path=f'/devices/{device_id}')

    async def get_details_by_device_id_async(self, device_id: int) -> RestResponseType:  # noqa: E501
        """
        The same as get_details_by_device_id but async.
        """
        return await self._async_get(path=f'/devices/{device_id}')

    def get_device_filevault_recovery_key(self, device_uuid: str) -> RestResponseType:  # noqa: E501
        """
        Gets a macOS device's FileVault Recovery Key

        :param str device_uuid: The device UUID
        :return: JSON API response as a dict
        :rtype: dict
        """
        _path = f'/devices/{device_uuid}/security/recovery-key'
        return self._get(path=_path)

    async def get_device_filevault_recovery_key_async(self, device_uuid: str) -> RestResponseType:  # noqa: E501
        """
        The same as get_device_filevault_recovery_key but async.
        """
        _path = f'/devices/{device_uuid}/security/recovery-key'
        return await self._async_get(path=_path)

    def get_security_info_by_id(self, device_id: str) -> RestResponseType:  # noqa: E501
        """
        Processes the device ID to retrieve the security
        information sample related info

        :param str device_id: The device ID
        :return: JSON API response as a dict
        :rtype: dict
        """
        _path = f'/devices/{device_id}/security'
        return self._get(path=_path)

    async def get_security_info_by_id_async(self, device_id: str) -> RestResponseType:  # noqa: E501
        """
        The same as get_security_info_by_id but async.
        """
        _path = f'/devices/{device_id}/security'
        return await self._async_get(path=_path)

    def get_security_info_by_alternate_id(self, searchby: str, alternate_id: str) -> RestResponseType:  # noqa: E501
        """
        Processes the device ID to retrieve the security
        information sample related info by Alternate ID

        :param str searchby: The searchby parameter
        :param str alternate_id: The alternate ID
        :return: JSON API response as a dict
        :rtype: dict
        """
        _path = '/devices/security'
        _params = f'searchby={searchby}&id={alternate_id}'
        return self._get(path=_path, params=_params)

    async def get_security_info_by_alternate_id_async(self, searchby: str, alternate_id: str) -> RestResponseType:  # noqa: E501
        """
        The same as get_security_info_by_alternate_id but async.
        """
        _path = '/devices/security'
        _params = f'searchby={searchby}&id={alternate_id}'
        return await self._async_get(path=_path, params=_params)

    def get_bulk_security_info(self, organization_group_id: str, user_name: str) -> RestResponseType:  # noqa: E501
        """
        Processes the information like organization group ID, user name, model,
        platform, last seen, ownership, compliant status, seen since parameters
        and fetches the security information for the same.

        :param str organization_group_id: The organization group ID
        :param str user_name: The user name
        :return: JSON API response as a dict
        :rtype: dict
        """
        _path = '/devices/securityinfosearch'
        _query = f'organizationgroupid={organization_group_id}&user={user_name}'  # noqa: E501
        return self._get(path=_path, params=_query)

    async def get_bulk_security_info_async(self, organization_group_id: str, user_name: str) -> RestResponseType:  # noqa: E501
        """
        The same as get_bulk_security_info but async.
        """
        _path = '/devices/securityinfosearch'
        _query = f'organizationgroupid={organization_group_id}&user={user_name}'  # noqa: E501
        return await self._async_get(path=_path, params=_query)

    def switch_device_from_staging_to_user(self, device_id: str, user_id: str) -> RestResponseType:  # noqa: E501
        """
        API for Single Staging switch to directory or basic user

        :param str device_id: The device ID
        :param str user_id: The user ID
        :return: JSON API response as a dict
        :rtype: dict
        """
        _path = f"/devices/{device_id}/enrollmentuser/{user_id}"
        return self._patch(path=_path)

    async def switch_device_from_staging_to_user_async(self, device_id: str, user_id: str) -> RestResponseType:  # noqa: E501
        """
        The same as switch_device_from_staging_to_user but async.
        """
        _path = f"/devices/{device_id}/enrollmentuser/{user_id}"
        return await self._async_patch(path=_path)

    def get_managed_admin_account_by_uuid(self, device_id: str) -> RestResponseType:  # noqa: E501
        """
        Get information of the administrator account configured on a macOS
        device via device enrollment program (DEP).

        :param str device_id: The device ID
        :return: JSON API response as a dict
        :rtype: dict
        """
        _path = f"/devices/{device_id}/security/managed-admin-information"
        return self._get(path=_path)

    async def get_managed_admin_account_by_uuid_async(self, device_id: str) -> RestResponseType:  # noqa: E501
        """
        The same as get_managed_admin_account_by_uuid but async.
        """
        _path = f"/devices/{device_id}/security/managed-admin-information"
        return await self._async_get(path=_path)

    def delete_device_by_id(self, device_id: str) -> RestResponseType:
        """
        Delete a device from management.

        :param str device_id: The device ID
        :return: API response
        :rtype: dict
        """
        return self._delete(path=f'/devices/{device_id}')

    async def delete_device_by_id_async(self, device_id: str) -> RestResponseType:  # noqa: E501
        """
        The same as delete_device_by_id but async.
        """
        return await self._async_delete(path=f'/devices/{device_id}')

    def delete_customattribute_by_id(self, device_id: str, custom_attributes: str) -> RestResponseType:  # noqa: E501
        """
        Delete a device customattribute.

        :param str device_id: The device ID
        :param str customAttributes:
            The attributes to remove separated by a comma
        :return: JSON API response as a dict
        :rtype: dict
        """
        _path = f"/devices/{device_id}/customattributes"
        _data = {"CustomAttributes": []}
        for item in custom_attributes.split(","):
            _data["CustomAttributes"].append({"Name": item})
        return self._delete(path=_path, json=_data)

    async def delete_customattribute_by_id_async(self, device_id: str, custom_attributes: str) -> RestResponseType:  # noqa: E501
        """
        The same as delete_customattribute_by_id but async.
        """
        _path = f"/devices/{device_id}/customattributes"
        _data = {"CustomAttributes": []}
        for item in custom_attributes.split(","):
            _data["CustomAttributes"].append({"Name": item})
        return await self._async_delete(path=_path, json=_data)

    def delete_customattribute_by_alt_id(self, serialnumber: str, custom_attributes: str) -> RestResponseType:  # noqa: E501
        """
        Delete a device customattribute by it's serial number.

        # NOTE: (clayton) This function doesn't seem to work from testing?

        :param str serialnumber: The device serial number
        :param str customAttributes:
            The attributes to remove separated by a comma
        :return: API response as a dict
        :rtype: dict
        """
        _path = f"/devices/serialnumber/{serialnumber}/customattributes"
        _data = {"CustomAttributes": []}
        for item in custom_attributes.split(","):
            _data["CustomAttributes"].append({"Name": item})
        return self._delete(path=_path, json=_data)

    async def delete_customattribute_by_alt_id_async(self, serialnumber: str, custom_attributes: str) -> RestResponseType:  # noqa: E501
        """
        The same as delete_customattribute_by_alt_id but async.
        """
        _path = f"/devices/serialnumber/{serialnumber}/customattributes"
        _data = {"CustomAttributes": []}
        for item in custom_attributes.split(","):
            _data["CustomAttributes"].append({"Name": item})
        return await self._async_delete(path=_path, json=_data)

    def search_enrollment_token(self, organization_group_uuid: str, **kwargs) -> RestResponseType:  # noqa: E501
        """
        Returns a list of enrollment tokes that match the search criteria.

        :param str organization_group_uuid: The Uuid of the Organization Group
        :param str kwargs: Search criteria
        :return: API response as a dict
        :rtype: dict
        """
        _path = f"/groups/{organization_group_uuid}/enrollment-tokens"
        return self._get(path=_path, params=kwargs)

    async def search_enrollment_token_async(self, organization_group_uuid: str, **kwargs) -> RestResponseType:  # noqa: E501
        """
        The same as search_enrollment_token but async.
        """
        _path = f"/groups/{organization_group_uuid}/enrollment-tokens"
        return await self._async_get(path=_path, params=kwargs)

    def create_enrollment_token(self, organization_group_uuid: str, registration_record: Dict[str, str]) -> RestResponseType:  # noqa: E501
        """
        Creates a device enrollment token in the given organization unit
        with a given registration record (data)

        :param str organization_group_uuid: The Uuid of the Organization Group
        :param str registration_record: The registration record
        :return: API response as a dict
        :rtype: dict
        """
        _path = f"/groups/{organization_group_uuid}/enrollment-tokens"
        return self._post(path=_path, json=registration_record)

    async def create_enrollment_token_async(self, organization_group_uuid: str, registration_record: Dict[str, str]) -> RestResponseType:  # noqa: E501
        """
        The same as create_enrollment_token but async.
        """
        _path = f"/groups/{organization_group_uuid}/enrollment-tokens"
        return await self._async_post(path=_path, json=registration_record)

    def delete_enrollment_token(self, organization_group_uuid: str, token_uuid: str) -> RestResponseType:  # noqa: E501
        """
        Deletes a device enrollment token from the given organization unit

        :param str organization_group_uuid: The Uuid of the Organization Group
        :param str token_uuid: The Uuid of the token
        """
        _path = f"/groups/{organization_group_uuid}/enrollment-tokens/{token_uuid}"  # noqa: E501
        return self._delete(path=_path)

    async def delete_enrollment_token_async(self, organization_group_uuid: str, token_uuid: str) -> RestResponseType:  # noqa: E501
        """
        The same as delete_enrollment_token but async.
        """
        _path = f"/groups/{organization_group_uuid}/enrollment-tokens/{token_uuid}"  # noqa: E501
        return await self._async_delete(path=_path)

    def get_device_smartgroups(self, device_id: str) -> RestResponseType:
        """
        Get the smart groups for a device

        :param str device_id: The device ID
        :return: JSON API response as a dict
        :rtype: dict
        """
        _path = f"/devices/{device_id}/smartgroups"
        return self._get(path=_path)

    async def get_device_smartgroups_async(self, device_id: str) -> RestResponseType:  # noqa: E501
        """
        The same as get_device_smartgroups but async.
        """
        _path = f"/devices/{device_id}/smartgroups"
        return await self._async_get(path=_path)

    def get_devices_apps(self, device_id):
        """
        Get the apps for a device

        :param str device_id: The device ID
        :return: JSON API response as a dict
        :rtype: dict
        """
        _path = f"/devices/{device_id}/apps"
        return self._get(path=_path)

    async def get_devices_apps_async(self, device_id):
        """
        The same as get_devices_apps but async.
        """
        _path = f"/devices/{device_id}/apps"
        return await self._async_get(path=_path)

    def get_devices_profiles(self, device_id):
        """
        Get the profiles for a device

        :param str device_id: The device ID
        :return: JSON API response as a dict
        :rtype: dict
        """
        _path = f"/devices/{device_id}/profiles"
        return self._get(path=_path)

    async def get_devices_profiles_async(self, device_id):
        """
        The same as get_devices_profiles but async.
        """
        _path = f"/devices/{device_id}/profiles"
        return await self._async_get(path=_path)
