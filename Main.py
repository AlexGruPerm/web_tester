from FWTest_Rep_11_1 import WTest_Rep_11_1
from FWTest_Rep_01_1 import WTest_Rep_01_1

def main():
    """ Main procedure to start all tests. """

arr_test_names = [WTest_Rep_11_1,
                  WTest_Rep_01_1] #list of defined tests for executing, each test is a class.

print('Tests begins.............................')
print('                                         ')
arr_test_objs = []
for i in range(len(arr_test_names)):
    arr_test_objs.append(arr_test_names[i]()) #create instance of class and append it into list
    arr_test_objs[i].start() # for each instance is running start method that defined in parent class TestProject
    print(' ------------------------------------------------- ')
print('                                         ')
print('Tests ends...............................')

main()