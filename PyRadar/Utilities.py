__author__ = 'Chad Dotson'

import cStringIO
import urllib2

from PIL import Image

def get_image_from_url(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)')]
    response = opener.open(url)
    im = cStringIO.StringIO(response.read())
    return Image.open(im)
