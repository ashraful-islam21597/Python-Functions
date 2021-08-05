
def part(arr,left,right):
    pivot=arr[right]
    while(arr[left]<pivot):
        left+=1
    while(arr[right]>pivot):
        right-=1
    if right==left:
        return left
    else:
        arr[left],arr[right]=arr[right],arr[left]
        return part(arr,left,right)


def quicksort(arr,left,right):
    if left<right:
        partitionpoint=part(arr,left,right)
        quicksort(arr,left,partitionpoint-1)
        quicksort(arr,partitionpoint+1,right)
    return arr
values=[2,7,1,8,6,3,5,4]
quicksort(values, 0, len(values) - 1)
print(values)