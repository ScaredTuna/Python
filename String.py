name = input("Enter Name:")
start = int(input("Enter Starting Number:"))
end = int(input("Enter Ending Number:"))

print("-------------------------------------------")
print(name)
print(name[0], name[3])
print(name[1:4])
if end < len(name):
    print(name[start:end])
else:
    print("End Value is Beyond End of Name")
print("-------------------------------------------")