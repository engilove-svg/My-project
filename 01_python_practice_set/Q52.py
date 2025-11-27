#create a set my_set={1,2,3,3,4} and print it. What happens to duplicate 3?
my_set={1,2,3,3,4}


my_set.remove(2)
my_set.add(5)
print(my_set)
if 4 in my_set:
    print("4 is in the set")
else:
    print("4 is not in the set")
