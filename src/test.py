import numpy as np
import pandas as pd
import pyspark as ps            #Spark
import psycopg2 as pg2          #Postgres
from pymongo import MongoClient #MongoDB
import matplotlib.pyplot as plt

import scrapy
import pprint


from scrapy.crawler import CrawlerProcess

#configure mongo
client = MongoClient('localhost',27017)
craigslist = client['craigslist']
listings = craigslist['all_listings']

class CraigslistScraper(scrapy.Spider):
    name = 'craigslist'
    
    start_urls = ['https://www.craigslist.org/about/sites']
    
    custom_settings = {
       "AUTOTHROTTLE_ENABLED" : True
    }
    
    def parse(self,response):#parsing the start_url
        city_links = []
        for i in range(1,5):
            #states.extend(response.xpath("(//div[@class = 'box box_{}'])[1]/h4/text()".format(i)).extract())
            city_links.extend(response.xpath("(//div[@class = 'box box_{}'])[1]/ul/li/a/@href".format(i)).extract())

        #for l in city_links:
        l = city_links[0]
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
        #print('working ' + str(response.request.url))
        #city
        city = response.xpath("//li[@class = 'crumb area']/p/a/text()").extract()[0]
        #print('city: ' + str(city))
        #sub categorey
        sub_cat = response.xpath("//li[@class = 'crumb category']/p/a/text()").extract()[0]
        #print('category: ' + str(sub_cat))
        #post id
        post_id = response.xpath("//p[@class = 'postinginfo']/text()").extract()[0]
        #print('id: ' + str(post_id))
        #adjust these dates
        #post time
        post_time = response.xpath("(//time[@class = 'date timeago'])[1]/text()").extract()[0][0]
        #print('post_time: ' + str(post_time))
        #last updated
        post_upd = response.xpath("(//time[@class = 'date timeago'])[2]/text()").extract()[0][0]
        #print('post_upd: ' + str(post_upd))
        #price
        price = response.xpath("//span[@class = 'price']/text()").extract()[0]
        #print('price: ' + str(price))
        #name
        name = response.xpath("//span[@id = 'titletextonly']/text()").extract()
        #print('name: ' + str(name))
        #description
        des = response.xpath("//section[@id = 'postingbody']/text()").extract()
        #print('description: ' + str(des))
        #attributes
        attrs = response.xpath("//p[@class = 'attrgroup']/span/text()").extract()
            #check if they exist
        #images
            #see if thumbnails works
        img_cnt = response.xpath("//a[@class = 'thumb']").extract().count()
            
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
        print(item)
        #listings.insert_one(item)



process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(CraigslistScraper)
process.start()
#process.stop()

listings.estimated_document_count()
