#write a program that takes a list of numbers and removes all duplicate using a set
user_input=input("enter a number separated by the space\n")
number=list(map(int,user_input.split()))
uniq_number=list(set(number))
print("numbers:",number)
print("without duplicates:",uniq_number)
