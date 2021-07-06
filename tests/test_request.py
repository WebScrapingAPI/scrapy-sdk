import urllib.parse

from webscrapingapi_scrapy_sdk import WebScrapingApiRequest

DEFAULT_URL = 'https://example.com'

def test_webscrapingapi_request():
    '''It should add the encoded url to the request meta'''
    req = WebScrapingApiRequest('https://example.com?p=1')
    assert req.meta['webscrapingapi_params']['url'] == 'https://example.com?p=1'

def test_webscrapingapi_params():
    '''It should add the parameters to the request meta'''
    req = WebScrapingApiRequest(DEFAULT_URL, params={'render_js': False})
    assert req.meta['webscrapingapi_params']['render_js'] is False

def test_webscrapingapi_headers():
    '''It should add the headers to the request'''
    req = WebScrapingApiRequest(DEFAULT_URL, headers={'Accept-Language': 'En-US'})
    assert req.headers.get('Accept-Language') == b'En-US'