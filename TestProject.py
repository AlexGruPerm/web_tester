"""Base Class for all tests Classes. Implements common checks, time,size. """
import logging
import io
import json
import datetime
import requests
from PageDownloader import PageDownload
import Params



class TestProject():
    ''' Basic class for test project. This is a parent class for WTestX classe. '''
    # pylint: disable=too-many-instance-attributes
    # It is reasonable in this case.
    download_time = float(0.0)
    download_time_test_res = None
    download_size = float(0.0)
    download_size_test_res = None
    page_content = None # str content of downloaded page
    test_time = None
    test_size = None
    cookie = None
    headers = None
    test_name = None
    url = None
    params = None
    tproperty = None
    test_custom_property = None
    # this object contains all tests results
    # common object for all tests.
    this_test_dict = []
    results_text_file = None
    current_datetime = None

    def read_tests_history(self):
        '''Read content oh tests history from file.'''
        logging.debug(" read results file: "+self.results_text_file)
        with io.open(self.results_text_file, encoding='utf-8', errors='ignore') as file:
            data = json.load(file)
        self.this_test_dict = data




    #cookie, headers, test_name
    def __init__(self, test_config):
        '''Class constructor '''
        # pylint: disable-msg=too-many-arguments
        try:
            logging.debug('Begin parse params')
            # Check that all necessary keys exists in dict
            try:
                check_keys = ('name', 'url', 'headers', 'cookies', 'post_data',
                              'test_suc_time', 'test_suc_size')
                for c_key in check_keys:
                    if not c_key in test_config:
                        raise KeyError('Key ' + c_key + ' not found in test config params.')
                    elif not test_config.get(c_key):
                        raise ValueError('Value for Key ' + c_key + ' is empty or None.')
            except KeyError as err_key_obj:
                logging.critical(err_key_obj.args)
                raise KeyError(err_key_obj.args)
                # here return or exit from execution
            except ValueError as err_val_obj:
                logging.critical(err_val_obj.args)
                raise ValueError(err_val_obj.args)
                # here return or exit from execution
            else:
                logging.debug('All keys found in test config params.')
                self.test_name = test_config['name']
                self.url = test_config['url']
                self.headers = test_config['headers']
                self.cookie = requests.cookies.RequestsCookieJar()
                self.results_text_file = Params.results_text_file_1
                for cook_key in test_config['cookies']:
                    self.cookie.set(cook_key,
                                    test_config['cookies'].get(cook_key).get('value'),
                                    domain=test_config['cookies'].get(cook_key).get('domain'),
                                    path=test_config['cookies'].get(cook_key).get('path'))

                #PREV: self.params =  test_config['post_data'] #json.dumps(test_config['post_data'])
                # First we need populate self.params and next update subtag
                self.params = test_config['post_data']
                self.params.update({'data': json.dumps(test_config['post_data']['data'],
                                                       sort_keys=False, separators=(',', ': '))})
                self.test_time = test_config['test_suc_time']
                logging.debug('self.test_time MIN=' + str(self.test_time['min']))
                logging.debug('self.test_time MAX=' + str(self.test_time['max']))
                self.test_size = test_config['test_suc_size']
                self.test_custom_property = test_config['test_suc_custom_property']
                logging.debug('All values in params checked for not None,Null')
                logging.debug('Test name (' + self.test_name + ') url (' + self.url + ')')
                logging.debug("TestProject __init__ test_name="+self.test_name)
                logging.debug("TestProject __init__ url="+self.url)
        except Exception as err_obj:
            logging.critical('External exception handler: ' + str(err_obj.args))


    def check_time(self):
        '''Check download time for criterion.'''
        #print("Page Download time is: ", str(self.download_time), " seconds. Criterion : ",
        #      str(self.test_time['min']), " - ", str(self.test_time['max']))
        logging.info("Page Download time is: "+ str(self.download_time)+ " seconds. Criterion : "+
                     str(self.test_time['min'])+ " - "+ str(self.test_time['max']))
        if self.download_time >= self.test_time['min'] and \
           self.download_time <= self.test_time['max']:
            self.download_time_test_res = 'SUCCESS'
        else:
            self.download_time_test_res = 'FAIL'
        logging.info('    '+self.download_time_test_res)


    def check_size(self):
        '''Check download size for criterion.'''
        logging.info("Page Download size is: "+ str(self.download_size)+ " bytes. Criterion : "+
                     str(self.test_size['min'])+ " - "+ str(self.test_size['max']))
        if self.download_size >= self.test_size['min'] and \
           self.download_size <= self.test_size['max']:
            self.download_size_test_res = 'SUCCESS'
        else:
            self.download_size_test_res = 'FAIL'
        logging.info('    ' + self.download_size_test_res)


    def check_property(self):
        '''Must be rewrited if necessary in child class. '''
        pass


    def populate_tmp_dict_with_test_res(self):
        '''Populate temporary dict with test results.'''
        this_test_res_dict = {}
        this_test_res_dict['run_datetime'] = self.current_datetime
        this_test_res_dict['download_time'] = self.download_time
        this_test_res_dict['res_download_time'] = self.download_time_test_res
        this_test_res_dict['download_size'] = self.download_size
        this_test_res_dict['res_download_size'] = self.download_size_test_res
        return this_test_res_dict


    def save_results_in_text_file(self):
        '''Append new test results into text file'''
        self.read_tests_history()
        logging.debug("BEGIN SAVE RESULTS INTO : "+self.results_text_file)
        for test_block in self.this_test_dict['history']:
            if self.test_name in test_block['name']:
                logging.debug("Block "+self.test_name+" found in results file")
                this_test_dict = test_block['hist']
                this_test_res_dict = self.populate_tmp_dict_with_test_res()
                this_test_dict.append(this_test_res_dict)
                break
        else:
            logging.debug("Block "+ self.test_name+ " not found in results file")
            this_test_res_dict = self.populate_tmp_dict_with_test_res()
            self.this_test_dict['history'].append({"name": self.test_name, "hist": [this_test_res_dict]})
        with open('test_result.txt', 'wb') as output_file:
            output_file.write(json.dumps(self.this_test_dict,
                                         sort_keys=False, indent=4).encode('utf-8'))
        logging.debug("END SAVE RESULTS ")


    def start(self):
        '''Run this test '''
        logging.debug("[TestProject] self.test_name = " + self.test_name)
        self.current_datetime = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
        tpage = PageDownload(self) #inside PageDownload constructor we send TestProject instance.
        tpage.get_content(True)
        self.download_time = tpage.download_time
        self.download_size = tpage.download_size
        self.page_content = tpage.content
        self.check_time()
        self.check_size()
        if not self.test_custom_property is None:
            self.check_property()
        self.save_results_in_text_file()
