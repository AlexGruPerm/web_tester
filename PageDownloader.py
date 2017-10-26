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
        r = requests.post(url, cookies=self.cookie, data=post_data)
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
