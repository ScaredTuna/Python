name = input("Enter Name:")
salary = int(input("Enter Salary:"))

print("----------------------------------------")
if salary < 10000:
    vat = 0
if salary >= 10000 and salary < 20000:
    vat = salary * 11 / 100
if salary >= 20000 and salary < 30000:
    vat = salary * 17 / 100
if salary >= 30000 and salary < 40000:
    vat = salary * 21 / 100
if salary >= 40000:
    vat = salary * 29 / 100

print("Name:", name)
print("Salary: £", salary)
print("----------------------------------------")
print("VAT: £", vat)
print("Net Salary: £", salary - vat)
print("Monthly Salary:", (salary / 12))
print("Monthly VAT:", (vat / 12))
print("Monthly Net Salary:", ((salary - vat) / 12))
print("----------------------------------------")
