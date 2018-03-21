msg = input("Enter Any Message:")

print("--------------------------------------")
store = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while i < len(msg):
    if ord(msg[i]) >= 65 and ord(msg[i]) <= 90:
        store[ord(msg[i]) - 65] += 1
    elif ord(msg[i]) >= 97 and ord(msg[i]) <= 122:
        store[ord(msg[i]) - 97] += 1
    else:
        store[26] += 1
    i += 1
i = 0
print("Entered Message:", msg)
print("")
print("Number of Each Letter:")
while i < len(store) - 1:
    if store[i] != 0:
        print(chr(i + 65), "=", store[i])
    i += 1
print("Other =", store[26])
print("--------------------------------------")