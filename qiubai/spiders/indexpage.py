import scrapy

from qiubai.items import QiubaiItem

class QiuBaiSpider(scrapy.Spider):
    name = "qiubai"
    start_urls=[
        "http://www.qiushibaike.com/",
    ]


    def parse(self, response):
       #jin ru ce shi
       #from scrapy.shell import inspect_response
       #inspect_response(response, self)
 
       #print response.xpath('//div[@class="content"]').extract()

       #print response.xpath('//divi@class="article block untagged mb15"]').extract()


      for ele in response.xpath('//div[@class="article block untagged mb15"]'):
          authors = ele.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract()
          contents = ele.xpath('./div[@class="content"]/span/text()').extract()
          yield QiubaiItem(author=authors, content=contents)
                 
