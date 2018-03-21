message = input("Enter Any Message:")

print("--------------------------------------")
i = 0
while i < len(message):
    print(message[i])
    i = i + 1
print("--------------------------------------")
i = len(message) - 1
while i >= 0:
    print(message[i])
    i = i - 1
print("--------------------------------------")