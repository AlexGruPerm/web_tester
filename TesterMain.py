from PageDownloader import PageDownload
from FXpathSeacher import XpathSearch
import requests
import Params

#AlexGruPerm github
#https://github.com/AlexGruPerm/web_tester.git

jar = requests.cookies.RequestsCookieJar()
jar.set('PHPSESSID',          '328fe257868ed419e48d8aaf44f1e085', domain='mkrpk.ders.proitr.ru', path='/')
jar.set('session_prm_salary', 'd7946be1334a613d86c97ca7deda7e5d', domain='mkrpk.ders.proitr.ru', path='/')
jar.set('__DebugUkaz',        '0',                                domain='mkrpk.ders.proitr.ru', path='/salary')

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
#report_grid.get_content(url,Params.grid_param_3,True)
report_grid.read_content_file()

grid_search = XpathSearch(report_grid.content)
grid_search.search("//*")
#Comments for test git from PyCharm into github _

