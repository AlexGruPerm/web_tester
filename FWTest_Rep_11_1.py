from TestProject import TestProject
import Params

class WTest_Rep_11_1(TestProject):
    '''Class for user's 1 test '''
    cookie = Params.cookies_1
    headers = Params.headers_1
    url_main = Params.url_main_1
    url_report = Params.url_report_1
    test_name = Params.test_1_name

    def __init__(self):
        """ Class construtcot """
        super(WTest_Rep_11_1,self).__init__(self.cookie,self.headers,self.test_name)


