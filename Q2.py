import random


r_list = []
for i in range(0,10):
    x = random.randint(0,5)
    r_list.append(x)
print("The list is: " , r_list)


my_list = []
duplicates = []

for i in r_list:
    if i not in my_list:
        my_list.append(i)
    else:
        duplicates.append(i)

print("Duplicate numbers are: ", duplicates)