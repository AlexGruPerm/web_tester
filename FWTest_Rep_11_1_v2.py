from TestProject import TestProject
import Params
from FXpathSeacher import XpathSearch
from decimal import Decimal

class WTest_Rep_11_1_v2(TestProject):
    '''Class for user's 1 test '''
    cookie = Params.cookies_3
    headers = Params.headers_2
    url = Params.url_2
    test_name = Params.test_3_name
    test_time = Params.test_3_time
    test_size = Params.test_3_size

    params = Params.grid_param_3

    tproperty = Params.test_3_property # dict of check property value
    tproperty_page = {
                      "row_count" : 0,
                      "col_sum"   : 0,
                      "col_count" : 0
                     } # empty dict with Fact property values

    def __init__(self):
        """ Class constructor """
        super(WTest_Rep_11_1_v2,self).__init__(self.test_time,self.cookie, self.headers,
                                               self.test_name, self.url, self.params,
                                               self.tproperty)

    def check_property(self):
        """ This function is written special for test 11_1 and for addition checks """
        grid_search = XpathSearch(self.page_content)
        res = grid_search.search("//table/tbody/tr",False)
        res_cnt = len(res)-1
        self.tproperty_page["row_count"] = res_cnt

        matrix = []
        for trs in res[1:len(res)]:
            table_line = []
            for t in trs:
                if t.tag=='td':
                    table_line.append(str(t.text))
            matrix.append(table_line)

        test_col_num = 0 # first column in report
        test_col_sum = Decimal(0.0)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0:  # calculate fields in first row
                    test_col_num += 1
                if j == 0:  # calculate sum of cells in one column
                    try:
                        test_col_sum = test_col_sum + Decimal(
                            matrix[i][j].strip().replace(',', '.').replace(u'\xa0', ''))
                    except ValueError:
                        print("      error on line [", i, "]", end=" ")

        self.tproperty_page["col_sum"] = float(test_col_sum)
        self.tproperty_page["col_count"] = test_col_num

        for key, value in self.tproperty.items():
            print("Expected (", key, ") - ", value, " real ", self.tproperty_page[key])
            if value == self.tproperty_page[key]:
                print("    SUCCESS")
            else:
                print("    FAIL")