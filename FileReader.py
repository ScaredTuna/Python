qa = open("data.txt")
for line in qa:
    print(line)

F1 = open("data.txt", "r")
F2 = open("data2.txt", "w")
for something in F1:
    print(something, file=F2)