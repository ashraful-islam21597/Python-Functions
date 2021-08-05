def  sum_of_digit(n):
    if n%2!=0:
        x=n//2
        sum=x*(n+1)+(x+1)
    else:
        x=n//2
        sum=x*(n+1)
    return sum
print(sum_of_digit(int(input())))
