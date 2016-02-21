from os.path import dirname, join
from setuptools import setup


version = '0.7.2'


def read(fname):
    return open(join(dirname(__file__), fname)).read()


with open("requirements.txt", "r'") as f:
    install_reqs = f.readlines()

setup(name='noaa_radar',
      version=version,
      author="Chad Dotson",
      author_email="chad@cdotson.com",
      description="Tools for downloading and overlaying radar images from the Ridge radar sites.",
      license="GNUv3",
      keywords=["noaa", "radar", "weather"],
      url="https://github.com/chaddotson/noaa_radar",
      download_url = 'https://github.com/chaddotson/noaa_radar/tarball/0.7.2',
      packages=['noaa_radar', 'scripts'],
      long_description=read("README.rst"),
      install_requires=install_reqs,
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'fetch_radar_image_cli = scripts.fetch_radar_image_cli:main',
          ]
      },
      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Utilities",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
      ],
      test_suite='nose.collector',
      tests_require=['nose'],

)
