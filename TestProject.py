from PageDownloader import PageDownload

class TestProject():
    """ Basic class for test project. This is a parent class for WTestX classe. """
    cookie = None
    headers = None
    test_name = None
    url       = None

    #cookie, headers, test_name
    def __init__(self,cookie,headers,test_name,url):
        """ Class construtcot """
        #print('(', self.__class__, ')')
        #print('Call __init__ of TestProject')
        self.cookie  = cookie
        self.headers = headers
        self.test_name = test_name # human test name
        self.url = url

    def start(self):
        """ Run this test """
        print("                     ")
        print("run... this test.........    [TestProject] self.test_name = ",self.test_name)
        tpage = PageDownload('self.test_name')
        tpage.set_cookie(self.cookie)
        tpage.get_content(self.url,None,True)
