names = []
choice = ""
longest = ""
second = ""
print("------------------------------------------")
while choice != "exit":
    choice = input("Enter name (exit to quit):")
    if choice != "exit":
        names.append(choice)
        if len(choice) > len(longest):
            second = longest
            longest = choice
        elif len(choice) > len(second):
            second = choice
print("------------------------------------------")
i = 0
print("List of Names:")
while i < len(names):
    print(i + 1, ".", names[i])
    i += 1
print("")
print("Name With the Most Characters:", longest)
print("Name With Second Most Characters:", second)
print("------------------------------------------")