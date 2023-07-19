n = int(input())
for x in range(n):
    k = input()
    for y in range(len(k)):
        if k[y] !=".":
            break
    print("."*(y//2)+k[y:])

        
            
    