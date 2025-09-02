## TC=o(nlogn)##best and average case
##sc=o(1)
## worst case-->[5,5,5,5,5,5,5,5,5]->o(n^2)

def partition(nums,low,high):
    pivot=nums[low]
    i=low
    j=high

    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j] = nums[j],nums[i]

    nums[low],nums[j] = nums[j],nums[low]
    return j ## j ke left me isse chote and right me bade no. hai


def quick_sort(nums,low,high):
    if low<high:
        p_idx=partition(nums,low,high)
        quick_sort(nums,low,p_idx-1)
        quick_sort(nums,p_idx+1,high)

arr = [4, 1, 7, 6, 3, 2, 8]
quick_sort(arr, 0, len(arr) - 1)
print(arr)