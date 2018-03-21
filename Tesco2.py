product = input("Enter the Name of the Product:")
quantity = int(input("Enter the Quantity Bought:"))
unitPrice = float(input("Enter the Unit Price of Product:"))
productType = input("Is it a Food Item (y/n)?")

if productType == "y":
    VAT = 0

else:
    VAT = (quantity * unitPrice) * 7 / 100

print("------------------------------------------")
print("Products:", product, "x", quantity, "@", unitPrice, "each")
print("Total w/o VAT:", quantity * unitPrice)
print("VAT:", VAT)
print("Total Bill:", quantity * unitPrice + VAT)
print("------------------------------------------")
