

def hellomessage():
    print("Hello")
    print("My")
    print("Friends!")


def add(a, b):
    print(a, "+", b, "=", a + b)


def biggestnum(a, b):
    if a > b:
        print(a, ">", b)
    elif b > a:
        print(b, ">", a)
    else:
        print(a, "=", b)


print("------------------------------------")
hellomessage()
print("------------------------------------")
add(7, 5)
add(10, 20)
print("------------------------------------")
biggestnum(7, 2)
biggestnum(3, 3)
biggestnum(2, 5)
print("------------------------------------")