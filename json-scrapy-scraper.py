import scrapy
import os
from os.path import basename

class CrypkoJSONSpider(scrapy.Spider):
    
    # required spider vars
    name = 'crypko-json'
    allowed_domains = ['crypko.ai']
    
    json_url = 'https://api.crypko.ai/crypkos/'
    
    #start_urls sets the urls of the download locations
    start_json_urls = [] #56798
    
    custom_settings = {
            'CONCURRENT_REQUESTS': 64,
            'CONCURRENT_REQUESTS_PER_DOMAIN': 32
    }
    
    for i in range(1,712044):
        start_json_urls.append(json_url + str(i) + "/detail")
        
    if not os.path.exists("json"):
        os.makedirs("json")
    
    file_name = ''
    
    def parse_json(self, response):
        with open("json/" + basename(response.request.url.split("/detail")[0]) + "-detail.json", "wb") as f:
            f.write(response.body)
            
    def start_requests(self):
        for url in self.start_json_urls:
            yield scrapy.Request(url, self.parse_json)
    
