from PageDownloader import PageDownload

class TestProject():
    """ Basic class for test project. This is a parent class for WTestX classe. """
    download_time = float(0.0)
    download_size = float(0.0)
    page_content  = None # str content of downloaded page

    #cookie, headers, test_name
    def __init__(self):#,cookie,headers,test_name,url,params):
        """ Class constructor """

    def check_time(self):
        """ Check download time for criterion. """
        print("Page Download time is: ", str(self.download_time), " seconds. Criterion : ",
              str(self.test_time[0]), " - ", str(self.test_time[1]))
        if (self.download_time >= self.test_time[0] and self.download_time <= self.test_time[1]):
            print("    SUCCESS")
        else:
            print("    FAIL")

    def check_size(self):
        """ Check download size for criterion. """
        print("Page Download size is: ", str(self.download_size), " bytes. Criterion : ",
              str(self.test_size[0]), " - ", str(self.test_size[1]))
        if (self.download_size >= self.test_size[0] and self.download_size <= self.test_size[1]):
            print("    SUCCESS")
        else:
            print("    FAIL")


    def start(self):
        """ Run this test """
        print("                     ")
        print("[TestProject] self.test_name = ",self.test_name)
        tpage = PageDownload(self.test_name)

        tpage.set_cookie(self.cookie)
        tpage.set_header(self.headers)
        tpage.set_url(self.url)
        tpage.set_params(self.params)

        tpage.get_content(True)
        self.download_time = tpage.download_time
        self.download_size = tpage.download_size
        self.page_content = tpage.content
        #print("self.page_content=",type(self.page_content))
        self.check_time()
        self.check_size()
        if not(self.tproperty is None):
           self.check_property()