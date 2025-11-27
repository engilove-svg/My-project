num=int(input("enter a number"))
rev = 0

while num > 0:
    digit = num % 10        # get last digit
    rev = rev * 10 + digit  # build reversed number
    num //= 10              # remove last digit

print("Reversed number:", rev)
