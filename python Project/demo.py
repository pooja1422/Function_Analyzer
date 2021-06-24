# quick sort
def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[-1]
        sm,eq,lg=[],[],[]
        for nums in arr:
            if nums<pivot:
                sm.append(nums)
            elif nums==pivot:
                eq.append(nums)
            else:
                lg.append(nums)
    return quick_sort(sm)+eq+quick_sort(lg)

# merge sort

def merge(l1,l2):
    res=[]
    i, j=0,0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i+=1
        else:
            res.append(l2[j])
            j+=1
    while i<len(l1):
        res.append(l1[i])
        i+=1
    while j<len(l2):
        res.append(l2[j])
        j+=1
    return res
def merge_sort(arr):
    if len(arr)<2:
        return arr[:]
    else:
        mid=len(arr)//2
        a1=merge_sort(arr[:mid])
        a2=merge_sort(arr[mid:])
        return merge(a1,a2)
# bubble sort
def bubble_sort(arr):
    swap=True
    while swap:
        swap=False
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                swap=True
                arr[i],arr[i+1]=arr[i+1],arr[i]
