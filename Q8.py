import keyword

def checker(x):
    return x.isidentifier() and not keyword.iskeyword(x)

a = input("Enter your variable name: ")

ans = checker(a)

print("Your variable name is: ", ans)