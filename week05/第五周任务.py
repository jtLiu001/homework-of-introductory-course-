import math
import time
import random


def is_prime_num(num):
    for i in range(2,int(math.sqrt(num))):
        if num%i==0:
            return 0    # 合数

    return 1    # 质数


def insert_sort(lts):
    length=len(lts)
    for i in range(1,length):
        i_value=lts[i]
        j=i-1
        while lts[j]>=i_value and j>=0:
            lts[j+1]=lts[j]
            j-=1
        lts[j+1]=i_value


n=int(input())
l=[]
for k in range(n):
    l.append(random.uniform(0,100000))
print(l)
start_time=time.time()
insert_sort(l)
end_time=time.time()
print(l)
print(f"运行时间为：{end_time-start_time}")
