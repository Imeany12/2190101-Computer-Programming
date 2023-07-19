#id = str(input())
#x = (11-(13*int(id[0])+12*int(id[1])+11*int(id[2])+10*int(id[3])+9*int(id[4])+8*int(id[5])+7*int(id[6])+6*int(id[7])+5*int(id[8])+4*int(id[9])+3*int(id[10])+2*int(id[11]))%11)%10
#ans = id[0]+" "+id[1:5]+" "+id[5:10]+" "+id[10:]+" "+str(x)
#print(ans)
#######################
#num = int(input())
#read = ["zero","one","two","three","four","five","six","seven","eight","nine"]
#print( num,"-->",read[num])
#######################
#input = str(input())
#x = input.split("/") 
#month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
#print(input[-7:-5:1]) check month num
#print(month[int(x[1])-1],x[0]+",",x[2])
#######################
#num = str(input())
#digit = int(input())
#digit -= len(num)
#zero = "0"*digit
#print(zero+num)
#######################
#input = str(input())
#x = input.split()
#sum = int(x[0]) + int(x[1]) + int(x[2]) + int(x[3]) + int(x[4]) + int(x[5]) + int(x[6])
#print(sum)
#######################
#u = str(input())
#v = str(input())
#u = u.strip("[]")
#v = v.strip("[]")
#u = u.split(",")
#v = v.split(",")
#u = [float(u[0]),float(u[1]),float(u[2])]
#v = [float(v[0]),float(v[1]),float(v[2])]
#ans =[float(u[0])+float(v[0]),float(u[1])+float(v[1]),float(u[2])+float(v[2])]
#3print(u,"+",v,"=",ans)
#######################
#data = str(input())
#i1 = data[3] + data[10] + data[17] + data[24] + data[31]
#i2 = data[7] + data[12] + data[17] + data[22] + data[27]
#i3 = int(i1)+int(i2) + 10000
#i4 = str(i3)
#i5 = int(i4[-4])+int(i4[-3])+int(i4[-2])
#i6 = i5%10 + 1
#text = ["A","B","C","D","E","F","G","H","I","J"]
#print(i4[-4]+i4[-3]+i4[-2]+text[i6-1])
#######################
#import math
#take input turn into simple decimal
#input = input()
#x = input.split(",")
#sum = ((int(x[0])+0)/1 + (int(x[1]+x[2]))/10**(len(x[1]+x[2])))
#print(sum)
#take decimal turn into fraction
#length = len(str(sum))
#numerator = sum*(10**length)
#denominator = 10**length
#divisor = math.gcd(int(numerator),int(denominator))
#print(str(int(numerator/divisor))+" / "+str(int(denominator/divisor)))
#numerator = float(x[1]+x[2])-float("0"+x[1])
#denominator = float("9"*len(x[2])+"0"*len(x[1]))
#divisor = math.gcd(int(numerator),int(denominator))
#print(str(int(x[0])*int(denominator/divisor)+int(numerator/divisor))+" / "+str(int(denominator/divisor)))
#input = input()
#code = ["01","02","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","51","53","55","58"]
#name = ["The Sirindhorn Thai Language Institute","General Education Center","Graduate School","Faculty of Engineering",
#        "Faculty of Arts","Faculty of Science"," Faculty of Political Science","Faculty of Architecture",
#        "Faculty of Commerce and Accountancy","Faculty of Education","Faculty of Communication Arts","Faculty of Economics",
#        "Faculty of Medicine","Faculty of Veterinary Science","Faculty of Dentistry","Faculty of Pharmaceutical Sciences",
#        "Faculty of Law","Faculty of Fine and Applied Arts","Faculty of Nursing","Faculty of Allied Health Sciences",
#        "Faculty of Psychology","Faculty of Sports Science","School of Agricultural","College of Population Studies",
#        "College of Public Health Sciences","Language Institute","Sasin Graduate Institute of Business","Administration of Chulalongkorn University"]
#if (input in code or input in name):
#        print("OK")
#else :
#        print("Error")
#s = float(input())
#if s>= 80 :
#        print("A")
#elif s>= 70 :
#        print("B")
#elif s>= 60 :
#        print("C")
#elif s>= 50 :
#        print("D")
#else :
#        print("F")
#x = [float(i) for i in input().split()]
#find minimum x
#min_x = x[0]
#if x[1] < min_x:
#        min_x = x[1]
#if x[2] < min_x:
#        min_x = x[2]
#if x[3] < min_x:
#        min_x = x[3]
#find maximum x
#max_x = x[3]
#if x[2] > max_x:
#        max_x = x[2]
#if x[1] > max_x:
#        max_x = x[1]
#if x[0] > max_x:
#        max_x = x[0]
#final ans
#final = x[0] + x[1] + x[2] + x[3] - min_x - max_x
#print(round(final/2,2))
#x = int(input())
#if x//(10**9) :
#        print("Reject")
#elif 1000<x<=2000 :
#        print(58)
#elif 500<x<=1000 :
#        print(38)
#elif 250<x<=500 :
#        print(28)
#elif 100<x<=250 :
#        print(22)
#else :
#        print(18)
#x = input()
#n = len(x)
#if n>9 :
#        if n>10:
#                y = round(int(x)/10**9)
#                print(str(y)+"B")
#        else:
#                y = round(int(x)/10**9,1)
#                print(str(y)+"B")
#elif n>6 :
     #   if n>7:
    #            y = round(int(x)/10**6)
   #             print(str(y)+"M")
  #      else:
 #               y = round(int(x)/10**6,1)
