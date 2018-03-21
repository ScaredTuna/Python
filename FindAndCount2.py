

def findandcount(msg, find):
    i = 0
    occur = 0
    a = 0
    w = ""
    f = ""
    while a < len(msg):
        if ord(msg[a]) >= 65 and ord(msg[a]) <= 90:
            w += chr(ord(msg[a]) + 32)
        else:
            w += msg[a]
        a += 1
    a = 0
    while a < len(find):
        if ord(find[a]) >=65 and ord(find[a]) <= 90:
            f += chr(ord(find[a]) + 32)
        else:
            f += find[a]
        a += 1
    a = 0
    while i < len(w) - len(f) + 1:
        if w[i: i + len(f)] == f:
            occur += 1
            i += len(f)
        else:
            i += 1
    i = 0
    w = ""
    print("String =", occur)
    occur = 0
    while i < len(msg) - len(find) + 1:
        if msg[i: i + len(find)] == find:
            occur += 1
            i += len(find)
        else:
            i += 1
    i = 0
    print("String (Case Sensitive) =", occur)
    occur = 0
    while a < len(msg):
        if ord(msg[a]) >= 65 and ord(msg[a]) <= 90:
             w += chr(ord(msg[a]) + 32)
        else:
            w += msg[a]
        a += 1
    a = 0
    while i < len(w) - len(f) + 1:
        if i + len(f):
            a = 0
        if ord(w[i + len(f)]) >= 65 and ord(w[i + len(f)]) <= 90:
            i += 1
        elif ord(w[i + len(f)]) >= 97 and ord(w[i + len(f)]) <= 122:
            i += 1
        else:
            if i == 0:
                if w[i: i + len(f)] == f:
                    occur += 1
                    i += len(f)
                else:
                    i += 1
            else:
                if ord(w[i - 1]) >=65 and ord(w[i - 1]) <= 90:
                    i += 1
                elif ord(w[i - 1]) >= 97 and ord(w[i - 1]) <= 122:
                    i += 1
                else:
                    if w[i: i + len(f)] == f:
                        occur += 1
                        i += len(f)
                    else:
                        i += 1
    i = 0
    print("Words =", occur)
    occur = 0
    while i < len(msg) - len(find) + 1:
        if ord(msg[i + len(find)]) >= 65 and ord(msg[i + len(find)]) <= 90:
            i += 1
        elif ord(msg[i + len(find)]) >= 97 and ord(msg[i + len(find)]) <= 122:
            i += 1
        else:
            if i == 0:
                if msg[i: i + len(find)] == find:
                    occur += 1
                    i += len(find)
                else:
                    i += 1
            else:
                if ord(msg[i - 1]) >= 65 and ord(msg[i - 1]) <= 90:
                    i += 1
                elif ord(msg[i - 1]) >= 97 and ord(msg[i - 1]) <= 122:
                    i += 1
                else:
                    if msg[i: i + len(find)] == find:
                        occur += 1
                        i += len(find)
                    else:
                        i += 1
    i = 0
    print("Words (Case Sensitive) =", occur)
    occur = 0


msg = input("Enter Any Message:")
find = input("Enter Term to Search For:")

print("----------------------------------------")
print("Message input: " + msg)
print("Number of Times Search Term appears in Message as:")
findandcount(msg, find)
print("----------------------------------------")
