from setuptools import setup

with open("requirements.txt", "r'") as f:
    install_reqs = f.readlines()

setup(name='pyradar',
      author="Chad Dotson",
      author_email="chad@cdotson.com",
      url="http://www.cdotson.com",
      version='1.0',
      packages=['PyRadar', 'scripts'],
      install_requires=install_reqs,
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'fetch_radar_image_cli = bin.fetch_radar_image_cli:main',
          ]
      }
)
