char = input("Enter Any Character:")
print("-------------------------------------------")
print(chr(ord(char) + 1))
print("-------------------------------------------")
ch = input("Enter Any Alphabet Character:")
print("-------------------------------------------")
if ord(ch) >= 65 and ord(ch) <= 90:
    print(chr(ord(ch) + 32))
elif ord(ch) >= 97 and ord(ch) <= 122:
    print(chr(ord(ch) - 32))
else:
    print("Entered Character is Not in Alphabet")
print("-------------------------------------------")
