# -*- coding: utf-8 -*-
"""
    :copyright: ©2018 by IPIP.net
"""

from .database import Reader


class DistrictInfo:
    country_name = ""
    region_name = ""
    city_name = ""
    district_domain = ""
    china_admin_code = ""
    covering_radius = ""
    latitude = ""
    longitude = ""

    def __init__(self, **kwargs):
        self._map = kwargs
        for key in self._map:
            self.__setattr__(key, self._map[key])

    def __getattr__(self, item):
        return self._map.get(item, "")


class District:

    db = None

    def __init__(self, name):
        self.db = Reader(name)

    def find(self, addr, language):
        return self.db.find(addr, language)

    def find_map(self, addr, language):
        return self.db.find_map(addr, language)

    def find_info(self, addr, language):
        m = self.db.find_map(addr, language)
        if m is None:
            return None
        return DistrictInfo(**m)

    def is_ipv4(self):
        return self.db.is_support_ipv4()

    def is_ipv6(self):
        return self.db.is_support_ipv6()

    def languages(self):
        return self.db.support_languages()

    def fields(self):
        return self.db.support_fields()

    def build_time(self):
        return self.db.build_utc_time()