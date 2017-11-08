""" Main module with main() function to start test project """
import logging
from time import sleep
from FTestRunner import TestRunner
from FWTest_Rep_11_1_v2 import WTest_Rep_11_1_v2

logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)

def main():
    '''Main procedure to start all tests.'''
    tests_list = []
    # here we can add tests into common list
    tests_list.append(WTest_Rep_11_1_v2)
    test_runner = TestRunner(tests_list)
    #WTest_Rep_11_1, WTest_Rep_11_1_v2, WTest_Rep_01_1
    test_runner.init_test()

    #for i in range(1,10):
    test_runner.start()
    #    sleep(30)

    # print('=======================')
    # here we have saved property of tests tr.test_arr_objs()

main()
