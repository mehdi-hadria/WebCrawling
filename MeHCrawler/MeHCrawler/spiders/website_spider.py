import scrapy

class siteSpider(scrapy.Spider):
    name = "MeHspider"
    def start_requests(self):
        urls = ['https://www.ekimetrics.com']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        i = 0
        filename = 'content_.html'
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log('Save file %s' % filename)