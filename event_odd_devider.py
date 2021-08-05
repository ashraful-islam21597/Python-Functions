lst=[2,31,6,0,2,9,13,11,19,20,17]
print(list(sorted(lst, key=lambda x: [x % 2, x])))