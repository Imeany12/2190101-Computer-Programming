i = list(input())
for x in range(len(i)):
    if i[x] == "(":
        i[x] = "["
    elif i[x] == ")":
        i[x] = "]"
    elif i[x] == "[":
        i[x] = "("
    elif i[x] == "]":
        i[x] = ")"

print("".join(i))
    