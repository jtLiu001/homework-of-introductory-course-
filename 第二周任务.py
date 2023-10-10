# 1 递归
# def max_division(n,di):
#     if n <= 0:
#         return "输入应为正整数", 0
#     if di.get(n,0)!=0:
#         return di.get(n)
#     else:
#         max_=0
#         result=""
#         li = []
#         for i in range(1,int(n/2+1)):
#             a=max_division(i,di)
#             b=max_division(n-i,di)
#             product= a[1]*b[1]
#             if max_<product:
#                 max_=product
#                 li=[a[0], b[0]]
#             result="*".join(li)
#             # print(result)
#             # print(max_)
#         di[n]=(result,max_)
#         return result,max_
#
#
# d={1:("1",1),
#    2:("2",2),
#    3:("3",3)}
# num=int(input("请输入n:"))
# print(max_division(num,d)[0])
# 循环
# def max_division(n,di):
#     if di.get(n, 0) != 0:
#         return di.get(n)
#     li=[]
#     for i in range(4,n+1):
#         max_=0
#         result=""
#         for j in range(1,int(i/2)+1):
#             a=di[j]
#             b=di[i-j]
#             # print(a,b)
#             product= a[1]*b[1]
#             # print(product)
#             if max_<product:
#                 # print(1)
#                 # print(product)
#                 max_ = product
#                 li=[a[0], b[0]]
#                 result="*".join(li)
#         di[i]=(result,max_)
#
#
# d={1:("1",1),
#     2:("2",2),
#     3:("3",3),}
# n=int(input())
# max_division(n,d)
# s=d[n]
# print(s[0])
# 3
# def dfs(state, path, visited):
#     global chart
#     if state == "10":
#         # 找到了解决方案
#         print("找到解决方案：", path)
#         return
#
#     for st in chart[state]:
#         if st not in visited:
#             visited.add(st)
#             dfs(st, path + [st], visited)
#             visited.remove(st)
#
#
# # 初始状态：(1, 1, 1, 1) 表示人、狼、羊、菜都在起始岸
# initial_state ="1"
# # 移动方式
# states={"1":"人羊狼菜","2":"狼菜","3":"人狼菜","4":"狼","5":"人羊狼",
#         "6":"菜","7":"人羊菜","8":"羊","9":"人羊","10":"空",}
# chart={"1":("2",),
#        "2":("1","3"),
#        "3":("2","4","6"),
#        "4":("3","5"),
#        "5":("4","8"),
#        "6":("3","7"),
#        "7":("6","8"),
#        "8":("5","9"),
#        "9":("8","10"),
#        "10":("9",)}
# visited={"1",}
# path=["1",]
# dfs("1",path,visited)
# 4
# c=int(input())
# g=0
# while (g+1)**2<c:
#     g+=1
# h=0
# while (c-(g+h)**2)>0.0001:
#     h+=0.0001
# g=g+h
# print(g)

# # 5
# c=int(input())
# g=c/2
# i=0
# while abs(g**2-c)>0.0001:
#     i+=1
#     g=(g+c/g)/2
# print(g,i)

# 6没有太大影响

# 7
# c=int(input())
# g=c/2
# i=0
# while abs(g**3-c)>0.000000001:
#     i+=1
#     g=(2*g+c/g**2)/3
# print(g,i)

# 8 蒙特卡洛方法计算pi
# import numpy as np
# n = 100000
# count = 0
# for i in range(n):
#     x = np.random.uniform(0, 1)
#     y = np.random.uniform(0, 1)
#     if x**2 + y**2 < 1:
#         count += 1
# m = count / n
# pi = m * 4
# print(pi)

# # 9
# # 蒙特卡洛
# import numpy as np
# import math
# n = 100000
# count = 0
# for i in range(n):
#     x = np.random.uniform(2, 3)
#     y = np.random.uniform(0, 45)
#     if y<x**2+4*x*math.sin(x):
#         count += 1
# m = 45*count / n
# print(m)
# # 调用函数
# from scipy import integrate
# def f(x):
#     return x**2+4*x*math.sin(x)
#
# # 区间 [a, b]
# a = 2
# b = 3
#
# # 使用quad函数计算定积分
# result, error = integrate.quad(f, a, b)
#
# print("定积分的值:", result)
# print("误差估计:", error)
