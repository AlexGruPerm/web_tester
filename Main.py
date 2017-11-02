""" Main module with main() function to start test project """
from FTestRunner import TestRunner
from FWTest_Rep_01_1 import WTest_Rep_01_1
from FWTest_Rep_11_1 import WTest_Rep_11_1
from FWTest_Rep_11_1_v2 import WTest_Rep_11_1_v2

def main():
    '''Main procedure to start all tests.'''
    test_runner = TestRunner([WTest_Rep_11_1, WTest_Rep_11_1_v2, WTest_Rep_01_1])
    test_runner.init_test()
    test_runner.start()
    # print('=======================')
    # here we have saved property of tests tr.test_arr_objs()

main()
