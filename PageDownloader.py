""" File contains only one class PageDownload,
    that responsible for download html.  """

#import time
import sys
import io
import json
#import codecs
#from lxml import html
#from pprint import pprint
#from io import StringIO, BytesIO
#from lxml import etree
#import lxml.html
import datetime
#import xml.etree.ElementTree as ET
import requests

class PageDownload():
    '''
    Class just for download HTML content and return html as text.
    '''
    # pylint_: disable=too-many-instance-attributes
    # It is reasonable in this case.
    download_time = float(0.0)
    download_size = int(0)
    headers = None
    cookie = None
    url = None
    params = None

    def __init__(self, page_name):
        '''Class constructor, set some initial variables.'''
        #self.page_name = page_name # Internal name of class instance (human)
        self.file_name = page_name+'.html'#self.page_name+'.html'
        self.is_save_file = False  # Save content of html in local file self.file_name
        self.content = None

    def set_header(self, p_headers):
        '''Set class member with object type requests.cookies.RequestsCookieJar'''
        self.headers = p_headers

    def set_cookie(self, p_cookie):
        '''Set class member with object type requests.cookies.RequestsCookieJar'''
        self.cookie = p_cookie

    def set_url(self, p_url):
        """Set class member with object type requests.cookies.RequestsCookieJar"""
        self.url = p_url

    def set_params(self, p_params):
        """Set class member with object type requests.cookies.RequestsCookieJar"""
        self.params = p_params

    def get_content(self, is_save_file):#url,post_data,
        """Download html from url with send cookie (self.cookie) and post data."""
        t_begin = datetime.datetime.now()

        #print('url=', url)
        #print('cookies=', self.cookie)
        #print('headers=', self.headers)
        #print('post_data=',post_data)

        test_params = self.params
        try:
            dict_data = test_params['data']
            # < class 'dict'>
            # < class 'dict'>
            # Here we can make some manipulations with dict_data
            test_params.update({'data': json.dumps(dict_data,
                                                   sort_keys=False,
                                                   separators=(',', ': '))})
            # < class 'dict'>
            # < class 'str'>
        except KeyError:
            print("Not found key : 'data ")

        requests_res = requests.post(url=self.url,
                                     cookies=self.cookie,
                                     data=test_params,
                                     headers=self.headers)
        #print('self.headers=',type(self.headers))
        t_end = datetime.datetime.now()
        delta = t_end - t_begin
        self.download_time = delta.total_seconds()
        print('Now save to file', self.file_name)
        if is_save_file:
            with open(self.file_name, 'wb') as output_file:
                output_file.write(requests_res.text.encode('utf-8'))

        self.content = requests_res.text.encode('utf-8').decode('utf-8')
        self.download_size = sys.getsizeof(self.content)
        #print("Size of string representation of result is ", sys.getsizeof(self.content), " bytes")

    def read_content_file(self):
        '''Function read file with html and populate member self.content'''
        with io.open(self.file_name, encoding='utf-8', errors='ignore') as file:
            self.content = file.read()
        print("From file loaded ", sys.getsizeof(self.content), " bytes")
