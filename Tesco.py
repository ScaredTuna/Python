Product = "Pepsi"
Quantity = 10
Unit_Price = 1.25
Amount = Quantity * Unit_Price
VAT = Amount * 11 / 100
print("Product:", Product)
print("Quantity Purchased:", Quantity)
print("Unit Price:", Unit_Price)
print("----------------------------------")
print("Total Bill:", Amount)
print("VAT:", VAT)
print("Net Amount:", (Amount - VAT))