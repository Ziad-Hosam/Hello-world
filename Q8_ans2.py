import keyword

def checker(x):
    if x.isidentifier():
        if not keyword.iskeyword(x):
            print("Your variable name is right!!!!!")
        else:
            print("Sorry your variable name is wrong and is a keyword")
    else:
        print("Sorry your variable name is wrong")


a = input("Enter your variable name: ")
checker(a)