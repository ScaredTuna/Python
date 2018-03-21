

def name(a):
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
    else:
        b = ""
    return b


def hundred(w, a):
    if int(num[a]) != 0:
        w = w + name(int(num[a]))
        w = w + " Hundred "
    w = w + "and "
    w = ten(w, a + 1)
    return w


def ten(w, a):
    b = int(num[a])
    if b == 2:
        w = w + "Twenty "
    elif b == 3:
        w = w + "Thirty "
    elif b == 4:
        w = w + "Forty "
    elif b == 5:
        w = w + "Fifty "
    elif b == 6:
        w = w + "Sixty "
    elif b == 7:
        w = w + "Seventy "
    elif b == 8:
        w = w + "Eighty "
    elif b == 9:
        w = w + "Ninety "
    if b == 1:
        c = int(num[a + 1])
        if c == 0:
            w = w + "Ten"
        elif c == 1:
            w = w + "Eleven"
        elif c == 2:
            w = w + "Twelve"
        elif c == 3:
            w = w + "Thirteen"
        elif c == 4:
            w = w + "Fourteen"
        elif c == 5:
            w = w + "Fifteen"
        elif c == 6:
            w = w + "Sixteen"
        elif c == 7:
            w = w + "Seventeen"
        elif c == 8:
            w = w + "Eighteen"
        elif c == 9:
            w = w + "Nineteen"
    else:
        w = w + name(int(num[a + 1]))
    return w


num = input("Enter Any Number:")
word = ""
print("-----------------------------------")
if len(num) == 4:
    word = word + name(int(num[0]))
    word = word + " Thousand "
    word = hundred(word, 1)
elif len(num) == 3:
    word = hundred(word, 0)
elif len(num) == 2:
    word = ten(word, 0)
elif len(num) == 1:
    word = word + name(int(num[0]))
print("Number in Digits:", num)
print("Number in Words:", word)
print("-----------------------------------")
