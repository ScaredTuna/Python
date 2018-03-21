name = input("Enter Name:")
salary = int(input("Enter Salary:"))
if salary >= 35000:
    VAT = salary * 21 / 100
if salary < 35000:
    VAT = salary * 17 / 100
print("----------------------------------------------")
print("Name:", name)
print("Salary:", salary)
print("----------------------------------------------")
print("Total VAT:", VAT)
print("Net Salary:", (salary - VAT))
print("Monthly Salary:", (salary / 12))
print("Monthly VAT:", (VAT / 12))
print("Monthly Net Salary:", ((salary - VAT) / 12))
print("----------------------------------------------")
