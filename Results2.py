name = input("Enter Name:")
phy = int(input("Enter Physics Marks:"))
che = int(input("Enter Chemistry Marks:"))
mat = int(input("Enter Mathematics Marks:"))
tot = phy + che + mat
per = tot * 100 / 450
print("-------------------------------------")
print("Name:", name)
print("Total Marks:", tot)
print("Percentage:", per)
if per >= 60:
    print(name, "has Passed")
if per < 60:
    print(name, "has Failed")
print("-------------------------------------")