"""
Module to manage smartgroups (add and remove)
"""

from pyws1uem.mdm.mdm import MDM
from pyws1uem.client import Client, RestResponseType
from typing import List, Dict


class Smartgroups(MDM):
    """
    Base Smartgroups Class

    Contains REST-API Calls to retrieve and manage smartgroups
    """

    def __init__(self, client: Client):
        """
        Initialize Smartgroups Class

        :param client: Client Object
        """
        MDM.__init__(self, client)

    def get_smartgroup(self, smartgroup_id: str) -> RestResponseType:
        """
        Get a specific smartgroup
        """
        return self._get(path=f'/smartgroups/{smartgroup_id}')

    async def get_smartgroup_async(self, smartgroup_id: str) -> RestResponseType:  # noqa: E501
        """
        Get a specific smartgroup
        """
        return await self._async_get(path=f'/smartgroups/{smartgroup_id}')

    def add_smartgroup(
        self,
        name: str,
        tags: List[str] = [],
        criteria_type: str = 'All',
        managed_by_organization_group_id: str = '1',
        organization_groups: List[Dict[str, str]] = [],
        user_groups: List[Dict[str, str]] = [],
        ownerships: List[str] = [],
        platforms: List[str] = [],
        models: List[str] = [],
        operating_systems: List[Dict[str, str]] = [],
        user_additions: List[Dict[str, str]] = [],
        device_additions: List[Dict[str, str]] = [],
        user_exclusions: List[Dict[str, str]] = [],
        device_exclusions: List[Dict[str, str]] = [],
        user_groups_exclusions: List[Dict[str, str]] = [],
        management_types: List[str] = [],
        enrollment_categories: List[str] = [],
        oem_and_models: List[Dict[str, str]] = [],
        cpu_architectures: List[str] = [],
    ) -> RestResponseType:
        """
        Add a new smartgroup
        """
        payload = {
            'Name': name,
            'Tags': tags,
            'CriteriaType': criteria_type,
            'MangedByOrganizationGroupId': managed_by_organization_group_id,
            'OrganizationGroups': organization_groups,
            'UserGroups': user_groups,
            'Ownerships': ownerships,
            'Platforms': platforms,
            'Models': models,
            'OperatingSystems': operating_systems,
            'UserAdditions': user_additions,
            'DeviceAdditions': device_additions,
            'UserExclusions': user_exclusions,
            'DeviceExclusions': device_exclusions,
            'UserGroupsExclusions': user_groups_exclusions,
            'ManagementTypes': management_types,
            'EnrollmentCategories': enrollment_categories,
            'OemAndModels': oem_and_models,
            'CpuArchitectures': cpu_architectures,
        }
        return self._post(path='/smartgroups', json=payload)

    async def add_smartgroup_async(
        self,
        name: str,
        tags: List[str] = [],
        criteria_type: str = 'All',
        managed_by_organization_group_id: str = '1',
        organization_groups: List[Dict[str, str]] = [],
        user_groups: List[Dict[str, str]] = [],
        ownerships: List[str] = [],
        platforms: List[str] = [],
        models: List[str] = [],
        operating_systems: List[Dict[str, str]] = [],
        user_additions: List[Dict[str, str]] = [],
        device_additions: List[Dict[str, str]] = [],
        user_exclusions: List[Dict[str, str]] = [],
        device_exclusions: List[Dict[str, str]] = [],
        user_groups_exclusions: List[Dict[str, str]] = [],
        management_types: List[str] = [],
        enrollment_categories: List[str] = [],
        oem_and_models: List[Dict[str, str]] = [],
        cpu_architectures: List[str] = [],
    ) -> RestResponseType:
        """
        Add a new smartgroup
        """
        payload = {
            'Name': name,
            'Tags': tags,
            'CriteriaType': criteria_type,
            'MangedByOrganizationGroupId': managed_by_organization_group_id,
            'OrganizationGroups': organization_groups,
            'UserGroups': user_groups,
            'Ownerships': ownerships,
            'Platforms': platforms,
            'Models': models,
            'OperatingSystems': operating_systems,
            'UserAdditions': user_additions,
            'DeviceAdditions': device_additions,
            'UserExclusions': user_exclusions,
            'DeviceExclusions': device_exclusions,
            'UserGroupsExclusions': user_groups_exclusions,
            'ManagementTypes': management_types,
            'EnrollmentCategories': enrollment_categories,
            'OemAndModels': oem_and_models,
            'CpuArchitectures': cpu_architectures,
        }
        return await self._async_post(path='/smartgroups', json=payload)

    def update_smartgroup(
        self,
        smartgroup_id: str,
        name: str,
        tags: List[str] = [],
        criteria_type: str = 'All',
        managed_by_organization_group_id: str = '1',
        organization_groups: List[Dict[str, str]] = [],
        user_groups: List[Dict[str, str]] = [],
        ownerships: List[str] = [],
        platforms: List[str] = [],
        models: List[str] = [],
        operating_systems: List[Dict[str, str]] = [],
        user_additions: List[Dict[str, str]] = [],
        device_additions: List[Dict[str, str]] = [],
        user_exclusions: List[Dict[str, str]] = [],
        device_exclusions: List[Dict[str, str]] = [],
        user_groups_exclusions: List[Dict[str, str]] = [],
        management_types: List[str] = [],
        enrollment_categories: List[str] = [],
        oem_and_models: List[Dict[str, str]] = [],
        cpu_architectures: List[str] = []
    ) -> RestResponseType:
        """
        Update a smartgroup
        """
        payload = {
            'Name': name,
            'Tags': tags,
            'CriteriaType': criteria_type,
            'ManagedByOrganizationGroupId': managed_by_organization_group_id,
            'OrganizationGroups': organization_groups,
            'UserGroups': user_groups,
            'Ownerships': ownerships,
            'Platforms': platforms,
            'Models': models,
            'OperatingSystems': operating_systems,
            'UserAdditions': user_additions,
            'DeviceAdditions': device_additions,
            'UserExclusions': user_exclusions,
            'DeviceExclusions': device_exclusions,
            'UserGroupsExclusions': user_groups_exclusions,
            'ManagementTypes': management_types,
            'EnrollmentCategories': enrollment_categories,
            'OemAndModels': oem_and_models,
            'CpuArchitectures': cpu_architectures,
        }
        return self._put(path=f'/smartgroups/{smartgroup_id}', json=payload)

    async def update_smartgroup_async(
        self,
        smartgroup_id: str,
        name: str,
        tags: List[str] = [],
        criteria_type: str = 'All',
        managed_by_organization_group_id: str = '1',
        organization_groups: List[Dict[str, str]] = [],
        user_groups: List[Dict[str, str]] = [],
        ownerships: List[str] = [],
        platforms: List[str] = [],
        models: List[str] = [],
        operating_systems: List[Dict[str, str]] = [],
        user_additions: List[Dict[str, str]] = [],
        device_additions: List[Dict[str, str]] = [],
        user_exclusions: List[Dict[str, str]] = [],
        device_exclusions: List[Dict[str, str]] = [],
        user_groups_exclusions: List[Dict[str, str]] = [],
        management_types: List[str] = [],
        enrollment_categories: List[str] = [],
        oem_and_models: List[Dict[str, str]] = [],
        cpu_architectures: List[str] = []
    ) -> RestResponseType:
        """
        Update a smartgroup
        """
        payload = {
            'Name': name,
            'Tags': tags,
            'CriteriaType': criteria_type,
            'ManagedByOrganizationGroupId': managed_by_organization_group_id,
            'OrganizationGroups': organization_groups,
            'UserGroups': user_groups,
            'Ownerships': ownerships,
            'Platforms': platforms,
            'Models': models,
            'OperatingSystems': operating_systems,
            'UserAdditions': user_additions,
            'DeviceAdditions': device_additions,
            'UserExclusions': user_exclusions,
            'DeviceExclusions': device_exclusions,
            'UserGroupsExclusions': user_groups_exclusions,
            'ManagementTypes': management_types,
            'EnrollmentCategories': enrollment_categories,
            'OemAndModels': oem_and_models,
            'CpuArchitectures': cpu_architectures,
        }
        return await self._async_put(path=f'/smartgroups/{smartgroup_id}', json=payload)  # noqa: E501

    def delete_smartgroup(self, smartgroup_id: str) -> RestResponseType:
        """
        Delete a smartgroup
        """
        return self._delete(path=f'/smartgroups/{smartgroup_id}')

    async def delete_smartgroup_async(self, smartgroup_id: str) -> RestResponseType:  # noqa: E501
        """
        Delete a smartgroup
        """
        return await self._async_delete(path=f'/smartgroups/{smartgroup_id}')

    def get_devices(self, smartgroup_id: str) -> RestResponseType:
        """
        Get all devices of a smartgroup
        """
        return self._get(path=f'/smartgroups/{smartgroup_id}/devices')

    async def get_devices_async(self, smartgroup_id: str) -> RestResponseType:
        """
        Get all devices of a smartgroup
        """
        return await self._async_get(path=f'/smartgroups/{smartgroup_id}/devices')  # noqa: E501

    def get_apps(self, smartgroup_id: str) -> RestResponseType:
        """
        Get all apps of a smartgroup
        """
        return self._get(path=f'/smartgroups/{smartgroup_id}/apps')

    async def get_apps_async(self, smartgroup_id: str) -> RestResponseType:
        """
        Get all apps of a smartgroup
        """
        return await self._async_get(path=f'/smartgroups/{smartgroup_id}/apps')

    def search_smartgroups(self, search_term: str) -> RestResponseType:
        """
        Search smartgroups by name
        """
        return self._get(path=f'/smartgroups/search?name={search_term}')

    async def search_smartgroups_async(self, search_term: str) -> RestResponseType:  # noqa: E501
        """
        Search smartgroups by name
        """
        return await self._async_get(path=f'/smartgroups/search?name={search_term}')  # noqa: E501
