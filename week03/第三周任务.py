# 1 "小数的十进制到二进制转换"
# num=input()
# int_part=int(num.split('.')[0])
# float_part=float('0'+'.'+num.split('.')[1])
# print(float_part)
# bin_int=bin(int_part)[2:]   # 二进制整数部分字符串序列
# bin_float='.'
# carry=0
# for i in range(8):
#     float_part*=2
#     carry=int(float_part)
#     bin_float+=str(carry)
#     float_part-=carry
# result=bin_int+bin_float
# print(result)


# 2 ""随机浮点数""
# import random
# random_num=random.uniform(10,21)
# print(random_num)


# 3 "验证身份证号是否合法"
# import re
# string=input()
# l=r"^\d{17}[0-9Xx]$"
# match=re.match(l,string)
# try:
#     print(match.group())
# except AttributeError:
#     print("不是身份证号码！")
# else:
#     print("是一个身份证号码")


# 4链表，增删改查

# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.nex=None
#
#
# class NodeList:
#     def __init__(self,nex):
#         self.nex=nex
#         self.num=0
#
#     def append(self,node):
#         node.nex=self.nex
#         self.nex=node
#         self.num+=1
#
#     def search(self,svalue):
#         pre=self
#         cur=self.nex
#         while cur!=0:
#             if cur.value==svalue:
#                 return pre,cur
#             else:
#                 pre=cur
#                 cur=cur.next
#         print("未找到该节点！")
#         return None,None
#
#     def change(self,value):
#         pre, cur = self.search(value)
#         if (pre,cur)==(None,None):
#             print("未找到该节点！")
#         else:
#             cur.value=value
#
#     def delete(self,value):
#         pre,cur=self.search(value)
#         if (pre,cur)==(None,None):
#             print("未找到该节点！")
#         else:
#             pre.next=cur.next
#             self.num-=1


# 5 for 循环

# li=[]
# for i in range(1,101):
#     if i%2==0:
#         li.append(i)
# print(li)


# 6 百分转等级制
# rank=""
# score=int(input("请输入成绩:"))
# if score<60:
#     rank="不合格"
# elif 60 <= score < 75:
#     rank="合格"
# elif 75 <= score < 90:
#     rank="良好"
# elif 90 <= score:
#     rank="优秀"
# print("等级制为："+rank)


# 7 最大公约数
# def euclidean_gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
#
# # 示例
# num1 =int(input("num1:"))
# num2 =int(input("num2:"))
# gcd = euclidean_gcd(num1, num2)
# print("最大公约数:", gcd)


# 8 排序算法比较


# 9 列表推导式
# def fun(length,a,i):
#     result=1
#     for j in range(0,length):
#         if j==i:
#             pass
#         else:
#             result*=a[j]
#     return result
#
#
# length=int(input("请输入数组长度："))
# li=input("请输入以”,“分隔的数组：")
# lj=li.split(",")
# lk=[int(i) for i in lj]
# lm=[fun(length,lk,i) for i in range(0,length)]
# print(lm)

