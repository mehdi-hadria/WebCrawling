import scrapy

class siteSpider(scrapy.Spider):
    number_page = 1
    name = "MeHspider"
    """def __init__(self,*args, **kwargs):
        super(siteSpider,self).__init__(*args,**kwargs)
        self.start_urls = kwargs.pop('start_urls').split(';')
    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse)"""
    def __init__(self,filename=None):
        if filename:
            with open(filename,'r') as f:
                self.start_urls= [l.strip() for l in f.readlines()]

    def parse(self,response):
        filename = 'content_%s.html' % str(self.number_page)
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log('Save file %s' % filename)
        self.number_page = self.number_page +1