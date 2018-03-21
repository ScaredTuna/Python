message = input("Enter Any Message:")

print("------------------------------------------")
i = 0
a = 0
while i < len(message):
    if message[i] == ' ':
        print(message[a:i])
        a = i + 1
    i = i + 1
print(message[a:i])
print("------------------------------------------")

'''
print("------------------------------------------")
i = 0
while i < len(message):
    if message[i] == ' ':
        print("")
    else:
        print(message[i], end="")
    i = i + 1
print("------------------------------------------")
'''
'''
print("------------------------------------------")
i = 0
word = ""
while i < len(message):
    if message[i] == ' ':
        print(word)
        word = ""
    else:
        word = word + message[i]
    i = i + 1
print(word)
print("------------------------------------------")
'''
