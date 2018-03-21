names = []
choice = ""
print("------------------------------------------")
while choice != "exit":
    choice = input("Enter name (exit to quit):")
    if choice != "exit":
        names.append(choice)
print("------------------------------------------")
i = 0
print("List of Names:")
while i < len(names):
    print(i + 1, ".", names[i])
    i += 1
print("------------------------------------------")
