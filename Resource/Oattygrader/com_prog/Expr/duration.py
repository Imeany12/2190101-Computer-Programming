a = []
while True:
    i = input()
    
    if i  !="q":
        a.append(float(i))
    elif len(a)== 0 and i == "q":
        print("No Data")
        break
    elif i  =="q":
        av = sum(a)/len(a)
        ans = round(av,2)
        print(ans)
        break



        
