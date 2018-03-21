

def ones(a):
    if a == 1:
        b = "One"
    elif a == 2:
        b = "Two"
    elif a == 3:
        b = "Three"
    elif a == 4:
        b = "Four"
    elif a == 5:
        b = "Five"
    elif a == 6:
        b = "Six"
    elif a == 7:
        b = "Seven"
    elif a == 8 :
        b = "Eight"
    elif a == 9:
        b = "Nine"
    elif a == 10:
        b = "Ten"
    elif a == 11:
        b = "Eleven"
    elif a == 12:
        b = "Twelve"
    elif a == 13:
        b = "Thirteen"
    elif a == 14:
        b = "Fourteen"
    elif a == 15:
        b = "Fifteen"
    elif a == 16:
        b = "Sixteen"
    elif a == 17:
        b = "Seventeen"
    elif a == 18:
        b = "Eighteen"
    elif a == 19:
        b = "Nineteen"
    else:
        b = ""
    return b


def ty(a):
    if a == 2:
        b = "Twenty "
    elif a == 3:
        b = "Thirty "
    elif a == 4:
        b = "Forty "
    elif a == 5:
        b = "Fifty "
    elif a == 6:
        b = "Sixty "
    elif a == 7:
        b = "Seventy "
    elif a == 8:
        b = "Eighty "
    elif a == 9:
        b = "Ninety "
    return b


num = int(input("Enter Any Number:"))
numb = num
word = ""
print("-------------------------------------")
if num == 0:
    word = "Zero"
if num >= 1000:
    word = ones(num // 1000) + " Thousand "
    num = num % 1000
if num >= 100:
    word += ones(num // 100) + " Hundred "
    num = num % 100
if numb >= 100 and num != 0:
    word += "and "
if num >= 20:
    word += ty(num // 10)
    num = num % 10
if num > 0:
    word += ones(num)
print("Number in Digits:", numb)
print("Number in Words:", word)
print("-------------------------------------")
