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
    #headers = None
    #cookie = None
    #url = None
    #params = None
    test_proj_instance = None

    def __init__(self, test_proj):
        '''Class constructor, set some initial variables.'''
        #self.page_name = page_name # Internal name of class instance (human)
        self.test_proj_instance = test_proj #instance of class TestProject
        self.file_name = self.test_proj_instance.test_name+'.html'#self.page_name+'.html'
        self.is_save_file = False  # Save content of html in local file self.file_name
        self.content = None


    def get_content(self, is_save_file):#url,post_data,
        """Download html from url with send cookie (self.cookie) and post data."""
        t_begin = datetime.datetime.now()

        #print('url=', url)
        #print('cookies=', self.cookie)
        #print('headers=', self.headers)
        #print('post_data=',post_data)

        #test_params = self.params
        #try:
            #dict_data = test_params['data']
            # < class 'dict'>
            # < class 'dict'>
            # Here we can make some manipulations with dict_data
            #test_params.update({'data': json.dumps(dict_data,
            #                                       sort_keys=False,
            #                                       separators=(',', ': '))})
            # < class 'dict'>
            # < class 'str'>
        #except KeyError:
        #    print("Not found key : 'data ")
        logging.debug('type self.cookie'+(str(type(self.test_proj_instance.cookie))))
        logging.debug('self.test_proj_instance.cookie=' + (str(self.test_proj_instance.cookie)))

        #print(self.test_proj_instance.params)
        # test_params.update({'data': json.dumps(dict_data,
        #                                       sort_keys=False,
        #                                       separators=(',', ': '))})



        requests_res = requests.post(url=self.test_proj_instance.url,
                                     cookies=self.test_proj_instance.cookie,
                                     data=self.test_proj_instance.params,
                                     headers=self.test_proj_instance.headers)

        t_end = datetime.datetime.now()
        delta = t_end - t_begin
        self.download_time = delta.total_seconds()
        logging.debug('Now save to file '+ self.file_name)
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
        logging.debug("From file loaded "+ str(sys.getsizeof(self.content))+ " bytes")
