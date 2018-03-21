def binary():
    num = ""
    while num == "":
        print("-----------------------------------------------")
        num = input("Enter a Binary Number:")
        i = 0
        while i < len(num):
            if ord(num[i]) != 48 and ord(num[i]) != 49:
                print("-----------------------------------------------")
                print("Error: Input is not a Binary Number")
                i = len(num)
                num = ""
            else:
                i += 1
    return num


bin = binary()
print("-----------------------------------------------")
num = 0
i = len(bin) - 1
a = 0
while i >= 0:
    num += int(bin[i]) * (2 ** a)
    i -= 1
    a += 1
print("For the Binary Number:", bin)
print("The Decimal Value is:", num)
print("-----------------------------------------------")
