import random
import datetime
import threading

class WorkerThread(threading.Thread):

 def __init__(self,arr:list, f_idx:int, l_idx:int, sort_type:str = 'asc'):
     super(WorkerThread,self).__init__()
     self.arr=arr
     self.f_idx=f_idx
     self.l_idx=l_idx
     self.sort_type=sort_type

 def run(self):
     last_index = (len(self.arr) - 1) if self.l_idx >= len(self.arr) else self.l_idx
     #print("Run thread.....")
     for j in range(last_index - self.f_idx):
         for i in range(self.f_idx, last_index + 1):
             # print(i)
             if i > self.f_idx:
                 if self.sort_type == 'asc':
                     if self.arr[i - 1] > self.arr[i]:
                         self.arr[i], self.arr[i - 1] = self.arr[i - 1], self.arr[i]
                 if self.sort_type == 'desc':
                     if self.arr[i - 1] < self.arr[i]:
                         self.arr[i], self.arr[i - 1] = self.arr[i - 1], self.arr[i]
                         # print("i=",i," arr[i]<arr[i-1] ",arr[i]," ",arr[i-1])
                         # print("j=[",j,"] -----------  ",arr)
         last_index -= 1 # max min elemt in right position
     return self.arr




def sort_array(arr:list, f_idx:int, l_idx:int, sort_type:str = 'asc'):
    """
    Сортировка по возрастанию.
    :param arr:  Лист в котором выполняется сортировка в диапазоне элементов от f_idx до l_idx
    :param f_idx: Индекс первого элемента, с которого начинается сортировка
    :param l_idx: Индекс конечного элемента до которого выполняется сортировка
    :param sort_type: asc,desc
    :return: отсортированный массив
    """
    #print(len(arr))
    last_index = (len(arr)-1) if l_idx >= len(arr) else l_idx

    for j in range(last_index-f_idx):
        for i in range(f_idx,last_index+1):
            #print(i)
            if i > f_idx:
                if sort_type == 'asc':
                    if arr[i-1] > arr[i]:
                        arr[i], arr[i-1] = arr[i-1], arr[i]
                if sort_type == 'desc':
                    if arr[i-1] < arr[i]:
                        arr[i], arr[i-1] = arr[i-1], arr[i]
                    #print("i=",i," arr[i]<arr[i-1] ",arr[i]," ",arr[i-1])
        #print("j=[",j,"] -----------  ",arr)
        last_index -= 1  # max min elemt in right position
    return arr


def test_sort_array():
    """
     TDD
    """
    test_array = [9,8,1,2,5,0,4,3]
    res = sort_array(test_array, f_idx = 0, l_idx = 7)
    print(res)
    if  res == [0,1,2,3,4,5,8,9]: # whole
        print("Test#1 OK")
    else:
        print("Test#1 FAIL")

    test_array = [9,8,1,2,5,0,4,3]
    res = sort_array(test_array, f_idx=0, l_idx=2)[0:3]
    print(res)
    if res == [1,8,9]: # first 3
        print("Test#2 OK")
    else:
        print("Test#2 FAIL")

    test_array = [9,8,1,2,5,0,4,3]
    res = sort_array(test_array, f_idx = 5, l_idx = 7)[-3:]
    print(res)
    if res == [0,3,4]: # last 3
        print("Test#3 OK")
    else:
        print("Test#3 FAIL")

    test_array = [9,8,1,2,5,0,4,3]
    res = sort_array(test_array, f_idx = 2, l_idx = 5)[2:6]
    print(res)
    if res == [0,1,2,5]: # middle 4, from index 2 to 5
        print("Test#4 OK")
    else:
        print("Test#4 FAIL")


#test_sort_array()

#w_array = [9,8,1,2,5,0,4,3]
#print(w_array)
#res = sort_array(w_array, f_idx = 0, l_idx = 8, sort_type='desc')
#print(res)

#print(16//4)


w_array = [random.randint(0,10) for _ in range(40000)]
s_array = w_array.copy() # for second algo
#@@@ print(w_array)
t_begin = datetime.datetime.now()
res = sort_array(w_array, f_idx = 0, l_idx = len(w_array), sort_type='asc')
t_end = datetime.datetime.now()
delta = t_end - t_begin
#@@@print(res)
print("(1)Duration = ",delta.total_seconds()," sec.") # 24 sec.

print("============================================")
#@@@print(s_array)
t_begin = datetime.datetime.now()
workerthreadlist=[]

thread_count = 100
parts_count = len(s_array)//thread_count

for x in range(0,thread_count): # 0 (0-3) 1 (4-7) 2 (8-11)
 newthread = WorkerThread(s_array, f_idx = x*parts_count, l_idx = (x+1)*parts_count-1, sort_type='asc')
 workerthreadlist.append(newthread)
 newthread.start()
for x in range(0,thread_count):
 workerthreadlist[x].join()

print("============================================")

#@@@print(s_array)
# тут ещё проход по общему списку, который отсортирован частично.
res2 = sort_array(s_array, f_idx = 0, l_idx = len(w_array), sort_type='asc') #общий проход с малым количеством перестановок.

#@@@print(res2)
t_end = datetime.datetime.now()
delta = t_end - t_begin
print("(1)Duration = ",delta.total_seconds()," sec.")

if res==res2:
    print("OK. Arrays are equal")
else:
    print("Fail. Arrays are NOT equal")

#x = [1, 2, 3]
#x.extend([4, 5])
#print (x)

''''''