#optimal
'''
n=[5,3,2,2,1,5,5,7,5,10] #constraints-->1<=n[i]<=10 , n and m can have 10**8 elements
m=[10,111,1,9,5,67,2]
h_list=[0]*11# contarints ko dekh kar h_list=[0,0,0,0,0,0,0,0,0,0,0]

for i in n:# TC=o(n) , Sc=o(11)
    h_list[i]+=1

for i in m:     #TC=o(m)  total TC=o(n+m)
    if i<1 or i>10:
        print(0)
    else:
        print(h_list[i])
'''
#using dictionary
n=[5,3,2,2,1,5,5,7,5,10] #yha per constraint diye ho ya na diye ho ye kam karega but upper wala only constraint ke liye kam karega
m=[10,111,1,9,5,67,2]

f_map={}

for i in n:
    if i in f_map:
        f_map[i]+=1
    else:
        f_map[i]=1
print(f_map)
for i in m:
    if i in f_map:
        print(f_map[i])
    else:
        print(0)


