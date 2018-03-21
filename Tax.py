

def vat(salary):
    if salary > 20000:
        tax = salary * 21 / 100
    else:
        tax = salary * 17 / 100
    return tax


name = input("Enter Name:")
salary = int(input("Enter Salary:"))

print("------------------------------------")
print("Name:", name)
print("------------------------------------")
print("Total Salary: £", salary)
print("VAT: £", vat(salary))
print("Net Salary: £", salary - vat(salary))
print("------------------------------------")
print("Total Monthly Salary: £", salary / 12)
print("Monthly VAT: £", vat(salary) / 12)
print("Monthly Net Salary: £", (salary - vat(salary)) / 12)
print("------------------------------------")