def sum_of_digits(n):
    if(n==0):
        return 0
    else:
        return n%10 + sum_of_digits(n//10)
    '''take last digit and remove the last digit'''
    
n=int(input("enter the number:\n"))
print(sum_of_digits(n))
