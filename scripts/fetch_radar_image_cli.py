#!/usr/bin/env python

"""
This script will fetch and composite Radar weather radar images.
"""

from argparse import ArgumentParser
from logging import basicConfig, getLogger, INFO, DEBUG

from noaa_radar import Radar

basicConfig(level=INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

logger = getLogger(__name__)


def get_args():
    parser = ArgumentParser(description='Image Scraper')
    parser.add_argument('radar', help='Radar site code')
    parser.add_argument('output_file', help='Output file')
    parser.add_argument('--base_reflectivity', default=False, help='Get base reflectivity.', action='store_true')
    parser.add_argument('--relative_motion', default=False, help='Get storm relative motion.', action='store_true')
    parser.add_argument('--base_velocity', default=False, help='Get base velocity.', action='store_true')
    parser.add_argument('--one_hour', default=False, help='Get one hour precipitation.', action='store_true')
    parser.add_argument('--composite_reflectivity', default=False, help='Get composite reflectivity.',
                        action='store_true')
    parser.add_argument('--storm_total', default=False, help='Get storm total precipitation.', action='store_true')
    parser.add_argument('--background', default='#000000', help='The hex background color.  Default: #000000')
    parser.add_argument('--highways', default=False, help='Include highways', action='store_true')
    parser.add_argument('--counties', default=False, help='Include counties', action='store_true')
    parser.add_argument('--cities', default=False, help='Include cities', action='store_true')
    parser.add_argument('--legend', default=False, help='Include legend', action='store_true')
    parser.add_argument('--warnings', default=False, help='Include warnings', action='store_true')
    parser.add_argument('--rivers', default=False, help='Include rivers', action='store_true')
    parser.add_argument('--topo', default=False, help='Include topography', action='store_true')
    parser.add_argument('-v', '--verbose', help='Verbose log output', default=False, action='store_true')
    return parser.parse_args()


def main():
    try:
        args = get_args()

        if args.verbose:
            getLogger('').setLevel(DEBUG)

        logger.info("Radar site: %s", args.radar)
        logger.info("Output: %s", args.output_file)

        img = None

        noaa = Radar()

        if args.base_reflectivity:
            img = noaa.get_base_reflectivity(args.radar,
                                             background=args.background,
                                             include_highways=args.highways,
                                             include_counties=args.counties,
                                             include_cities=args.cities,
                                             include_legend=args.legend,
                                             include_warnings=args.warnings,
                                             include_rivers=args.rivers,
                                             include_topography=args.topo)

        elif args.composite_reflectivity:
            img = noaa.get_composite_reflectivity(args.radar,
                                                  background=args.background,
                                                  include_highways=args.highways,
                                                  include_counties=args.counties,
                                                  include_cities=args.cities,
                                                  include_legend=args.legend,
                                                  include_warnings=args.warnings,
                                                  include_rivers=args.rivers,
                                                  include_topography=args.topo)

        elif args.relative_motion:
            img = noaa.get_storm_relative_motion(args.radar,
                                                 background=args.background,
                                                 include_highways=args.highways,
                                                 include_counties=args.counties,
                                                 include_cities=args.cities,
                                                 include_legend=args.legend,
                                                 include_warnings=args.warnings,
                                                 include_rivers=args.rivers,
                                                 include_topography=args.topo)

        elif args.base_velocity:
            img = noaa.get_base_velocity(args.radar,
                                         background=args.background,
                                         include_highways=args.highways,
                                         include_counties=args.counties,
                                         include_cities=args.cities,
                                         include_legend=args.legend,
                                         include_warnings=args.warnings,
                                         include_rivers=args.rivers,
                                         include_topography=args.topo)

        elif args.one_hour:
            img = noaa.get_one_hour_precipitation(args.radar,
                                                  background=args.background,
                                                  include_highways=args.highways,
                                                  include_counties=args.counties,
                                                  include_cities=args.cities,
                                                  include_legend=args.legend,
                                                  include_warnings=args.warnings,
                                                  include_rivers=args.rivers,
                                                  include_topography=args.topo)

        elif args.storm_total:
            img = noaa.get_storm_total_precipitation(args.radar,
                                                     background=args.background,
                                                     include_highways=args.highways,
                                                     include_counties=args.counties,
                                                     include_cities=args.cities,
                                                     include_legend=args.legend,
                                                     include_warnings=args.warnings,
                                                     include_rivers=args.rivers,
                                                     include_topography=args.topo)

        else:
            logger.error("A valid radar type must be specified.")

        if img is not None:
            img.save(args.output_file, "JPEG", quality=99)
            logger.info("Done")

    except KeyboardInterrupt:
        logger.info("Cancelling...")


if __name__ == "__main__":
    main()
