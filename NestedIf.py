no = int(input("Enter Number:"))

print("-----------------------------------")
if no > 1000:
    print("A")
    if no > 5000:
        print("C")
    else:
        print("E")
else:
    print("B")
    if no > 500:
        print("D")
print("-----------------------------------")
