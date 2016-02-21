from unittest import TestCase

from noaa_radar.radar import Radar

__author__ = 'Chad Dotson'

# Admittedly, these aren't good tests.
class TestNOAA(TestCase):

    def setUp(self):
        self.noaa = Radar()

    def test_get_composite_reflectivity(self):

        image = self.noaa.get_composite_reflectivity('HTX')
        assert image

    def test_get_base_reflectivity(self):
        image = self.noaa.get_base_reflectivity('HTX')
        assert image

    def test_get_storm_relative_motion(self):
        image = self.noaa.get_storm_relative_motion('HTX')
        assert image

    def test_get_base_velocity(self):
        image = self.noaa.get_base_velocity('HTX')
        assert image

    def test_get_one_hour_precipitation(self):
        image = self.noaa.get_one_hour_precipitation('HTX')
        assert image

    def test_get_storm_total_precipitation(self):
        image = self.noaa.get_storm_total_precipitation('HTX')
        assert image