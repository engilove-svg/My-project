def safe_divide(a,b):
    if b==0:
        print ("cannot divide by zero")
    else:
        return a/b

a=int(input())
b=int(input())
print(safe_divide(a,b))