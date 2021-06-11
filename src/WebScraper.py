from pymongo import MongoClient #MongoDB
import scrapy
from scrapy.crawler import CrawlerProcess
import pprint

###To do
#save raw html
#clean link following


#configure mongo
client = MongoClient('localhost',27017)
craigslist = client['craigslist']
listings = craigslist['all_listings']

class CraigslistScraper(scrapy.Spider):
    name = 'craigslist'
    start_urls = ['https://www.craigslist.org/about/sites']
    custom_settings = {
       "AUTOTHROTTLE_ENABLED" : True # so you dont get blocked as a bot
    }
    
    def parse(self,response):#scrapy main method
        city_links = []
        for i in range(1,5):
            city_links.extend(response.xpath("(//div[@class = 'box box_{}'])[1]/ul/li/a/@href".format(i)).extract())

        for l in city_links:
            yield response.follow(l,callback=self.to_forsale)

    def to_forsale(self,response):
        next_page_url = str(response.request.url)[:-1] + str(response.xpath("//a[@class = 'sss']/@href").extract()[0])
    
        if next_page_url is not None:
            yield response.follow(next_page_url,callback = self.listing)
 
    def listing(self,response):        
        for n in response.xpath("//a[@class = 'button next']/@href").extract():
            print(str(n))
            yield response.follow(n,callback = self.listing)
        for l in response.xpath("//li[@class = 'result-row']/a/@href").extract():
            print(str(l))
            yield response.follow(l, callback = self.parse_listing)
                    
    def parse_listing(self,response):
        city = response.xpath("//li[@class = 'crumb area']/p/a/text()").extract()[0]
        sub_cat = response.xpath("//li[@class = 'crumb category']/p/a/text()").extract()[0]
        post_id = response.xpath("//p[@class = 'postinginfo']/text()").extract()[0]
        post_time = response.xpath("(//time[@class = 'date timeago'])[1]/text()").extract()[0][0]
        post_upd = response.xpath("(//time[@class = 'date timeago'])[2]/text()").extract()[0][0]
        price = response.xpath("//span[@class = 'price']/text()").extract()[0]
        name = response.xpath("//span[@id = 'titletextonly']/text()").extract()
        des = response.xpath("//section[@id = 'postingbody']/text()").extract()
        attrs = response.xpath("//p[@class = 'attrgroup']/span/text()").extract()
        img_cnt = len(response.xpath("//a[@class = 'thumb']").extract())
            
        item = {
            'post_id':post_id,
            'city':city,
            'sub_cat':sub_cat,
            'price':price,
            'name':name,
            'des':des,
            'upload_date':post_time,
            'image_count':img_cnt,
            'attrs':attrs
        }
        #pprint.pprint(item)
        listings.insert_one(item)


#run it
if __name__ == '__main__':
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(CraigslistScraper)
    process.start()
    process.stop()