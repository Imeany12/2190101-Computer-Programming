# students = []  
# 
# fn = open("Data.txt", "r")  
# for line in fn : 
#     sid,point = line.strip().split() # split gives 2 value in a list. We can use 2 variables.
#     point = float(point)          
#     students.append([point, sid]) # add to a list, with score first, so it can be used in sort.
# fn.close()
# 
# students.sort(reverse=True)   # we can sort normally and then reverse the list.
# for [point,sid] in students :
#     print(sid,point)
# fout = open("Boomer", "w")  #open for writing
# num = 0
# for i in range(1,101) :
#     num = num + i
#     fout.write(str(num)+" ")
#     if i%10 == 0 :
#         fout.write("\n")
# fout.close()
#practice
# fn = open("File.txt", "r")
# text = []
# for line in fn :
#     text.append(line.removesuffix("\n").strip())
# fn.close()
# for i in range(-1,-len(text)-1,-1) :
#     print(text[i])
filename = str(input())
fn = open(filename,"r")
text = []
for line in fn :
    line.replace("\n","")
    if line == " " :
        pass
    else : text.append(line)
fn.close()
fout = open("reverse.txt", "w")
for i in range(-1,-1-len(text),-1) :
    fout.write(text[i])
fout.close()
# filename1 = str(input())
# filename2 = str(input())
# fn = open(filename1,"r")
# text1 = []
# for line in fn :
#     text1.append(line.removesuffix("\n").strip())
# fn.close()
# fnn = open(filename2,"r")
# text2 = []
# for line in fnn :
#     text2.append(line.removesuffix("\n").strip())
# fnn.close()
# if text1 == text2 :
#     print("True")
# else : print("False")
