a=int(input("enter a first number:\n"))
b=int(input("enter a second number:\n"))
op=int(input("which operation do you want to used?\nFor + operation,Press 1\nFor - operation,Press 2\n For * operation, Press 3\n For / operation, Press 4\n"))

match(op):
    case (1):
        print( a, "+", b ,"=",a+b)
    case (2):
        print("a-b=",a-b)
    case (3):
        print("a*b=",a*b)
    case (4):
        print("a/b=",a/b)