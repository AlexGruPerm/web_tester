import time
import sys
import requests
import io
import json
import codecs
from lxml import html
from pprint import pprint
from io import StringIO, BytesIO
from lxml import etree
import lxml.html
import datetime
import xml.etree.ElementTree as ET

class PageDownload():
   '''Class just for download HTML content and return html as text'''
   def __init__(self, page_name):
       '''Class constructor, set some initial variables.'''
       self.cookie = None
       self.page_name = page_name # Internal name of class instance (human)
       self.file_name = self.page_name+'.html'
       self.is_save_file = False  # Save content of html in local file self.file_name
       self.content = None

   def set_cookie(self, p_cookie):
        '''Set class member with object type requests.cookies.RequestsCookieJar'''
        self.cookie = p_cookie

   def get_content(self,url,post_data,is_save_file):
        '''Download html from url with send cookie (self.cookie) and post data. Save content into file file_name
           if parameter is not None'''
        t1 = datetime.datetime.now()
        #headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.8,ru;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "7668",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "PHPSESSID=30a37d8f7897bfd9b0c80536cbcc15b0; session_prm_salary=b566fb7790cb6c57e02646302191c478; _ym_uid=1509037403214612514; _ym_isad=2",
            "Host": "mkrpk.ders.proitr.ru",
            "Origin": "http://mkrpk.ders.proitr.ru",
            "Pragma": "no-cache",
            "Referer": "http://mkrpk.ders.proitr.ru/salary/index.php?show=rep_11_1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        r = requests.post(url, cookies=self.cookie, data=post_data, headers=headers)
        t2 = datetime.datetime.now()
        delta = t2 - t1

        print('Now save to file',self.file_name)
        if is_save_file:
            with open(self.file_name, 'wb') as output_file:
                output_file.write(r.text.encode('utf-8'))

        self.content = r.text.encode('utf-8').decode('utf-8')

        print("Size of string representation of result is ", sys.getsizeof(self.content), " bytes")
        print("Duration of load first page is ", str(delta.total_seconds()), " seconds")

   def read_content_file(self):
        '''Function read file with html and populate member self.content'''
        with io.open(self.file_name, encoding='utf-8', errors='ignore') as file:
            self.content=file.read()
        print("From file loaded ", sys.getsizeof(self.content), " bytes")
