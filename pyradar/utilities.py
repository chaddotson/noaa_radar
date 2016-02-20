from six.moves import cStringIO

try:
    from urllib2 import build_opener
except ImportError:
    from urllib.request import build_opener

from PIL import Image

__author__ = 'Chad Dotson'

def get_image_from_url(url):
    opener = build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)')]
    response = opener.open(url)
    im = cStringIO(response.read())
    return Image.open(im)
