""" File contains only one class PageDownload,
    that responsible for download html.  """

#import time
import logging
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
    # pylint: disable=too-many-instance-attributes
    # It is reasonable in this case.
    download_time = float(0.0)
    download_size = int(0)
    file_name = None
    content = None
    url = None
    cookie = None
    params = None
    headers = None

    def __init__(self, test_name, url, cookie, params, headers):
        '''Class constructor, set some initial variables.'''
        self.file_name = test_name+'.html'
        self.url = url
        self.cookie = cookie
        self.params = params
        self.headers = headers


    def get_content(self, is_save_file):#url,post_data,
        """Download html from url with send cookie (self.cookie) and post data."""
        t_begin = datetime.datetime.now()
        #logging.debug('type self.cookie'+(str(type(self.cookie))))
        #logging.debug('self.test_proj_instance.cookie=' + (str(self.test_proj_instance.cookie)))
        requests_res = requests.post(url = self.url,
                                     cookies = self.cookie,
                                     data = self.params,
                                     headers = self.headers)
        t_end = datetime.datetime.now()
        delta = t_end - t_begin
        self.download_time = delta.total_seconds()
        logging.debug('Now save to file '+ self.file_name)
        if is_save_file:
            with open(self.file_name, 'wb') as output_file:
                output_file.write(requests_res.text.encode('utf-8'))
        self.content = requests_res.text.encode('utf-8').decode('utf-8')
        self.download_size = sys.getsizeof(self.content)


    def read_content_file(self):
        '''Function read file with html and populate member self.content'''
        with io.open(self.file_name, encoding='utf-8', errors='ignore') as file:
            self.content = file.read()
        logging.debug("From file loaded "+ str(sys.getsizeof(self.content))+ " bytes")
