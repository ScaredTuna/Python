message = input ("Enter Any Message:")

print("-------------------------------------")
i = 0
space = 0
while i < len(message):
    if message[i] == ' ':
        space = space + 1
    i = i + 1
print("Message is:", message)
print("Number of Words =", space + 1)
print("-------------------------------------")
