import scrapy
import os
from os.path import basename



class UserScraper(scrapy.Spider):
    # required spider vars
    name = 'crypko'
    allowed_domains = ['crypko.ai']
    
    s_url = 'https://s.crypko.ai/u/'
    
    address_file = 'deduped_addresses.txt'
    
    #start_urls sets the urls of the download locations
    start_urls = []
    
    custom_settings = {
            'CONCURRENT_REQUESTS': 64,
            'CONCURRENT_REQUESTS_PER_DOMAIN': 64
    }
    
    if not os.path.exists("json-users"):
        os.makedirs("json-users")
    
    with open(address_file, "r") as f:
        contents = f.read().split("\n")
        for addr in contents:
            start_urls.append(s_url + addr)
            
            
    def parse(self, response):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_json)
            
    def parse_json(self, response):
        with open("json-users/" + basename(response.request.url) + "-.json", "wb") as f:
            f.write(response.body)
