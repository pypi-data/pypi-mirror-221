from datetime import datetime
from logging import Logger
from pathlib import Path
from typing import Union

import swisseph as swe

from py_astrolab import CompositeAspects, KrInstance, NatalAspects
from py_astrolab.types import ZodiacType
from py_astrolab.utilities import calculate_position, for_every_planet


class Transits():
    iflag = swe.FLG_SWIEPH+swe.FLG_SPEED
    now = datetime.now()

    def __init__(
            self,
            user: KrInstance,
            name="Now",
            year: int = now.year,
            month: int = now.month,
            day: int = now.day,
            hour: int = now.hour,
            minute: int = now.minute,
            city: str = "",
            nation: str = "",
            lng: Union[int, float] = 0,
            lat: Union[int, float] = 0,
            tz_str: str = "",
            logger: Union[Logger, None] = None,
            geonames_username: str = 'century.boy',
            zodiac_type: ZodiacType = "Tropic",
            house_method: str = "Vehlow",
            online: bool = True,
            new_settings_file: Union[str, Path, None] = None
    ):
        self.user = user
        self.radix = KrInstance(
            name=name,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            city=city,
            nation=nation,
            lng=lng,
            lat=lat,
            tz_str=tz_str,
            logger=logger,
            geonames_username=geonames_username,
            zodiac_type=zodiac_type,
            house_method=house_method,
            online=online
        )
        self.julday = swe.julday(year, month, day, hour, minute)
        self.new_settings_file = new_settings_file
        self.__get_all()

    def __get_all(self):
        self.__natal_aspects()
        self.__transit_aspects()
        self.__lunar_phase()
        self.__new_moon()
        
    def __natal_aspects(self):
        composite_aspects = CompositeAspects(self.radix, self.user, self.new_settings_file)
        natal_aspects = composite_aspects.get_relevant_aspects()
        natal_aspects = [aspect for aspect in natal_aspects if aspect['p1_name'] not in {'Ascendant', 'Descendant', 'Midheaven', 'Imum Coeli'}]
        self.natal_aspects = natal_aspects
        self.points_in_houses = composite_aspects.get_points_in_houses()

    def __transit_aspects(self):
        transit_aspects = NatalAspects(self.radix, self.new_settings_file)
        self.transit_aspects = transit_aspects.get_relevant_aspects()        
    
    def __lunar_phase(self):
        self.lunar_phase = self.radix.lunar_phase
    
    def __new_moon(self):
        jd = self.julday
        sun_deg = swe.calc(jd, 0, self.iflag)[0][0]
        moon_deg = swe.calc(jd, 1, self.iflag)[0][0]
        while abs(sun_deg - moon_deg) > 0.1:
            jd -= 4/(24*60)
            sun_deg = swe.calc(jd, 0, self.iflag)[0][0]
            moon_deg = swe.calc(jd, 1, self.iflag)[0][0]
        new_moon = calculate_position(moon_deg, "New Moon", "Synod")
        new_moon = for_every_planet(self.user, new_moon, moon_deg)
        self.new_moon = new_moon