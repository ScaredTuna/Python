

def findandcount(msg, find):
    i = 0
    occur = 0
    while i < len(msg) - len(find) + 1:
        if msg[i: i + len(find)] == find:
            occur += 1
            i += len(find)
        else:
            i += 1
    return occur


msg = input("Enter Any Message:")
find = input("Enter Term to Search For:")

print("-------------------------------------------------------")
print("Message input: " + msg)
print("")
print("Number of Times '" + find + "' Occurs =", findandcount(msg, find))
print("-------------------------------------------------------")
