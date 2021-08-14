def sorting(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]

        sorting(l)

        sorting(r)

        i=0
        j=0
        k=0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
    return arr



l=[1,8,3,6,2,7,14,25,56,4]
print(sorting(l))

# def test(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
#         arr=arr[:mid]
#         test(arr)
#     return arr
# l=[1,2,3,5,6,7,8]
# print(test(l))


