"""
Module to manage smartgroups (add and remove)
"""

from .mdm import MDM
from ..client import Client
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

    def get_smartgroup(self, smartgroup_id: str):
        """
        Get a specific smartgroup
        """
        return self._get(path=f'/smartgroups/{smartgroup_id}')

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
    ):
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
    ):
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

    def delete_smartgroup(self, smartgroup_id: str):
        """
        Delete a smartgroup
        """
        return self._delete(path=f'/smartgroups/{smartgroup_id}')

    def get_devices(self, smartgroup_id: str):
        """
        Get all devices of a smartgroup
        """
        return self._get(path=f'/smartgroups/{smartgroup_id}/devices')

    def get_apps(self, smartgroup_id: str):
        """
        Get all apps of a smartgroup
        """
        return self._get(path=f'/smartgroups/{smartgroup_id}/apps')
