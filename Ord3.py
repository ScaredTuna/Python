msg = input("Enter Any Message:")
print("-------------------------------------------")
i = 0
word = ""
while i < len(msg):
    if ord(msg[i]) >= 48 and ord(msg[i]) <= 57:
        word = word + str(int(msg[i]) * 2)
    elif ord(msg[i]) >= 65 and ord(msg[i]) <= 90:
        word = word + chr(ord(msg[i]) + 32)
    elif ord(msg[i]) >= 97 and ord(msg[i]) <= 122:
        word = word + chr(ord(msg[i]) - 32)
    else:
        word = word + msg[i]
    i += 1
print("Entered Message:", msg)
print("Altered Message:", word)
print("-------------------------------------------")