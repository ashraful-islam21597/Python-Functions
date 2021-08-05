x=[10,20,30,40,50]

def Delete(index,array):
    """
index> the index of the array to be delete
array> the given array as parameter
"""
    array_size=len(x)
    while(index<array_size-1):
        array[index]=array[index+1]
        index+=1
    array.pop()
    return array
print(Delete(1,x))

