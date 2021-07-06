from scrapy import Request
from scrapy.exceptions import NotConfigured
from urllib.parse import urlencode

from webscrapingapi_scrapy_sdk.request import WebScrapingApiRequest

class WebScrapingApiMiddleware:
    webscrapingapi_api_url = 'https://api.webscrapingapi.com/v1'

    def __init__(self, api_key):
        self.api_key = api_key

    @classmethod
    def from_crawler(cls, crawler):
        api_key = crawler.settings.get('WEBSCRAPINGAPI_API_KEY')
        if not api_key:
            raise NotConfigured

        return cls(api_key=api_key)

    def _get_wsa_url(self, params):
        params.update({
            'api_key': self.api_key,
        })
        params = urlencode(params)
        return f'{self.webscrapingapi_api_url}?{params}'

    def process_request(self, request, spider):
        if not isinstance(request, WebScrapingApiRequest):
            return
        webscrapingapi_url = self._get_wsa_url(request.meta['webscrapingapi_params'])
        new_request = request.replace(cls=Request, url=webscrapingapi_url, meta=request.meta)
        return new_request