#                print(str(y)+"M")
#elif n>3 :
#        if n>4:
#                y = round(int(x)/10**3)
#                print(str(y)+"K")
#        else:
#                y = round(int(x)/10**3,1)
#                print(str(y)+"K")
#else:
#        print(x)
#d,m,y = [int(e) for e in input().split()]
#y = y - 543
#n = 31
#if m == 4 or m==6 or m==9 or m==11 :
#        n = 30
#elif m == 2:
#        n = 28
#        if y%400 == 0:
#                n = 29
#        elif y%4 == 0 and y%100 != 0:
#                n = 29
#d = d+15
#if d>n :
#        d = d - n
#        m = m + 1
#if m>12 :
#        m = m - 12
#        y = y + 1
#y = y + 543
#print(str(d)+"/"+str(m)+"/"+str(y))
#a,b,c,d = [int(e) for e in input().split()]
#if a > b :
#        a,b = b,a
#        if d >= a :
#                if c > d :
#                        c = c - a
#        else : c = c+a
#        b = a + c + d
#else :
#        if c > a >= b :
#                d = d + a
#        if d > c :
#                b = b + 2
#        else : b = 2*b
#print(a,b,c,d)
#import math
#bd, bm, by, d, m, y, = [int(e) for e in input().split()]
#by -= 543
#y -= 543
#amt = 0
#year365 = [31,28,31,30,31,30,31,31,30,31,30,31]
#year366 = [31,29,31,30,31,30,31,31,30,31,30,31]
#if (by%4 == 0 and by%100 != 0 or by%400 == 0) :
#     r = year366[bm-1]-bd+1+sum(year366[bm:])
#     gap = (y-by-1)*365
#else :
#     r = year365[bm-1]-bd+1+sum(year365[bm:])
#     gap = (y-by-1)*365
#if (y%4 == 0 and y%100 != 0 or y%400 == 0) :
#     b = sum(year366[0:m-1])+d-1
#else :
#     b = sum(year365[0:m-1])+d-1
#print(r,gap,b)
#amt = r + gap + b
#physical = math.sin(2*math.pi*amt/23)
#emotional = math.sin(2*math.pi*amt/28)
#intellect = math.sin(2*math.pi*amt/33)
#print(amt,"{:.2f}".format(physical),"{:.2f}".format(emotional),"{:.2f}".format(intellect))
#sum = 0
#arr = []
#if 
#while True : 
#     num = input()
#     if num == "q" :
#          break
#     arr.append(num)
#for i in range(0,len(arr)) :
#     sum += float(arr[i])
#avg = round(sum/len(arr),2)
#print(avg)
#key = input()
#ans = input()
#count = 0
#if len(key) != len(ans) :
#     print("Incomplete answer")
#else :
#     for i in range(0,len(key)) :
#          if key[i] == ans[i] :
#               count += 1
#     print(count)
#key = input()
#s = input()
#r = ""
#for ch in s :
#  if ch not in "),('[].\"":
#    r += ch
#arr = r.split()
#count = 0
#for i in arr :
#  if i == key :
#    count += 1
#print(count)
#s = int(input())
#h = 0
#while h < s :
#     h += 1
#     print(h*"*")
#     if h > 1 :
#          print("*"+(h-1)*" "+"*")
#     if h+1 == s :
#          print((2*s-1)*"*")
#n = int(input())
#y = n*[0]
#for i in range(n) :
#     x[i],y[i] = [int(e) for e in input().split()]
#r = n*[0]
#b = n*[0]
#blue list
#for i in range(len(b)) :
#     if i%2 == 0 :
#          b[i] = y[i]
#     else :
#          b[i] = x[i]
#red list
#for i in range(len(r)) :
#     if i%2 != 0 :
#          r[i] = y[i]
#     else :
#          r[i] = x[i]
#print(b,r)
#cmd = input()
#if cmd == "Zig-Zag" :
#     print(min(r),max(b))
#else :
#     print(min(b),max(r))
#s = list(input())
#a = s[0]
#count = 0
#for i in range(len(s)) :
#     if s[i] == a :
#          count += 1
#     else :
#          print(a,count, end = " ")
#          a = s[i]
#          count = 1
#print(a,count)
#h = int(input())
#step = 1
#count = 2
#print((h-1)*" " + "*" +(h-1)*" ")
#while count != h :
#     print((h-step-1)*" "+ "*" + (2*step-1)*" " + "*" + (h-step-1)*" ")
#     count += 1
#     step += 1
#print((2*h-1)*"*")
#s = input()
#n = ["0","1","2","3","4","5","6","7","8","9"]
#for i in range(len(n)):
#     if n[i] in s :
#          n[i] = ""
#for i in range(len(n)) :
#     if "" in n :
#          n.remove("")
#if n != [] :
#     print(",".join(n))
#else :
#     print("None")
#n = int(input())
#s = n*[0]
#fullname = ["Robert","Williams","James","John","Magaret","Edward","Sarah","Andrew","Anthony","Deborah"]
#nickname = ["Dick","Bill","Jim","Jack","Peggy","Ed","Sally","Andy","Tony","Debbie"]
#for i in range(len(s)) :
#     s[i] = input()
#for i in range(len(s)) :
#     if s[i] in fullname :
#          print(nickname[fullname.index(s[i])])
#     elif s[i] in nickname :
#          print(fullname[nickname.index(s[i])])
#     else :
#          print("Not found")
#x = [int(e) for e in input().split()]
#count = 0
#for i in range(len(x)-1) :
#     if x[i-1] < x[i] and x[i] > x[i+1] :
#          count += 1
#print(count)
#######################
#first set

def binarysum(a, b) :
    a = int(a,2)
    b = int(b,2)
    sum = bin(a+b)
    return sum

x = [str(e) for e in input().split()]
print(binarysum(x[0], x[1]))

