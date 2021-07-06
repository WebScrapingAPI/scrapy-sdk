import copy
from scrapy import Request

class WebScrapingApiRequest(Request):
    def __init__(self, url: str, params: dict = None, data: dict = None, headers: dict = None, meta = None, **kwargs):
        meta = copy.deepcopy(meta) or {}
        
        if not params:
            params = {}

        params['url'] = url
        
        if headers:
            params['keep_headers'] = 1
        else:
            headers = {}

        meta['webscrapingapi_params'] = params;

        super().__init__(
            url,
            headers=headers,
            body=data,
            meta=meta,
            **kwargs
        )