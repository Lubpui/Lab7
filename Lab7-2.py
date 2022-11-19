class selection:
    def __init__(self,val):
        self.list = val
        self.i = 0

    def calculate(self):
        if self.i+1 >= len(self.list):
            return 0
        minVal = self.list.index(min(self.list[self.i:]))
        self.list[self.i], self.list[minVal] = self.list[minVal], self.list[self.i]
        print(f"Sort |{self.i+1}|",self.list)
        self.i += 1
        selection.calculate(self)
        return self.list

listVal = [11, 4, 7, 5, 10, 9, 13, 1]
s = selection(listVal)
print("Default array : ",listVal)
print("Result : ",s.calculate())
