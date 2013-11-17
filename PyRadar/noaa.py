__author__ = 'Chad Dotson'

from PIL import Image
import os
import urllib2
import cStringIO
import Image
import ImageFont, ImageDraw, ImageOps

import PIL

class Utilities:
    @staticmethod
    def get_image_from_url(url):

        print url


        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)')]
        response = opener.open(url)
        im = cStringIO.StringIO(response.read())
        return Image.open(im)



class NOAA:
    ridge_radar_format = 'http://radar.weather.gov/ridge/RadarImg/{0}/{1}_{0}_0.gif'
    ridge_legend_format = 'http://radar.weather.gov/ridge/Legend/{0}/{1}_{0}_Legend_0.gif'
    ridge_warning_format = 'http://radar.weather.gov/ridge/Warnings/{0}/{1}_Warnings_0.gif'
    ridge_county_format = 'http://radar.weather.gov/ridge/Overlays/County/{0}/{1}_County_{0}.gif'
    ridge_highway_format = 'http://radar.weather.gov/ridge/Overlays/Highways/{0}/{1}_Highways_{0}.gif'
    ridge_topography_format = 'http://radar.weather.gov/ridge/Overlays/Topo/{0}/{1}_Topo_{0}.jpg'
    ridge_cities_format = 'http://radar.weather.gov/ridge/Overlays/Cities/{0}/{1}_City_{0}.gif'
    ridge_rivers_format = 'http://radar.weather.gov/ridge/Overlays/Rivers/{0}/{1}_Rivers_{0}.gif'

    #countyPath="$radarLocalPath$radarName/resources/county.gif"

    radar_type_map = {
        'N0R': ('Base Reflectivity', 'Short'),
        'N0S': ('Storm Relative Motion', 'Short'),
        'NOV': ('Base Velocity', 'Short'),
        'N1P': ('One-Hour Precipitation', 'Short'),
        'NCR': ('Composite Reflectivity', 'Short'),
        'NTP': ('Storm Total Precipitation', 'Short'),
        'N0Z': ('Base Reflectivity', 'Long'),
    }

    def overlay(self, base_image, new_image):
        base_image.paste(new_image, (0, 0), mask=new_image)

    def add_topography(self, type, tower_id, image):
        topo = Utilities.get_image_from_url(self.ridge_topography_format.format(self.radar_type_map[type][1], tower_id)).convert("RGBA")
        self.overlay(image, topo)

    def add_legend(self, type, tower_id, image):
        legend = Utilities.get_image_from_url(self.ridge_legend_format.format(type, tower_id)).convert("RGBA")
        self.overlay(image, legend)

    def add_warnings(self, type, tower_id, image):
        warnings = Utilities.get_image_from_url(self.ridge_warning_format.format(self.radar_type_map[type][1], tower_id)).convert("RGBA")
        self.overlay(image, warnings)

    def add_counties(self, type, tower_id, image):
        county = Utilities.get_image_from_url(self.ridge_county_format.format(self.radar_type_map[type][1], tower_id)).convert("RGBA")
        self.overlay(image, county)

    def add_highways(self, type, tower_id, image):
        highway = Utilities.get_image_from_url(self.ridge_highway_format.format(self.radar_type_map[type][1], tower_id)).convert("RGBA")
        self.overlay(image, highway)

    def add_cities(self, type, tower_id, image):
        cities = Utilities.get_image_from_url(self.ridge_cities_format.format(self.radar_type_map[type][1], tower_id)).convert("RGBA")
        self.overlay(image, cities)

    def add_rivers(self, type, tower_id, image):
        if self.radar_type_map[type][1] == 'Short':
            cities = Utilities.get_image_from_url(self.ridge_rivers_format.format(self.radar_type_map[type][1], tower_id)).convert("RGBA")
            self.overlay(image, cities)



    def build_radar_image(self, tower_id, type, background='#FFFFFF', include_topography=True, include_legend=True, include_counties=True, include_warnings=True, include_highways=True, include_cities=True, include_rivers=True):
        type = type.upper()
        tower_id = tower_id.upper()

        radar = Utilities.get_image_from_url(self.ridge_radar_format.format(type, tower_id)).convert("RGBA")

        short_or_long_range = self.radar_type_map[type][1]

        combined_image = Image.new("RGB", radar.size, background)


        if include_topography:
            self.add_topography(type,tower_id,combined_image)

        combined_image.paste(radar, (0, 0), mask=radar)

        if include_counties:
            self.add_counties(type, tower_id, combined_image)

        if include_highways:
            self.add_highways(type, tower_id, combined_image)

        if include_cities:
            self.add_cities(type, tower_id, combined_image)

        if include_rivers:
            self.add_rivers(type, tower_id, combined_image)

        if include_warnings:
            self.add_warnings(type, tower_id, combined_image)

        if include_legend:
            self.add_legend(type, tower_id, combined_image)


        #    legend = Utilities.get_image_from_url(self.ridge_legend_format.format(type, tower_id)).convert("RGBA")
        #    combined_image.paste(legend, (0, 0), mask=legend)




        return combined_image




    def get_composite_reflectivity(self, tower_id, include_legend=True, include_counties = True, include_warnings = True, include_highways = True, include_cities = True ):

        return self.build_radar_image(tower_id, "NCR", include_topography=False)


noaa = NOAA()


image = noaa.get_composite_reflectivity('HTX')

image.save("test.gif")
