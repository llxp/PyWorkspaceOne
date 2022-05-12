"""
Module to manage profiles
"""

from .mdm import MDM


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
        return self._get(path='/profiles/search', header=_header, params=kwargs)
        

    def get_active_win10_profiles(self):
        """
        Get all active Windows 10 Profiles
        """
        return self.searchv2(type='Auto', platform='WinRT', status='Active', ownership='C', orderby='ASC', pagesize=1000)


    def get_profile(self, profile_id):
        """
        Get Profile Details by Profile ID
        """
        _header = {'Accept': 'application/json;version=2'}
        _path = "/profiles/{}".format(profile_id)
        return self._get(self, path=_path, header=_header)

    