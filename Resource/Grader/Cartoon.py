cartoon = {}
order = []
while True :
    a = input()
    if a == "q" :
        break
    b = a.split(", ")
    if b[1] not in dict.keys(cartoon) :
        cartoon[b[1]] = b[0]
        order.append(b[1])
    else : cartoon[b[1]] += ", "+b[0]
for key in order :
    print(key +": " + cartoon[key])