import matplotlib.pyplot as plt
import io
import json
import math

results_text_file = 'test_result.txt'
test_name = "Report 11_1 v2 Report page"

with io.open(results_text_file, encoding='utf-8', errors='ignore') as file:
    data = json.load(file)

x=[]
y=[]

for test_block in data['history']:
    if test_name in test_block['name']:
        this_test_list = test_block['hist']
        #print(type(this_test_dict))
        i=1
        for t in this_test_list:
            i+=1
            #print(i," ",t['download_time'])
            x.append(i)
            y.append(t['download_time'])


y_max = math.floor(max(y)+1)
print(y_max)

plt.plot(x, y, 'b.')
plt.axis([0, 400, 0, y_max])
plt.show()


