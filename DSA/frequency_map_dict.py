#method 1
'''
nums=[5,6,7,7,1,9,111,1,1,5,1,1]
f_map={}
for i in range(0,len(nums)): #TC=o(n), SC=o(N)
    if nums[i] in f_map:
        f_map[nums[i]] += 1
    else:
        f_map[nums[i]] = 1# if key exist nahi karti to create karke 1 value asign kar dega like: key:value
print(f_map)
'''

nums=[5,6,7,7,1,9,111,1,1,5,1,1]
hash_map={}
n=len(nums)

for i in range(0,n): #TC=o(N)
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1 #TC=o(1), average case ->acces,update, delete,add kal maximum o(1) hi hoga
    #get method check dictionary in nums[i] ,if exist this key then return value , if not exist then return 0
print(hash_map)