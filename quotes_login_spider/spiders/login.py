# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
#from scrapy.utils.response import open_in_brower
class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        #extracting csrf_token
        csrf_token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        yield FormRequest('http://quotes.toscrape.com/login',
                          formdata = {'csrf_token':csrf_token,
                                      'username':'umer',
                                      'password':'123'},
                          callback = self.parse_after_login)

    def parse_after_login(self,response):
        if response.xpath('//a[text()="Logout"]'):


            print('You loggin in!')

