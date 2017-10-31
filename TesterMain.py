from PageDownloader import PageDownload
from FXpathSeacher import XpathSearch
import requests
import Params
import json
import pprint
from decimal import Decimal

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
#report_grid.get_content(url,Params.grid_param_1,True)
report_grid.read_content_file()


grid_search = XpathSearch(report_grid.content)
print(type(grid_search))
r = grid_search.search("//table/tbody/tr",False)
r_cnt = len(r)-1
#print("tr count = ",r_cnt)
matrix = []#[[0 for i in range(1)] for j in range(1)] # column with [0] count = count of <tr>

# ТЕСТ это сумма первого столбца.


# ищем таблицу и считаем в ней количество строк и колонок и среди них пустые !!!
print(type(r))
table_tr_count = 0
for trs in r[1:len(r)]:
 table_tr_count += 1
 #grid_search.print_html_elm(trs)
 #print('----------------------------------')
 table_line = []
 for t in trs:
     #grid_search.print_html_elm(t)
     #print(str(ths.text))
     if t.tag=='td':
         table_line.append(str(t.text))
 #print(table_line)
 matrix.append(table_line)
 #print("Table contains : ",str(table_tr_count)," rows.")


test_col_num = 0 # first column in report
test_col_sum = Decimal(0.0)

for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                if i==0:  # calculate fields in first row
                    test_col_num += 1
                if j==0:  # calculate sum of cells in one column
                    try:
                        test_col_sum = test_col_sum + Decimal(matrix[i][j].strip().replace(',', '.').replace(u'\xa0',''))
                    except ValueError:
                        print("      error on line [",i,"]",end=" ")

print("OK 1. len_matric=",len(matrix))
print("OK 2. test_col_sum=",str(test_col_sum))
print("OK 3. test_col_num=",str(test_col_num))


'''
print(type(Params.grid_param_3))
udata = json.dumps(Params.grid_param_3, sort_keys=False,indent=4, separators=(',', ': '))
print(type(udata))

if 'data' in udata:
    print('Exists search Data!')
else:
    print('No search Data!')
'''
