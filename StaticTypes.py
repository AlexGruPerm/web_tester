from random import random

s1 = [round(random()*10) for i in range(1,10)]  #[1,2,3,4,5,6]
s2 = []
s3 = []

def solve_task(step):
    if len(s1)==0 and len(s3)==0:
        # крайний шаг
        return s1 or s2 or s3
    else:
        # рекурентный шаг
        if step == 1:
           mx = max(s1)
           while (True):
              if len(s1)==0:
                  break 
              x = s1.pop()
              #print("1- x=",x)
              if x == mx:
                 s2.append(x)
              else:
                 s3.append(x)
        else: # step=3
            mx = max(s3)
            while (True):
                if len(s3) == 0:
                    break
                x = s3.pop()
                #print("3- x=", x)
                if x == mx:
                   s2.append(x)
                else:
                   s1.append(x)
        next_step = 3 if step==1 else 1
        #print("step=",step,"s2=",s2)
        solve_task(next_step)


print(s1)
res = solve_task(1)
print(s2)


