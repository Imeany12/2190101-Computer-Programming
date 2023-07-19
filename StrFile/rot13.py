e = [",","!"," ","\"",":"]
n = ["0","1","2","3","4","5","6","7","8","9"]
while True:
    i = input()
    p = list(i)
    if i == "end":
        break
    else:
        k = []
        for x in i:
            if x in e or x in n:
                k.append(x)
            elif ord(x)>=78 and ord(x)<=80:
                k.append(chr(ord(x)-13))
            elif ord(x)<=109:
                k.append(chr(ord(x)+13))
            else:
                k.append(chr(ord(x)-13))
        print("".join(k))

    


        
