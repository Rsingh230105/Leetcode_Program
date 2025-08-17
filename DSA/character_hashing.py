'''
s="azyxyyzaaaa"
q=["d","a","y","x"]

#TC=o(n+m), sc=o(26) or o(1)
#constraints ## this solution only for follow constraints
# 'a'<=s[i]<='z' like 97 to 122 asscii value
h_list=[0]*26

for ch in s:
    assci_value=ord(ch)
    index=assci_value - 97#ch='a', assi_value=97,index=97-97=0
    h_list[index]+=1

for ch in q:
    assci_value=ord(ch)
    index=assci_value - 97
    print(h_list[index])
'''

##method two  using dictionary ##
s="azyXyyAzaaMaa"
q=["d","Z","M","x"]

f_map={}

for i in s:
    if i in f_map:
        f_map[i]+=1
    else:
        f_map[i]=1
print(f_map)
for i in q:
    if i in f_map:
        print(f_map[i])
    else:
        print(0)
