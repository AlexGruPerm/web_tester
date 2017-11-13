import logging
from TestProject import TestProject
import Params
from FXpathSeacher import XpathSearch
from decimal import Decimal

class WTest_Rep_oiv_info(TestProject):
    '''Class for user's 1 test '''
    test_config = Params.params_3

    tproperty_page = {
                      "row_count" : 0
                     } # empty dict with Fact property values

    def __init__(self):
        """ Class constructor """
        super(WTest_Rep_oiv_info,self).__init__(self.test_config)

    def check_property(self):
        """ This function is written special for test 11_1 and for addition checks """
        grid_search = XpathSearch(self.page_content)
        res = grid_search.search("//table/tbody/tr",False)
        res_cnt = len(res)
        self.tproperty_page["row_count"] = res_cnt
        logging.debug("[WTest_Rep_oiv_info] check_property row_count="+str(self.tproperty_page["row_count"]))
        for key, value in self.test_custom_property.items():
            logging.info("Expected ("+ str(key)+ ") - "+ str(value)+ " real "+ str(self.tproperty_page[key]))
            if value == self.tproperty_page[key]:
                logging.info('    SUCCESS')
            else:
                logging.info('    FAIL')