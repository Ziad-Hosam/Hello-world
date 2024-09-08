n = int(input("Enter your number: ").strip())

if n%2 != 0:
    print("Wired")
elif n%2 == 0 and n > 1 and n < 6:
    print("Not Wired")
elif n%2 == 0 and n > 5 and n < 21:
    print("Wired")
elif n%2 == 0 and n > 20:
    print("Not Wired")