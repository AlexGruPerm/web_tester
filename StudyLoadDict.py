import io
import json

#dict_test_results = {}
#results_text_file = None

with io.open('test_result.txt', encoding='utf-8', errors='ignore') as file:
    data = json.load(file)

this_test_dict = [] # history of this test by name as list
print(type(this_test_dict))
print(type(data['history']))
print(type(data['history'][0]))

rep_name = "Report 11_1 v000 Report page"

for test_block in data['history']:
    print('test_block name =',test_block['name'])
    if rep_name in test_block['name']:
        print('FOUND')

        this_test_dict = test_block['hist']
        print(type(this_test_dict))
        print(this_test_dict)
        #------------------------
        this_test_res_dict = {}
        this_test_res_dict['run_datetime'] = '01.01.2017 12:38:44'
        this_test_res_dict['download_time'] = '3.99'
        this_test_res_dict['res_download_time'] = 'SUCCESS'
        #------------------------
        this_test_dict.append(this_test_res_dict)
        print(this_test_dict)
        break
else:
    print('NOT FOUND')
    this_test_res_dict = {}
    this_test_res_dict['run_datetime'] = '01.01.2017 12:38:44'
    this_test_res_dict['download_time'] = '3.88'
    this_test_res_dict['res_download_time'] = 'SUCCESS'
    data['history'].append({"name":rep_name, "hist": [this_test_res_dict]})


with open('test_result.txt', 'wb') as output_file:
   output_file.write(json.dumps(data, sort_keys=False, indent=4).encode('utf-8'))

