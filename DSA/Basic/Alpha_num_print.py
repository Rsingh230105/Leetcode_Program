# x=input("enter your alphanumeric:")
# l_al=[]
# l1_num=[]
# for i in x:
#     if (i>='A' and i<='Z') or (i>'a' and i<='z'):
#         l_al.append(i)
# for i in x:
#     if i>='0' and i<='9':
#         l1_num.append(i)
#
# l_al.sort()
# l1_num.sort()
# # print(l_al)
# print(l1_num)
# f=l_al+l1_num
#
# s=""
# for i in f:
#     s=s+i
# print(s)
#
#

x=input("enter your alphanumeric:")
l=[]
l1=[]
for i in x:
    if i.isalpha():
        l.append(i)
    else:
        l1.append(i)
f=sorted(l)+sorted(l1)
op="".join(f)
print(op)


