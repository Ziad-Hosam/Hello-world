a = int(input("Enter number of Rows: "))

for x in range(a):
    print(' ' * x, end='')
    print('* ' * (a - x))