from TestProject import TestProject
import Params

class WTest_Rep_01_1(TestProject):
    '''Class for user's 2 test '''
    cookie = Params.cookies_1
    headers = Params.headers_1
    url = Params.url_1
    test_name = Params.test_1_name
    test_time = Params.test_1_time
    test_size = Params.test_1_size
    params = Params.grid_param_1

    def __init__(self):
        """ Class constructor """
        super(WTest_Rep_01_1,self).__init__()


