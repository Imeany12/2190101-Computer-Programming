k =input()
v =["a","e","i","o","u"]
l = ["s","x","ch"]
if k[-1] in l or k[-2:] in l:
    print(str(k)+"es")
elif k[-1] =="y" and k[-2] not in v:
    print(str(k[:-1])+"ies")
else:
    print(str(k)+"s")