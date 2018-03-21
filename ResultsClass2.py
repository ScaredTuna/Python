class Results:
    def marks(self, a, b, c):
        self.phy = a
        self.che = b
        self.mat = c

    def showresult(self):
        tot = self.phy + self.che + self.mat
        print("Result =", tot)
        print("Percentage:", tot * 100 / 300)


print("-----------------------------")
peter = Results()
peter.marks(75, 80, 85)
peter.showresult()
print("-----------------------------")
