"""Yes! I always have my coffee when I watch radar, you know that. - Dark Helmet (Spaceballs)"""

__author__ = 'Chad Dotson'

from PIL import Image
from utilities import get_image_from_url


class NOAA:

    _ridge_radar_format = 'http://radar.weather.gov/ridge/RadarImg/{0}/{1}_{0}_0.gif'
    _ridge_legend_format = 'http://radar.weather.gov/ridge/Legend/{0}/{1}_{0}_Legend_0.gif'
    _ridge_warning_format = 'http://radar.weather.gov/ridge/Warnings/{0}/{1}_Warnings_0.gif'
    _ridge_county_format = 'http://radar.weather.gov/ridge/Overlays/County/{0}/{1}_County_{0}.gif'
    _ridge_highway_format = 'http://radar.weather.gov/ridge/Overlays/Highways/{0}/{1}_Highways_{0}.gif'
    _ridge_topography_format = 'http://radar.weather.gov/ridge/Overlays/Topo/{0}/{1}_Topo_{0}.jpg'
    _ridge_cities_format = 'http://radar.weather.gov/ridge/Overlays/Cities/{0}/{1}_City_{0}.gif'
    _ridge_rivers_format = 'http://radar.weather.gov/ridge/Overlays/Rivers/{0}/{1}_Rivers_{0}.gif'

    _radar_type_map = {
        'N0R': ('Base Reflectivity', 'Short'),
        'N0S': ('Storm Relative Motion', 'Short'),
        'N0V': ('Base Velocity', 'Short'),
        'N1P': ('One-Hour Precipitation', 'Short'),
        'NCR': ('Composite Reflectivity', 'Short'),
        'NTP': ('Storm Total Precipitation', 'Short'),
        'N0Z': ('Base Reflectivity', 'Long'),
    }

    def __init__(self):
        pass

    def _overlay(self, base_image, new_image):
        base_image.paste(new_image, (0, 0), mask=new_image)

    def _add_topography(self, type, tower_id, image):
        topo = get_image_from_url(self._ridge_topography_format.format(self._radar_type_map[type][1], tower_id)).convert("RGBA")
        self._overlay(image, topo)

    def _add_legend(self, type, tower_id, image):
        legend = get_image_from_url(self._ridge_legend_format.format(type, tower_id)).convert("RGBA")
        self._overlay(image, legend)

    def _add_warnings(self, type, tower_id, image):
        warnings = get_image_from_url(self._ridge_warning_format.format(self._radar_type_map[type][1], tower_id)).convert("RGBA")
        self._overlay(image, warnings)

    def _add_counties(self, type, tower_id, image):
        county = get_image_from_url(self._ridge_county_format.format(self._radar_type_map[type][1], tower_id)).convert("RGBA")
        self._overlay(image, county)

    def _add_highways(self, type, tower_id, image):
        highway = get_image_from_url(self._ridge_highway_format.format(self._radar_type_map[type][1], tower_id)).convert("RGBA")
        self._overlay(image, highway)

    def _add_cities(self, type, tower_id, image):
        cities = get_image_from_url(self._ridge_cities_format.format(self._radar_type_map[type][1], tower_id)).convert("RGBA")
        self._overlay(image, cities)

    def _add_rivers(self, type, tower_id, image):
        if self._radar_type_map[type][1] == 'Short':
            cities = get_image_from_url(self._ridge_rivers_format.format(self._radar_type_map[type][1], tower_id)).convert("RGBA")
            self._overlay(image, cities)

    def _build_radar_image(self, tower_id, type, background='#000000', include_topography=True, include_legend=True, include_counties=True, include_warnings=True, include_highways=True, include_cities=True, include_rivers=True):
        type = type.upper()
        tower_id = tower_id.upper()

        radar = get_image_from_url(self._ridge_radar_format.format(type, tower_id)).convert("RGBA")

        combined_image = Image.new("RGB", radar.size, background)

        if include_topography:
            self._add_topography(type, tower_id, combined_image)

        combined_image.paste(radar, (0, 0), mask=radar)

        if include_rivers:
            self._add_rivers(type, tower_id, combined_image)

        if include_counties:
            self._add_counties(type, tower_id, combined_image)

        if include_highways:
            self._add_highways(type, tower_id, combined_image)

        if include_cities:
            self._add_cities(type, tower_id, combined_image)

        if include_warnings:
            self._add_warnings(type, tower_id, combined_image)

        if include_legend:
            self._add_legend(type, tower_id, combined_image)

        return combined_image

    def get_composite_reflectivity(self, tower_id, background='#000000', include_legend=True, include_counties=True, include_warnings=True, include_highways=True, include_cities=True):
        return self._build_radar_image(tower_id, "NCR", background, include_legend, include_counties, include_warnings, include_highways, include_cities)

    def get_base_reflectivity(self, tower_id, background='#000000', include_legend=True, include_counties=True, include_warnings=True, include_highways=True, include_cities=True):
        return self._build_radar_image(tower_id, "N0R", background, include_legend, include_counties, include_warnings, include_highways, include_cities)

    def get_storm_relative_motion(self, tower_id, background='#000000', include_legend=True, include_counties=True, include_warnings=True, include_highways=True, include_cities=True):
        return self._build_radar_image(tower_id, "N0S", background, include_legend, include_counties, include_warnings, include_highways, include_cities)

    def get_base_velocity(self, tower_id, background='#000000', include_legend=True, include_counties=True, include_warnings=True, include_highways=True, include_cities=True):
        return self._build_radar_image(tower_id, "N0V", background, include_legend, include_counties, include_warnings, include_highways, include_cities)

    def get_one_hour_precipitation(self, tower_id, background='#000000', include_legend=True, include_counties=True, include_warnings=True, include_highways=True, include_cities=True):
        return self._build_radar_image(tower_id, "N1P", background, include_legend, include_counties, include_warnings, include_highways, include_cities)

    def get_storm_total_precipitation(self, tower_id, background='#000000', include_legend=True, include_counties=True, include_warnings=True, include_highways=True, include_cities=True):
        return self._build_radar_image(tower_id, "NTP", background, include_legend, include_counties, include_warnings, include_highways, include_cities)

#noaa = NOAA()
#
#image = noaa.get_composite_reflectivity('HTX')
#image.save("composite_reflectivity.jpg")
#
#image = noaa.get_base_reflectivity('HTX')
#image.save("base_reflectivity.jpg")
#
#image = noaa.get_storm_relative_motion('HTX')
#image.save("storm_relative_motion.jpg")
#
#image = noaa.get_base_velocity('HTX')
#image.save("base_velocity.jpg")
#
#image = noaa.get_one_hour_precipitation('HTX')
#image.save("one_hour_precipitation.jpg")
#
#image = noaa.get_storm_total_precipitation('HTX')
#image.save("storm_total_precipitation.jpg")