v = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
s = ["club","diamond","heart", "spade"]
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return "({} {})".format(self.value,self.suit)
    def next1(self):
        ise = s.index(self.suit) 
        iva = v.index(self.value)
        if self.suit == s[-1]:
            if self.value == v[-1]:
                return Card(v[0],s[0])
            else:
                return Card(v[iva+1],s[0])
        else:
            return Card(self.value,s[ise+1])
    def next2(self):
        ise = s.index(self.suit) 
        iva = v.index(self.value)
        if self.suit == s[-1]:
            if self.value == v[-1]:
                self.value = v[0]
                self.suit = s[0]
            else:
                self.value = v[iva+1]
                self.suit = s[0]
        else:
            self.suit = s[ise+1]
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