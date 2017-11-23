""" Main module with main() function to start test project """
import logging
from time import sleep
from FTestRunner import TestRunner
from FWTest_Rep_11_1_v2 import WTest_Rep_11_1_v2
from FWTest_Rep_11_1_v3 import WTest_Rep_11_1_v3
from FWTest_Rep_oiv_info import WTest_Rep_oiv_info

logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)

def main():
    '''Main procedure to start all tests.'''
    tests_list = []
    # here we can add tests into common list

    #tests_list.append(WTest_Rep_11_1_v2)
    #tests_list.append(WTest_Rep_11_1_v3)
    tests_list.append(WTest_Rep_oiv_info)

    test_runner = TestRunner(tests_list)
    test_runner.init_test()

    #for i in range(1,2400):
    test_runner.start()
    #    sleep(30)

main()
