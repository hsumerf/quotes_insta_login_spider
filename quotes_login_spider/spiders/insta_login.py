# -*- coding: utf-8 -*-
import atexit
import datetime
import itertools
import json
import logging
import random
import signal
import sys
import sqlite3
import time
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
       # csrf_token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        BASE_URL = 'http://www.instagram.com'
        url_login = BASE_URL + '/accounts/login/'
        user_login = 'h.s.umer.farooq@gmail.com'
        user_password = 'password'
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        # session = requests.Session()
        # session.headers = {'user-agent':USER_AGENT}
        # session.headers.update({'Referer':BASE_URL})
        # req = session.get(BASE_URL)

        # session.headers.update({'csrftoken':req.cookies['csrftoken']})
        # login_data = {'username':USER_NAME,'password':PASSWD,'csrftoken':req.cookies['csrftoken']}
        # login = session.post(LOGIN_URL,data=login_data,allow_redirects = True)
        # session.headers.update({'csrftoken':login.cookies['csrftoken']})
        #
        # cookies = login.cookies
        #
        # print(login)
        # print(login.url)
        # print(login.text)


        log_string = 'Trying to login as %s...\n' % (user_login)
        #self.write_log(log_string)
        login_post = {
            'username': user_login,
            'password': user_password
        }
        s = requests.Session()
        s.headers.update({
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Host': 'www.instagram.com',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/',
            'User-Agent': user_agent,
            'X-Instagram-AJAX': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest'
        })
        s = requests.Session()
        r = s.get(response.url)
        s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
        time.sleep(5 * random.random())
        login = s.post(
            url_login, data=login_post, allow_redirects=True)
        s.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
        csrftoken = login.cookies['csrftoken']
        # ig_vw=1536; ig_pr=1.25; ig_vh=772;  ig_or=landscape-primary;
        s.cookies['ig_vw'] = '1536'
        s.cookies['ig_pr'] = '1.25'
        s.cookies['ig_vh'] = '772'
        s.cookies['ig_or'] = 'landscape-primary'
        time.sleep(5 * random.random())

        if login.status_code == 200:
            r = s.get('https://www.instagram.com/')
            finder = r.text.find(user_login)
            print(finder)
            print(r.url)
            print(r.text)
            open_in_browser(response)

        #     if finder != -1:
        #         ui = UserInfo()
        #         user_id = ui.get_user_id_by_login(user_login)
        #         login_status = True
        #         log_string = '%s login success!' % (user_login)
        #         write_log(log_string)
        #     else:
        #         login_status = False
        #         write_log('Login error! Check your login data!')
        # else:
        #     write_log('Login error! Connection error!')

        # login.status_code
        # login.content
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

