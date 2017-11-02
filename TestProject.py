"""Base Class for all tests Classes. Implements common checks, time,size. """
from PageDownloader import PageDownload


class TestProject():
    ''' Basic class for test project. This is a parent class for WTestX classe. '''
    # pylint: disable=too-many-instance-attributes
    # It is reasonable in this case.
    download_time = float(0.0)
    download_size = float(0.0)
    page_content = None # str content of downloaded page
    test_time = None
    test_size = None
    cookie = None
    headers = None
    test_name = None
    url = None
    params = None
    tproperty = None


    #cookie, headers, test_name
    def __init__(self, p_test_time, p_cookie, p_headers,
                 p_test_name, p_url, p_params, p_tproperty):
        '''Class constructor '''
        # pylint: disable-msg=too-many-arguments
        self.test_time = p_test_time
        self.cookie = p_cookie
        self.headers = p_headers
        self.test_name = p_test_name
        self.url = p_url
        self.params = p_params
        self.tproperty = p_tproperty

    def check_time(self):
        '''Check download time for criterion.'''
        print("Page Download time is: ", str(self.download_time), " seconds. Criterion : ",
              str(self.test_time[0]), " - ", str(self.test_time[1]))
        if self.download_time >= self.test_time[0] and self.download_time <= self.test_time[1]:
            print("    SUCCESS")
        else:
            print("    FAIL")

    def check_size(self):
        '''Check download size for criterion.'''
        print("Page Download size is: ", str(self.download_size), " bytes. Criterion : ",
              str(self.test_size[0]), " - ", str(self.test_size[1]))
        if self.download_size >= self.test_size[0] and self.download_size <= self.test_size[1]:
            print("    SUCCESS")
        else:
            print("    FAIL")

    def check_property(self):
        '''Must be rewrited if necessary in child class. '''
        pass

    def start(self):
        '''Run this test '''
        print("                     ")
        print("[TestProject] self.test_name = ", self.test_name)
        tpage = PageDownload(self.test_name)

        tpage.set_cookie(self.cookie)
        tpage.set_header(self.headers)
        tpage.set_url(self.url)
        print('type self.params =', type(self.params))
        tpage.set_params(self.params)

        tpage.get_content(True)
        self.download_time = tpage.download_time
        self.download_size = tpage.download_size
        self.page_content = tpage.content
        #print("self.page_content=", type(self.page_content))
        self.check_time()
        self.check_size()
        if not self.tproperty is None:
            self.check_property()
