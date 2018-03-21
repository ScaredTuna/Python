num = int(input("Enter Number:"))
range = int(input("Enter the Range:"))

print("----------------------------------")
print("TimesTable up to", range, "of:", num)
a = 1
while a <= range:
    print(num, "x", a, "=", num * a)
    a = a + 1
print("----------------------------------")
