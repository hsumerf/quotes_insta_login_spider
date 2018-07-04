# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
import requests
import json
import getpass

class InstaLoginSpider(scrapy.Spider):
    name = 'insta_login'
    allowed_domains = ['instagram.com']
    start_urls = ['https://www.instagram.com/accounts/login/']

    def parse(self, response):
        print(response.url)
        csrf_token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        BASE_URL = 'http://www.instagram.com'
        LOGIN_URL = BASE_URL + '/accounts/login/'
        USER_NAME = 'h.s.umer.farooq@gmail.com'
        PASSWD = 'umer+-789'
        USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        session = requests.Session()
        session.headers = {'user-agent':USER_AGENT}
        session.headers.update({'Referer':BASE_URL})
        req = session.get(BASE_URL)

        session.headers.update({'X-CSRFToken':req.cookies['csrftoken']})
        login_data = {'username':USER_NAME,'password':PASSWD}
        login = session.post(LOGIN_URL,data=login_data,allow_redirects = True)
        session.headers.update({'X-CSRFToken':login.cookies['csrftoken']})

        cookies = login.cookies
        print(cookies)


        print(login)
        print(login.url)
        # login_text = json.loads(login.text)
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

