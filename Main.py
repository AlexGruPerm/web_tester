from FTestRunner import TestRunner
from FWTest_Rep_01_1 import WTest_Rep_01_1
from FWTest_Rep_11_1 import WTest_Rep_11_1
from FWTest_Rep_11_1_v2 import WTest_Rep_11_1_v2

def main():
    """ Main procedure to start all tests. """
    tr = TestRunner([WTest_Rep_11_1,
                     WTest_Rep_11_1_v2,
                     WTest_Rep_01_1])
    tr.init_test()
    tr.start()
    # print('=======================')
    # here we have saved property of tests tr.test_arr_objs()

main()