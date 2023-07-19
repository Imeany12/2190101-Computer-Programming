# HW02 (Don't delete this line or add any line above this line.)
def read_file(filename):
  # return a list of lines 
    k = []
    f =open(filename)
    for x in f:
        k.append(x)
    return k
def write_file(lines, filename):
  # return nothing, write all lines to filename 
    f = open(filename,"w")
    for e in range(len(lines)):
        if "\n" in lines[e]:
            lines[e] = lines[e][:-1]
    x = "\n".join(lines)
    f.write(x)
    f.close()
def vi_editor(lines, commands):
  # Write your code here
    leftright = 0
    updown = 0
    mode = "command"
    initaillines = lines
    if len(initaillines) ==0:
        case ="empty"
    else:
        case ="notempty"
    for x in range(len(commands)):
        if mode == "insert":
            if commands[x]=="[" and "[Esc]" in commands:
                mode = "command"
            if fac=="n" and mode =="insert":
                lines[updown] = list(lines[updown])
                lines[updown].insert(tmplr,commands[x])
                lines[updown] = "".join(lines[updown])
                tmplr +=1
            if commands[x] == "\n":
                tmplr =0
                new = lines[updown][x:]
                lines.insert(updown+1, lines[updown][leftright+1:])
                lines[updown] =lines[updown][:x]
                fac = "n"
                updown+=1
            if len(lines)!=0:
                if fac == "i" and mode =="insert" and case == "notempty":
                    newsen = []
                    newsen.append(commands[x])
                    this_line = list(lines[updown])
                    newsen = "".join(newsen)
                    this_line.insert(leftright,newsen)
                    k = "".join(this_line)
                    lines[updown] = k
                    leftright +=1
                if fac == "i" and mode =="insert" and case == "empty":
                    newsen = []
                    newsen.append(commands[x])
                    this_line = list(lines[updown])
                    newsen = "".join(newsen)
                    this_line.append(newsen)
                    k = "".join(this_line)
                    lines[updown] = k
                    leftright +=1
                elif fac=="o" and mode =="insert":
                    newsen = [] 
                    newsen.append(commands[x])
                    this_line = list(lines[updown])
                    newsen = "".join(newsen)
                    this_line.append(newsen)
                    k = "".join(this_line)
                    lines[updown] = k
            else:
                if fac == "i" and mode =="insert":
                    lines.append(commands[x])
        elif mode == "command":
            if commands[x]=="i":
                fac = "i"
                mode ="insert"
            elif commands[x] == "j":
                updown = min(updown+1,len(lines))
            elif commands[x] =="k":
                if updown!=0:
                    updown -= 1
            elif commands[x] =="l":
                leftright  = min(leftright+1,len(lines[updown]))
            elif commands[x] == "h":
                if leftright!=0:
                    leftright -= 1
            elif commands[x] =="o":
                fac = "o"
                lines.insert(updown,"")
                mode = "insert"
            elif commands[x]=="x":
                this_line = list(lines[updown])
                this_line.pop(leftright)
                k = "".join(this_line)
                lines[updown] = k
            elif commands[x]=="D":
                this_line = list(lines[updown])
                this_line = this_line[:leftright]
                k = "".join(this_line)
                lines[updown] = k
    return lines
# cmd = "llihello test\nsawadeee[Esc]"
# cmd = "iHello World\nHello Python"
# cmd = "lllxiThe newly added[Esc]hhhxx"
# cmd = "joThe is the new line"
# testlines = []
# testlines = ["The quick brown fox", "jumps over the lazy dog"]
# print(vi_editor(testlines,cmd))
lines = read_file('data.txt')
commands = "iHello World\nHello Python"
vi_editor(lines, commands)
write_file(lines, 'edited_data.txt')