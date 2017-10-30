from TestProject import TestProject
import Params

class WTest_Rep_01_1(TestProject):
    '''Class for user's 2 test '''
    cookie = Params.cookies_2
    headers = Params.headers_2
    url_main = Params.url_main_2
    url_report = Params.url_report_2
    test_name = Params.test_2_name

    def __init__(self):
        """ Class construtcot """
        super(WTest_Rep_01_1,self).__init__(self.cookie,self.headers,self.test_name)


