class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return "("+str(self.value)+" "+str(self.suit) + ")"
    def next1(self):
        orderval = ["3","4","5","6","7","8","9","10","J","Q","K","A","2","3"]
        ordersuit = ["club","diamond", "heart" ,"spade","club"]
        newval = orderval[orderval.index(self.value)]
        newsuit = ordersuit[ordersuit.index(self.suit)]
        return Card(newval, newsuit)
    def next2(self):
        orderval = ["3","4","5","6","7","8","9","10","J","Q","K","A","2","3"]
        ordersuit = ["club","diamond", "heart" ,"spade","club"]
        self.value = orderval[orderval.index(self.value)+1]
        self.suit = ordersuit[ordersuit.index(self.suit)+1]
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
