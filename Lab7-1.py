class bubble:
    def __init__(self,val):
        self.list = val
        self.i = 0
        self.last = 0

    def calculate(self):
        rangeList = len(self.list)
        if rangeList-self.i == 1:
            self.last += 1
            self.i = 0
            print(f"Sort |{self.last}| : ",self.list)
        elif rangeList-self.last == 1:
            return 0
        if self.list[self.i] > self.list[self.i+1]:
            self.list[self.i],self.list[self.i+1] = self.list[self.i+1],self.list[self.i]
        self.i += 1
        bubble.calculate(self)
        return self.list

listVal = [11, 4, 7, 5, 10, 9, 13, 1]
b = bubble(listVal)
print("Default array : ",listVal)
print("Result : ",b.calculate())
