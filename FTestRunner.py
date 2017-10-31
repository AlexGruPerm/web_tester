
class TestRunner():
    """ Class for runs individual test from input list"""
    arr_test_objs = []   # list of test objects
    arr_test_names = []  # list of test class names

    def __init__(self,tests_list):
        """ init property arr_test_names with input classes (no class names) """
        print('Tests begins.')
        self.arr_test_names = tests_list # list

    def init_test(self):
        """ Go through test class names and create instances of this Classes. Populate list of objects. """
        for i in range(len(self.arr_test_names)):
            self.arr_test_objs.append(self.arr_test_names[i]())  # create instance of class and append it into list

    def start(self):
        """ Go through list of test objects and start each of them. """
        for i in range(len(self.arr_test_objs)):
            self.arr_test_objs[i].start()  # for each instance is running start method that defined in parent class TestProject
        print('Tests ends.')

    def test_arr_objs(self):
        """ make some test about array of objects"""
        for i in range(len(self.arr_test_objs)):
            print(self.arr_test_objs[i].test_name," was loaded ",self.arr_test_objs[i].download_time," seconds.")