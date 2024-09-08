def cost(D):
    C = ((D*1000/140) * 0.25) + 4
    return C

D = int(input("Enter the distance in KM: "))

print(cost(D))