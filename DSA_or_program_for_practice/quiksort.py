
# def partition(ar,low,high):
#     pivot=ar[high]
#     i=low-1
#     for j in range(low,high):
#         if ar[j]<=pivot:
#             i=i+1
#             ar[i],ar[j]=ar[j],ar[i]
#     (ar[i + 1], ar[high]) = (ar[high], ar[i + 1])
#     return i + 1
# def quicksort(ar,low,high):
#     if low<high:
#         p=partition(ar,low,high) 
#         quicksort(ar,low,p-1)
#         quicksort(ar,p+1,high)
# ar=[45,2,37,8,0,9,4,51,2]
# size=len(ar)
# quicksort(ar,0,size-1)
# print(ar)


def quicksort(arr):
    # base case: empty or single-element array
    if len(arr) <= 1:
        return arr
    # choose the first element as the pivot
    pivot = arr[0]
    # create two sublists: one for smaller elements and one for larger elements
    smaller = [x for x in arr[1:] if x < pivot]
    print('s',smaller)
    larger = [x for x in arr[1:] if x >= pivot]
    print('l',larger)
    # recursively sort the sublists and concatenate them with the pivot
    return quicksort(smaller) + [pivot] + quicksort(larger)
arr=[45,2,37,8,0,9,4,51,2]
r=quicksort(arr)
print(r)