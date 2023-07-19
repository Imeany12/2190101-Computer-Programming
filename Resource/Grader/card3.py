class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return "("+str(self.value)+" "+str(self.suit) + ")"
    def next1(self):
        orderval = ["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
        ordersuit = ["club","diamond", "heart" ,"spade"]
        s = ordersuit.index(self.suit)
        v = orderval.index(self.value)
        if s < 3 :
            s += 1
        else :
            if v < 12 :
                v += 1
                s = 0
            else :
                v = 0
                s = 0
        newval = orderval[v]
        newsuit = ordersuit[s]
        return Card(newval, newsuit)
        # return "("+str(newval)+" "+str(newsuit)+")"
    def next2(self):
        orderval = ["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
        ordersuit = ["club","diamond", "heart" ,"spade"]
        s = ordersuit.index(self.suit)
        v = orderval.index(self.value)
        if s < 3 :
            s += 1
        else :
            if v < 12 :
                v += 1
                s = 0
            else :
                v = 0
                s = 0
        self.value = orderval[v]
        self.suit = ordersuit[s]
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
