arr=[1000,10,100,5,50,20,500,2]
l=len(arr)-1
i=0
for i in range(l):
    for j in range(l-0):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)