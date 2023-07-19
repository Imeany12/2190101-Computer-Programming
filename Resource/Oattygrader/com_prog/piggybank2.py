class piggybank:
    def __init__(self):
        self.coins  ={}
    def add(self,v,n):
        if float(v) in self.coins:
            if (self.coins[float(v)]+int(n))>100:
                return False
            else:
                self.coins[float(v)]+=int(n)
                return True
        else:
            self.coins[float(v)] = int(n)
            return True
    def __int__(self):
        k = sum([int(self.coins[e]) for e in self.coins])
        return int(k)
    def __float__(self):
        k = sum([e*self.coins[e] for e in self.coins])
        return float(k)
    def __str__(self):
        k = [str(e)+":"+str(self.coins[e]) for e in sorted(self.coins)]
        return  "{"+str(", ".join(k))+"}"
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)

