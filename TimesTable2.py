a = int(input("Enter Starting TimesTable:"))
b = int(input("Enter Ending TimesTable:"))

print("--------------------------------------------")
print("TimesTables from", a, "to", b)
print("--------------------------------------------")
while a <= b:
    print("TimesTable of:", a)
    c = 1
    while c <= 10:
        print(a, "x", c, "=", a * c)
        c = c + 1

    a = a + 1
    print("--------------------------------------------")
