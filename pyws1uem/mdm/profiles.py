"""
Module to manage profiles
"""

from pyws1uem.mdm.mdm import MDM


class Profiles(MDM):
    """
    Base Profiles Class
    """

    def __init__(self, client):
        MDM.__init__(self, client)

    def searchv2(self, **kwargs):
        """
        Search for profiles
        """
        _header = {'Accept': 'application/json;version=2'}
        return self._get(path='/profiles/search', header=_header, params=kwargs)  # noqa: E501

    async def searchv2_async(self, **kwargs):
        """
        Search for profiles
        """
        _header = {'Accept': 'application/json;version=2'}
        return await self._async_get(path='/profiles/search', header=_header, params=kwargs)  # noqa: E501

    def get_active_win10_profiles(self):
        """
        Get all active Windows 10 Profiles
        """
        return self.searchv2(type='Auto', platform='WinRT', status='Active', ownership='C', orderby='ASC', pagesize=1000)  # noqa: E501

    async def get_active_win10_profiles_async(self):
        """
        Get all active Windows 10 Profiles
        """
        return await self.searchv2_async(type='Auto', platform='WinRT', status='Active', ownership='C', orderby='ASC', pagesize=1000)  # noqa: E501

    def get_profile(self, profile_id):
        """
        Get Profile Details by Profile ID
        """
        _header = {'Accept': 'application/json;version=2'}
        _path = f"/profiles/{profile_id}"
        return self._get(path=_path, header=_header)

    async def get_profile_async(self, profile_id):
        """
        Get Profile Details by Profile ID
        """
        _header = {'Accept': 'application/json;version=2'}
        _path = f"/profiles/{profile_id}"
        return await self._async_get(path=_path, header=_header)
