regnos = []
names = []
genders = []
groups = []
adds = []
marks = []


def create():
    regnos.append(input("Enter Registration Number:"))
    names.append(input("Enter Name:"))
    gender = ""
    while gender != "f" and gender != "m":
        gender = input("Enter Gender (m/f):")
        if gender == "f" or gender == "m":
            genders.append(gender)
        else:
            print("-----------------------------------------------")
            print("Error: Invalid Gender Entered. Please Enter m/f")
            print("-----------------------------------------------")
    marks.append(input("Enter Marks:"))
    group = ""
    while group != "Java" and group != ".Net" and group != "Big Data":
        group = input("Enter Group (Java, .Net, Big Data):")
        if group == "Java" or group == ".Net" or group == "Big Data":
            groups.append(group)
        else:
            print("-----------------------------------------------")
            print("Error: Invalid Group. Please Enter One of: Java, .Net or Big Data")
            print("-----------------------------------------------")
    adds.append(input("Enter Address:"))


def data(i):
    print("")
    print("Registration Number:", regnos[i])
    print("Name:", names[i])
    if genders[i] == "m":
        print("Gender: Male")
    elif genders[i] == "f":
        print("Gender: Female")
    print("Marks:", marks[i])
    print("Group:", groups[i])
    print("Address:", adds[i])
    print("")


def groupprint(a, c):
    i = 0
    while i < len(regnos):
        if c[i] == a:
            data(i)
        i += 1


def intcheck():
    num = "a"
    while ord(num) < 48 or ord(num) > 57:
        num = input("Please Select Number of Desired Service:")
        if ord(num) < 48 or ord(num) > 57:
            print("-----------------------------------------------")
            print("Error: Entry Must Be a Number")
    return int(num)


def menu():
    print("-----------------------------------------------")
    print("1: Enter Record")
    print("2: View Records")
    print("3: Quit")
    choice = intcheck()
    return choice


choice = menu()
while choice != 3:
    if int(choice) == 1:
        print("-----------------------------------------------")
        create()
        while choice != "y" and choice != "n":
            print("-----------------------------------------------")
            choice = input("Do You Wish to Enter Another Record (y/n)?:")
            if choice != "y" and choice != "n":
                print("Error: Invalid Choice. Please Enter y/n")
        if choice == "y":
            choice = 1
        elif choice == "n":
            choice = menu()
    elif choice == 2:
        print("-----------------------------------------------")
        print("1: All Records")
        print("2: Specific Record")
        print("3: Male Records")
        print("4: Female Records")
        print("5: Java Records")
        print("6: .Net Records")
        print("7: Big Data Records")
        print("8: Return to Previous Menu")
        choice = intcheck()
        if choice == 1:
            print("-----------------------------------------------")
            i = 0
            while i < len(regnos):
                data(i)
                i += 1
        elif choice == 2:
            print("-----------------------------------------------")
            reg = input("Enter Registration Number of Record to View:")
            print("-----------------------------------------------")
            groupprint(reg, regnos)
        elif choice == 3:
            print("-----------------------------------------------")
            print("Male Records:")
            groupprint("m", genders)
        elif choice == 4:
            print("-----------------------------------------------")
            print("Female Records:")
            groupprint("f", genders)
        elif choice == 5:
            print("-----------------------------------------------")
            print("Java Records:")
            groupprint("Java", groups)
        elif choice == 6:
            print("-----------------------------------------------")
            print(".Net Records:")
            groupprint(".Net", groups)
        elif choice == 7:
            print("-----------------------------------------------")
            print("Big Data Records:")
            groupprint("Big Data", groups)
        elif choice == 8:
            choice = "n"
        else:
            print("-----------------------------------------------")
            print("Error: Invalid Selection")
        while choice != "y" and choice != "n":
            print("-----------------------------------------------")
            choice = input("Do You Wish to View More Records (y/n)?:")
            if choice != "y" and choice != "n":
                print("Error: Invalid Choice. Please Enter y/n")
        if choice == "y":
            choice = 2
        elif choice == "n":
            choice = menu()
    else:
        print("-----------------------------------------------")
        print("Error: Invalid Choice. Please Select Number From List")
        choice = menu()
