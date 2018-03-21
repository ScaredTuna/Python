bill = float(input("Enter Total Bill:")) * 100
paid = float(input("Enter Amount Paid:")) * 100

print("---------------------------------------")
print("Total Bill = £", bill / 100)
print("Amount Paid = £", paid / 100)
print("---------------------------------------")
balance = (paid - bill)
print("Change Due = £", balance / 100)
print("---------------------------------------")
if balance >= 5000:
    fifty = balance // 5000
    balance = balance % 5000
    print("£50 =", int(fifty))
if balance >= 2000:
    twenty = balance // 2000
    balance = balance % 2000
    print("£20 =", int(twenty))
if balance >= 1000:
    balance = balance - 1000
    print("£10 =", 1)
if balance >= 500:
    balance = balance - 500
    print("£5 =", 1)
if balance >= 200:
    two = balance // 200
    balance = balance % 200
    print("£2 =", int(two))
if balance >= 100:
    balance = balance - 100
    print("£1 =", 100)
if balance >= 50:
    balance = balance - 50
    print("50p =", 1)
if balance >= 20:
    twentyp = balance // 20
    balance = balance % 20
    print("20p =", int(twentyp))
if balance >= 10:
    balance = balance - 10
    print("10p =", 1)
if balance >= 5:
    balance = balance - 5
    print("5p =", 1)
if balance >= 2:
    twop = balance // 2
    balance = balance % 2
    print("2p =", int(twop))
if balance >= 1:
    balance = balance - 1
    print("1p =", 1)
print("---------------------------------------")
