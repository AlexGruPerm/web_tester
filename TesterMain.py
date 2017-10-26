from PageDownloader import PageDownload
from FXpathSeacher import XpathSearch
import requests
import Params

#AlexGruPerm github
#https://github.com/AlexGruPerm/web_tester
#https://github.com/AlexGruPerm/web_tester.git

jar = requests.cookies.RequestsCookieJar()
jar.set('PHPSESSID',          '30a37d8f7897bfd9b0c80536cbcc15b0', domain='mkrpk.ders.proitr.ru', path='/')
jar.set('session_prm_salary', 'b566fb7790cb6c57e02646302191c478', domain='mkrpk.ders.proitr.ru', path='/')

'''
# Object for main report page
main_page = PageDownload('Report_1_MainPage')
main_page.set_cookie(jar)
url = 'http://mkrpk.ders.proitr.ru/salary/index.php?show=rep_11_1'
 #main_page.get_content(url,None,True)
main_page.read_content_file()
mpage_search = XpathSearch(main_page.content)
mpage_search.search("/html/body/div[@id='h-content']/div[contains(@class,'title')]/h1")
'''

# Object for grid content
report_grid = PageDownload('Report_1_Grid')
report_grid.set_cookie(jar)
url = 'http://mkrpk.ders.proitr.ru/salary/index.php'
 #report_grid.get_content(url,Params.grid_param_1,True)
report_grid.read_content_file()

grid_search = XpathSearch(report_grid.content)
grid_search.search("//*")

