no = int(input("Enter Number:"))

print("------------------------------------------")
if no > 7000:
    print("A")
    if no > 9000:
        print("C")
        if no < 10000:
            print("D")
        else:
            print("E")
else:
    print(1)
    if no > 5000:
        print(2)
    else:
        print(3)
        if no > 200:
            print(4)
        else:
            print(5)
print("------------------------------------------")
