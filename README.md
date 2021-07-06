# WebScrapingAPI Scrapy SDK

WebScrapingApi is an API that allows scraping websites while using rotating proxies to prevent bans. This SDK for Scrapy allows you to create a Scrapy spider, integrated with our API.

## API Key

To use the API and the SDK you will need a API Key. You can get one by registering at [WebScrapingApi](https://app.webscrapingapi.com/register)

## Installation

Run the following command in the main folder of your project:

```
pip install webscrapingapi-scrapy-sdk
```

## Usage

To use our API combined with Scrapy you first should install scrapy and create a new project by running these commands:

```
pip install scrapy
pip install webscrapingapi-scrapy-sdk
scrapy startproject myproject
cd myproject
```

Now that Scrapy created our project, the first step is to update the project's settings by adding at the end of the file /myproject/myproject/settings.py the following lines:

```
WEBSCRAPINGAPI_API_KEY = 'YOUR_API_KEY'

DOWNLOADER_MIDDLEWARES = {
    'webscrapingapi_scrapy_sdk.WebScrapingApiMiddleware': 543,
}

CONCURRENT_REQUESTS = 1
```

The next part is creating the spider. We will name our spider example.py and we will place it in myproject/myproject/spiders/

The source code for the spider is:

```
from webscrapingapi_scrapy_sdk import WebScrapingApiSpider, WebScrapingApiRequest

import urllib.parse as urlparse
from urllib.parse import parse_qs

class ExampleSpider(WebScrapingApiSpider):
    name = 'example'

    def start_requests(self):
        start_urls = [
            'https://httpbin.org',
            'http://httpbin.org/ip',
        ]
        for url in start_urls:
            yield WebScrapingApiRequest(url, params={
                # API Parameters
                # Set to 0 (off, default) or 1 (on) depending on whether or not to render JavaScript on the target web page. JavaScript rendering is done by using a browser.
                'render_js': 1,
                # Set datacenter (default) or residential depending on whether proxy type you want to use for your scraping request. Please note that a single residential proxy API request is counted as 25 API requests.
                'proxy_type': 'datacenter',
                # Specify the 2-letter code of the country you would like to use as a proxy geolocation for your scraping API request. Supported countries differ by proxy type, please refer to the Proxy Locations section for details.
                'country': 'us',
                # Set depending on whether or not to use the same proxy address to your request.
                'session': 1,
                # Specify the maximum timeout in milliseconds you would like to use for your scraping API request. In order to force a timeout, you can specify a number such as 1000. This will abort the request after 1000ms and return whatever HTML response was obtained until this point in time.
                'timeout': 10000,
                # Set desktop (default) or mobile or tablet, depending on whether the device type you want to your for your scraping request.
                'device': 'desktop',
                # Specify the option you would like to us as conditional for your scraping API request. Can only be used when the parameter render_js=1 is activated.
                'wait_until': 'domcontentloaded',
                # Some websites may use javascript frameworks that may require a few extra seconds to load their content. This parameters specifies the time in miliseconds to wait for the website. Recommended values are in the interval 5000-10000.
                'wait_for': 0,
            }, headers={
                # API Headers
                'authorization': 'bearer test',
                # Specify custom cookies to be passed to the request.
                'cookie': 'test_cookie=abc; cookie_2=def'
            })

    def parse(self, response):
        parsed_url = urlparse.urlparse(response.url)
        page = parse_qs(parsed_url.query)['url'][0].split("/")[2:]
        page = "-".join(page)
        filename = f'page-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
```

To understand better the WebScrapingAPI parameters, please read [our documentation](https://docs.webscrapingapi.com/#request-parameters)

Now that we have the spider, the only thing left to do is run it, by executing the following command:

```
scrapy crawl example
```

This spider should create 2 html files in the project folder, with the html sources from the links: https://httpbin.org and http://httpbin.org/ip 

For any questions or issues that you may find, please contact us via the [contact page](https://www.webscrapingapi.com/contact/)