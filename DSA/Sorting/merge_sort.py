##Divide and merge
## TC=o(nlogn)
## SC=o(n) #new result wala array liya hai
##Two merge sorted array

def merge_array(l,r):
    res=[]
    i,j=0,0
    n,m=len(l),len(r)
    while i<n and j<m:
        if l[i]<=r[j]:
            res.append(l[i])
            i+=1
        else:
            res.append(r[j])
            j+=1

    if i<n:
        while i<n:
            res.append(l[i])
            i+=1
    if j<m:
        while j<m:
            res.append(r[j])
            j+=1
    return res

#print(merge_array([1,2,3,4],[1,1,3,4,5,6,7]))


#### merge sort

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_arr = arr[:mid]
    right_arr =arr[mid:]

    left=merge_sort(left_arr)
    right=merge_sort(right_arr)

    return merge_array(left,right) ##recursive call

print(merge_sort([3,1,2,4,1,5,2,6,4]))