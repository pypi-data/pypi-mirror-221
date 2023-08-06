import json
from pathlib import Path
from typing import Union

import swisseph as swe

from py_astrolab import KrInstance
from py_astrolab.utilities import calculate_position, for_every_planet


class Transits():
    def __init__(
            self, kr_object: KrInstance,
            new_settings_file: Union[str, Path, None] = None
    ):
        self.user = kr_object
        self.new_settings_file = new_settings_file
        self._parse_json_settings()
    
    def prev_new_moon_calc(self, start_date):
        jd_start = swe.julday(start_date.year, start_date.month, start_date.day, start_date.hour, start_date.minute)
        jd = jd_start
        __iflag = swe.FLG_SWIEPH+swe.FLG_SPEED
        sun_deg = swe.calc(jd, 0, __iflag)[0][0]
        moon_deg = swe.calc(jd, 1, __iflag)[0][0]
        while abs(sun_deg - moon_deg) > 0.1:
            jd -= 4/(24*60)
            sun_deg = swe.calc(jd, 0, __iflag)[0][0]
            moon_deg = swe.calc(jd, 1, __iflag)[0][0]
        new_moon = calculate_position(moon_deg, "New Moon", "Synod")
        new_moon = for_every_planet(self.user, new_moon, moon_deg)
        return new_moon

    def _parse_json_settings(self):
        # Load settings file
        DATADIR = Path(__file__).parent

        if not self.new_settings_file:
            settings_file = DATADIR / "kr.config.json"
        else:
            settings_file = Path(self.new_settings_file)

        with open(settings_file, 'r', encoding="utf-8", errors='ignore') as f:
            settings = json.load(f)

        self.colors_settings = settings['colors']
        self.planets_settings = settings['planets']
        self.axes_settings = settings['axes']
        self.aspects_settings = settings['aspects']
        self.axes_orbit_settings = settings['axes_orbit']