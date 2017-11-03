""" Main module with main() function to start test project """
import logging
from FTestRunner import TestRunner
from FWTest_Rep_11_1_v2 import WTest_Rep_11_1_v2

logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.INFO)

def main():
    '''Main procedure to start all tests.'''
    test_runner = TestRunner([WTest_Rep_11_1_v2])
    #WTest_Rep_11_1, WTest_Rep_11_1_v2, WTest_Rep_01_1
    test_runner.init_test()
    test_runner.start()
    # print('=======================')
    # here we have saved property of tests tr.test_arr_objs()

main()
