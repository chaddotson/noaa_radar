noaa_radar
==========

This package provides tools for downloading and overlaying radar images from the NOAA Ridge radar sites.

.. image:: https://travis-ci.org/chaddotson/noaa_radar.svg?branch=master



From the command line
---------------------
From the command line, it is easy to request images with the provided utility script.  This example
fetches the radar image from the site near Atlanta.  It includes all of the available layers.


.. code-block:: bash

    fetch_radar_image_cli --composite_reflectivity --counties --cities --topo --rivers --legend --warnings --rivers ffc sample.jpg



Some simple code examples.
--------------------------

.. code-block:: python

    from noaa_radar import Radar

    noaa = Radar()

    image = noaa.get_composite_reflectivity('HTX')
    image.save("composite_reflectivity.jpg")

    image = noaa.get_base_reflectivity('HTX')
    image.save("base_reflectivity.jpg")

    image = noaa.get_storm_relative_motion('HTX')
    image.save("storm_relative_motion.jpg")

    image = noaa.get_base_velocity('HTX')
    image.save("base_velocity.jpg")

    image = noaa.get_one_hour_precipitation('HTX')
    image.save("one_hour_precipitation.jpg")

    image = noaa.get_storm_total_precipitation('HTX')
    image.save("storm_total_precipitation.jpg")


For an map of radar sites see, the noaa map at https://www.roc.noaa.gov/wsr88d/Images/WSR-88DCONUSCoverage1000.jpg.
On the map, Radar site names start with a K, just remove it and you have the name string of the site
to request.  For example, 'KHTX' becomes 'HTX'.