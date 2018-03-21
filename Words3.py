msg = input("Enter Any Message:")

print("-----------------------------------")
i = len(msg) - 1
a = len(msg)
while i >= 0:
    if msg[i] == ' ':
        print(msg[i + 1:a])
        a = i
    i = i - 1
print(msg[0:a])
print("-----------------------------------")


print("-----------------------------------")
i = len(msg) - 1
word = ""
while i >= 0:
    if msg[i] == ' ':
        print(word)
        word = ""
    else:
        word = msg[i] + word
    i = i - 1
print(word)
print("-----------------------------------")

