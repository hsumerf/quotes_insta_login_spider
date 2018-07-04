# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class InstaLoginSpider(scrapy.Spider):
    name = 'insta_login'
    allowed_domains = ['instagram.com']
    start_urls = ['https://www.instagram.com/accounts/login/']

    def parse(self, response):
        print(response.url)
        csrf_token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        # yield FormRequest('http://quotes.toscrape.com/login',
        #                   formdata={'csrf_token': csrf_token,
        #                             'username': 'h.s.umer.farooq@gmail.com',
        #                             'password': 'umer+-789'},
        #                   callback=self.parse_after_login)

        def parse_after_login(self, response):
            pass

            # print("You logged in")
            # if response.xpath('//a[text()="Logout"]'):
            #     self.log('You logged in!')
            #
            #open_in_browser(response)

