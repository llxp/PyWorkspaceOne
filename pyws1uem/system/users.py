"""
Module to manage core functionalities related to Users in WorkspaceONE UEM
"""

from pyws1uem.system.system import System
from pyws1uem.client import Client, RestResponseType


class Users(System):
    """
    Class to manage user related methods/functions,
    inherited from the base system class
    """

    def __init__(self, client: Client):
        System.__init__(self, client)

    def search(self, **kwargs):
        """
        Returns the Enrollment User's details matching the search parameters

        /api/system/users/search?{params}

        PARAMS:
            username={username}
            firstname={firstname}
            lastname={lastname}
            email={email}
            organizationgroupid={locationgroupid}
            role={role}
        """
        return self._get(path='/users/search', params=kwargs)

    async def search_async(self, **kwargs):
        """
        Returns the Enrollment User's details matching the search parameters

        /api/system/users/search?{params}

        PARAMS:
            username={username}
            firstname={firstname}
            lastname={lastname}
            email={email}
            organizationgroupid={locationgroupid}
            role={role}
        """
        return await self._async_get(path='/users/search', params=kwargs)

    def get_user_by_uuid(self, uuid):
        """
        Returns the enrollment user for a specific uuid using the v2 endpoint.

        PARAMS:
            uuid (str): AirWatch UUID to return
        """
        _path = f"/users/{uuid}"
        _header = {'Accept': 'application/json;version=2'}
        return self._get(header=_header, path=_path)

    async def get_user_by_uuid_async(self, uuid):
        """
        Returns the enrollment user for a specific uuid using the v2 endpoint.

        PARAMS:
            uuid (str): AirWatch UUID to return
        """
        _path = f"/users/{uuid}"
        _header = {'Accept': 'application/json;version=2'}
        return await self._async_get(header=_header, path=_path)

    def create_user(self, **kwargs):
        """
        Create an enrollment user using the v2 endpoint.

        /api/system/users/

        PARAMS:
            externalId={e559e7df-4ba0-4891-9fcd-8574c1770d34}
            userName={username}
            password={password}
            firstName={firstname}
            lastName={lastname}
            displayName={displayname}
            userPrincipalName={testuser@gandalf.dev}
            emailAddress={noreply@vmware.com}
            emailUsername={noreply@vmware.come}
            phoneNumber={1-111-111-1111}
            mobileNumber={+1(111)-111-1111}
            messageType={Email}
            messageTemplateUuid={53f732a0-3e08-474d-80f4-ff976b8eb698}
            enrollmentRoleUuid={599b9117-f399-4e60-a96b-cd1f771d5f06}
            status=true,
            securityType={directory}     REQUIRED
            deviceStagingEnabled=false,
            deviceStagingType={StagingDisabled}
            organizationGroupUuid={6fbc95c6-3269-4a88-804d-c8db7f479d7f}
            enrollmentOrganizationGroupUuid={94b1b965-59b9-462c-ad18-4a228f9830dd}
            customAttribute1={CustomAttribute1}
            customAttribute2={CustomAttribute2}
            customAttribute3={CustomAttribute3}
            customAttribute4={CustomAttribute4}
            customAttribute5={CustomAttribute5}
            aadMappingAttribute={e559e7df-4ba0-4891-9fcd-8574c1770d34}
            department={Sales}
            employeeIdentifier={12345}
            costCenter={110)
        """
        _header = {'Accept': 'application/json;version=2'}
        return self._post(header=_header, path="/users/", json=kwargs)

    async def create_user_async(self, **kwargs):
        """
        Create an enrollment user using the v2 endpoint.

        /api/system/users/

        PARAMS:
            externalId={e559e7df-4ba0-4891-9fcd-8574c1770d34}
            userName={username}
            password={password}
            firstName={firstname}
            lastName={lastname}
            displayName={displayname}
            userPrincipalName={testuser@gandalf.dev}
            emailAddress={noreply@vmware.com}
            emailUsername={noreply@vmware.come}
            phoneNumber={1-111-111-1111}
            mobileNumber={+1(111)-111-1111}
            messageType={Email}
            messageTemplateUuid={53f732a0-3e08-474d-80f4-ff976b8eb698}
            enrollmentRoleUuid={599b9117-f399-4e60-a96b-cd1f771d5f06}
            status=true,
            securityType={directory}     REQUIRED
            deviceStagingEnabled=false,
            deviceStagingType={StagingDisabled}
            organizationGroupUuid={6fbc95c6-3269-4a88-804d-c8db7f479d7f}
            enrollmentOrganizationGroupUuid={94b1b965-59b9-462c-ad18-4a228f9830dd}
            customAttribute1={CustomAttribute1}
            customAttribute2={CustomAttribute2}
            customAttribute3={CustomAttribute3}
            customAttribute4={CustomAttribute4}
            customAttribute5={CustomAttribute5}
            aadMappingAttribute={e559e7df-4ba0-4891-9fcd-8574c1770d34}
            department={Sales}
            employeeIdentifier={12345}
            costCenter={110)
        """
        _header = {'Accept': 'application/json;version=2'}
        return await self._async_post(header=_header, path="/users/", json=kwargs)  # noqa: E501

    def update_user_by_uuid(self, uuid: str = "", **kwargs):
        """
        Update the enrollment user with attributes using the v2 endpoint.

        /api/system/users/{uuid}

        PARAMS:
            password={Password1}
            firstName={Firstname}
            lastName={Lastname}
            displayName={displayName}
            userPrincipalName={testuser@gandalf.dev}
            emailAddress={noreply@vmware.com}
            emailUsername={noreply@vmware.com}
            phoneNumber={5551234567}
            mobileNumber={5551234567}
            messageType={Email}
            messageTemplateUuid={2aca918b-3468-4539-8750-41a7074b120d}
            deviceStagingEnabled": false,
            deviceStagingType={StagingDisabled}
            enrollmentRoleUuid={0aa0256e-89c6-450e-854c-aa97233b61b6}
            enrollmentOrganizationGroupUuid={db1d3802-6885-4035-99ab-e39239b5a0f2}
            CustomAttribute1={CustomAttribute1}
            CustomAttribute2={CustomAttribute2}
            CustomAttribute3={CustomAttribute3}
            CustomAttribute4={CustomAttribute4}
            CustomAttribute5={CustomAttribute5}
        """
        _path = f"/users/{uuid}"
        _header = {'Accept': 'application/json;version=2'}
        return self._put(path=_path, header=_header, json=kwargs)

    async def update_user_by_uuid_async(self, uuid: str = "", **kwargs):
        """
        Update the enrollment user with attributes using the v2 endpoint.

        /api/system/users/{uuid}

        PARAMS:
            password={Password1}
            firstName={Firstname}
            lastName={Lastname}
            displayName={displayName}
            userPrincipalName={testuser@gandalf.dev}
            emailAddress={noreply@vmware.com}
            emailUsername={noreply@vmware.com}
            phoneNumber={5551234567}
            mobileNumber={5551234567}
            messageType={Email}
            messageTemplateUuid={2aca918b-3468-4539-8750-41a7074b120d}
            deviceStagingEnabled": false,
            deviceStagingType={StagingDisabled}
            enrollmentRoleUuid={0aa0256e-89c6-450e-854c-aa97233b61b6}
            enrollmentOrganizationGroupUuid={db1d3802-6885-4035-99ab-e39239b5a0f2}
            CustomAttribute1={CustomAttribute1}
            CustomAttribute2={CustomAttribute2}
            CustomAttribute3={CustomAttribute3}
            CustomAttribute4={CustomAttribute4}
            CustomAttribute5={CustomAttribute5}
        """
        _path = f"/users/{uuid}"
        _header = {'Accept': 'application/json;version=2'}
        return await self._async_put(path=_path, header=_header, json=kwargs)

    def delete_user_by_uuid(self, uuid: str):
        """
        Delete the enrollment user by enrollment user uuid
        with the v2 endpoint.

        :param uuid: enrollment user uuid
        :return: API response as a dict
        :rtype: dict
        """
        _path = f'/users/{uuid}'
        _header = {'Accept': 'application/json;version=2'}
        return self._delete(header=_header, path=_path)

    async def delete_user_by_uuid_async(self, uuid: str):
        """
        Delete the enrollment user by enrollment user uuid
        with the v2 endpoint.

        :param uuid: enrollment user uuid
        :return: API response as a dict
        :rtype: dict
        """
        _path = f'/users/{uuid}'
        _header = {'Accept': 'application/json;version=2'}
        return await self._async_delete(header=_header, path=_path)

    def delete_user_by_id(self, user_id):
        """
        Delete the enrollment user by enrollment user id

        :param user_id:
        :return: API response
        """
        path = '/users/{}/delete'.format(user_id)
        return self._delete(path=path)

    async def delete_user_by_id_async(self, user_id):
        """
        Delete the enrollment user by enrollment user id

        :param user_id:
        :return: API response
        """
        path = '/users/{}/delete'.format(user_id)
        return await self._async_delete(path=path)

    def create_device_registration_to_user(
        self,
        user_id: str,
        register_device_details: str
    ) -> RestResponseType:
        """
        Register a device for a specific user

        Args:
            user_id (string)
            register_device_details (dict)

        Returns:
            API response (dict)
        """
        path = '/users/{}/registerdevice'.format(user_id)
        return self._post(path=path, data=register_device_details)

    async def create_device_registration_to_user_async(
        self,
        user_id: str,
        register_device_details: str
    ) -> RestResponseType:
        """
        Register a device for a specific user

        Args:
            user_id (string)
            register_device_details (dict)

        Returns:
            API response (dict)
        """
        path = '/users/{}/registerdevice'.format(user_id)
        return await self._async_post(path=path, data=register_device_details)

    def enrolled_devices(
        self,
        organizational_group_id: str = "",
        organization_group: str = "",
        platform: str = "",
        custom_attributes: str = "",
        serial_number: str = "",
        seen_since: str = "",
        seen_till: str = "",
        enrolled_since: str = "",
        enrolled_till: str = ""
    ):
        '''
        Retrives enrolled device details for the query information
        provided in the request

        :param: organizational_group_id:
        :param: organization_group:
        :param: platform:
        :param: custom_attributes:
        :param: serial_number:
        :param: seen_since:
        :param: seen_till:
        :param: enrolled_since:
        :param: enrolled_till:
        :return: API response
        '''
        temp = ''
        if organizational_group_id:
            temp += f'organizationalgroupid={organizational_group_id}&'
        if organization_group:
            temp += f'organizationgroup={organization_group}&'
        if platform:
            temp += f'platform={platform}&'
        if custom_attributes:
            temp += f'customattributes={custom_attributes}&'
        if serial_number:
            temp += f'serialnumber={serial_number}&'
        if seen_since:
            temp += f'seensince={seen_since}&'
        if seen_till:
            temp += f'seentill={seen_till}&'
        if enrolled_since:
            temp += f'enrolledsince={enrolled_since}&'
        if enrolled_till:
            temp += f'enrolledtill={enrolled_till}&'

        path = f'/users/enrolleddevices/search?{temp}'[:-1]
        response = self._get(path=path)
        return response

    async def enrolled_devices_async(
        self,
        organizational_group_id: str = "",
        organization_group: str = "",
        platform: str = "",
        custom_attributes: str = "",
        serial_number: str = "",
        seen_since: str = "",
        seen_till: str = "",
        enrolled_since: str = "",
        enrolled_till: str = ""
    ):
        '''
        Retrives enrolled device details for the query information
        provided in the request

        :param: organizational_group_id:
        :param: organization_group:
        :param: platform:
        :param: custom_attributes:
        :param: serial_number:
        :param: seen_since:
        :param: seen_till:
        :param: enrolled_since:
        :param: enrolled_till:
        :return: API response
        '''
        temp = ''
        if organizational_group_id:
            temp += f'organizationalgroupid={organizational_group_id}&'
        if organization_group:
            temp += f'organizationgroup={organization_group}&'
        if platform:
            temp += f'platform={platform}&'
        if custom_attributes:
            temp += f'customattributes={custom_attributes}&'
        if serial_number:
            temp += f'serialnumber={serial_number}&'
        if seen_since:
            temp += f'seensince={seen_since}&'
        if seen_till:
            temp += f'seentill={seen_till}&'
        if enrolled_since:
            temp += f'enrolledsince={enrolled_since}&'
        if enrolled_till:
            temp += f'enrolledtill={enrolled_till}&'

        path = f'/users/enrolleddevices/search?{temp}'[:-1]
        response = await self._async_get(path=path)
        return response
