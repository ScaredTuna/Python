msg = input("Enter Any Message:")
print("-------------------------------------------")
digit = 0
upper = 0
lower = 0
other = 0
space = 0
i = 0
while i < len(msg):
    if ord(msg[i]) >= 48 and ord(msg[i]) <= 57:
        digit += 1
    elif ord(msg[i]) >= 65 and ord(msg[i]) <= 90:
        upper += 1
    elif ord(msg[i]) >= 97 and ord(msg[i]) <= 122:
        lower += 1
    elif ord(msg[i]) == 32:
        space += 1
    else:
        other += 1
    i += 1
print("The Message Contains:")
print(digit, "Digits")
print(upper, "Upper Case Letters")
print(lower, "Lower Case Letters")
print(space, "Spaces")
print(other, "Other Characters")
print("-------------------------------------------")
