import scrapy
import os
from os.path import basename

# Scrapy spider class
class CrypkoImgSpider(scrapy.Spider):
    
    # required spider vars
    name = 'crypko'
    allowed_domains = ['crypko.ai']
    
    s_url = 'https://s.crypko.ai/c/'
    
    #start_urls sets the urls of the download locations
    start_urls = []
    
    custom_settings = {
            'CONCURRENT_REQUESTS': 64,
            'CONCURRENT_REQUESTS_PER_DOMAIN': 64
    }
    
    for i in range(1,712044):
        start_urls.append(s_url + str(i))
        
    if not os.path.exists("img"):
        os.makedirs("img")
    
    file_name = ''
    progress = 0
    def parse(self, response):
        item = response.xpath('//meta[@property="og:image"]/@content').extract_first().split("_lg.jpg")[0] + "_sm.jpg"
        self.file_name = basename(item)
        r = scrapy.Request(item, self.parse_image)
        yield r
    
    def parse_image(self, response):
        # sets file name to img/<number>-<filename>
        with open("img/" + basename(str(response.request.headers.get('Referer', None))).split("'")[0] + "-" + basename(response.request.url), 'wb') as f:
            f.write(response.body)
