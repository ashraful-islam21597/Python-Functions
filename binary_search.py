def binary_search(array,startpoint,item):

    endpoint=len(array)-1
    # midpoint=0
    loacation=-1
    comparison=0
    while(startpoint<=endpoint):
        comparison+=1
        midpoint=(startpoint+endpoint)//2
        if array[midpoint]==item:
            loacation=midpoint
            break
        elif(array[midpoint]<item):
            startpoint=startpoint+1
        else:
            endpoint=midpoint-1
    if(loacation==-1):
       return item,"not found"
    else:

        return loacation,comparison



array=[10,20,30,40,50,60,70,80,90]
print(binary_search(array,0,30))
# item=70
# startpoint=0
# endpoint=len(array)-1
# midpoint=0
# loacation=-1
# comparison=0
# while(startpoint<=endpoint):
#     comparison+=1
#
#     midpoint=(startpoint+endpoint)//2
#     if array[midpoint]==item:
#         loacation=midpoint
#         break
#     elif(array[midpoint]<item):
#         startpoint=startpoint+1
#     else:
#         endpoint=midpoint-1
# for i in array:
#     print(i)
# print("\n----------\n\n")
# if(loacation==-1):
#     print(item,"not found")
# else:
#     print(item,"found in",loacation," at " , comparison)
#
