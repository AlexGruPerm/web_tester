from FTestRunner import TestRunner
from FWTest_Rep_01_1 import WTest_Rep_01_1
from FWTest_Rep_11_1 import WTest_Rep_11_1

def main():
    """ Main procedure to start all tests. """
    tr = TestRunner([WTest_Rep_11_1])#,WTest_Rep_01_1])
    tr.init_test()
    tr.start()

main()