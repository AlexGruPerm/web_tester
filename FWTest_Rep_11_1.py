from TestProject import TestProject
import Params

class WTest_Rep_11_1(TestProject):
    '''Class for user's 1 test '''
    cookie = Params.cookies_2
    headers = Params.headers_2
    url = Params.url_2
    test_name = Params.test_2_name
    test_time = Params.test_2_time
    test_size = Params.test_2_size
    params = Params.grid_param_2

    tproperty = Params.test_2_property

    def __init__(self):
        """ Class constructor """
        super(WTest_Rep_11_1,self).__init__()


