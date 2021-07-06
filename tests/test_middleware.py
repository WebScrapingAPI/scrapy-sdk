import pytest
from scrapy import Request
from scrapy.http import Response
from scrapy.utils.test import get_crawler
from urllib.parse import urlencode

from webscrapingapi_scrapy_sdk import WebScrapingApiMiddleware, WebScrapingApiRequest

DEFAULT_API_URL = WebScrapingApiMiddleware.webscrapingapi_api_url
DEFAULT_API_KEY = 'API-KEY'
DEFAULT_URL = 'https://example.com'

def get_wsa_url(api_url, api_key, params={}):
    params.update({
        'api_key': api_key,
    })
    params = urlencode(params)
    return f'{api_url}?{params}'

@pytest.fixture
def wsa_middleware(api_key=DEFAULT_API_KEY):
    crawler = get_crawler(settings_dict={'WEBSCRAPINGAPI_API_KEY': api_key})
    return WebScrapingApiMiddleware.from_crawler(crawler)

@pytest.fixture
def wsa_request(url=DEFAULT_URL):
    return WebScrapingApiRequest(url)

@pytest.fixture
def wsa_response(api_key=DEFAULT_API_KEY, url=DEFAULT_URL):
    url = get_wsa_url(DEFAULT_API_URL, api_key, {"url": url})
    return Response(url)

def test_process_request(wsa_middleware, wsa_request):
    '''It should return a normal Request with a WebScrapingAPI API url'''
    url = get_wsa_url(DEFAULT_API_URL, DEFAULT_API_KEY, {"url": DEFAULT_URL})
    new_req = wsa_middleware.process_request(wsa_request, None)
    assert isinstance(new_req, Request)
    assert new_req.url == url