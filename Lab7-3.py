class insertion:
    def __init__(self,val):
        self.list = val
        self.i = 0

    def calculate(self):
        if self.i+1 >= len(self.list):
            return 0

        j = len(self.list[:self.i+2])-1

        while True:
            if j+1 == 1:
                break
            if self.list[j] < self.list[j-1]:
                self.list[j], self.list[j-1] = self.list[j-1], self.list[j]
            j -= 1

        print(f"sort |{self.i+1}|",self.list)

        self.i += 1

        insertion.calculate(self)
        return self.list

listVal = [11, 4, 7, 5, 10, 9, 13, 1]
s = insertion(listVal)
print("Default array : ",listVal)
print("Result : ",s.calculate())
