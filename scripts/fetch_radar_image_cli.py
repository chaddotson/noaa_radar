
"""
This script is responsible for checking twitter for direct messages and putting the source/message on the queue.
"""

#!/usr/bin/env python

from argparse import ArgumentParser
from logging import basicConfig, getLogger, INFO, DEBUG

from PyRadar import NOAA


basicConfig(level=INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

logger = getLogger(__name__)

def get_args():
    parser = ArgumentParser(description='Image Scraper')
    parser.add_argument('radar', help='Radar site code')
    parser.add_argument('output_file', help='Output file')
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

        logger.info("Retrieving %s", args.radar)
        logger.info("Saving to %s", args.output_file)

        img = NOAA().get_base_reflectivity(args.radar,
                                           background=args.background,
                                           include_highways=args.highways,
                                           include_counties=args.counties,
                                           include_cities=args.cities,
                                           include_legend=args.legend,
                                           include_warnings=args.warnings,
                                           include_rivers=args.rivers,
                                           include_topography=args.topo)

        img.save(args.output_file, "JPEG", quality=99)

        logger.info("Done")

    except KeyboardInterrupt:
            logger.info("Cancelling...")


if __name__ == "__main__":
    main()
