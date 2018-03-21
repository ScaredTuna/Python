class Results:
    phy = 0
    che = 0
    mat = 0

    def showresults(self):
        tot = self.phy + self.che + self.mat
        print("Result =", tot)
        print("Percentage:", tot * 100 / 300)


print("-------------------------------")
Peter = Results()
Peter.phy = 75
Peter.che = 100
Peter.mat = 90
Peter.showresults()
print("-------------------------------")
