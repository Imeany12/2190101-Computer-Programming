mname = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
zs = ["Aquarius", "Pisces", 'Aries', 'Taurus', 'Gemini', 'Cancer', "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", ]
to = [1,3,5,7,8,10,12]
def read_date():
    date1 = input().split()
    d1 = int(date1[0])
    m1 = mname.index(date1[1][:3])+1
    y1 = int(date1[2])
    return [d1,m1,y1]
def zodiac(d,m):
    if d>=22 and m ==4 or d <=21 and m==5:
        return "Taurus"
    elif d>=22 and m ==3 or d <=21 and m==4:
        return "Aries"
    elif d>=22 and m ==5 or d <=21 and m==6:
        return "Gemini"
    elif d>=22 and m ==6 or d <=21 and m==7:
        return "Cancer"
    elif d>=22 and m ==7 or d <=21 and m==8:
        return "Leo"
    elif d>=22 and m ==8 or d <=21 and m==9:
        return "Virgo"
    elif d>=22 and m ==9 or d <=21 and m==10:
        return "Libra"
    elif d>=22 and m ==10 or d <=21 and m==11:
        return "Scorpio"
    elif d>=22 and m ==11 or d <=21 and m==12:
        return "Sagittarius"
    elif d>=22 and m ==12 or d <=20 and m==1:
        return "Capricorn"
    elif d>=21 and m ==1 or d <=20 and m==2:
        return "Aquarius"
    elif d>=21 and m ==2 or d <=21 and m==3:
        return "Pisces"
def days_in_feb(y):
    if y%400==0  or (y%4==0 and y%100!= 0):
        d = 29
    else:
        d = 28
    return d
def days_in_month(m,y):
    
    if m in to:
        d = 31
    elif m ==2:
        d = days_in_feb(y)
    else:
        d =30
    return d
def days_in_between(d1,m1,y1,d2,m2,y2):
    days = 0
    for x in range(1,m1+1):
        if x in to:
            days +=31
        elif x == 2:
            days += days_in_feb(y1)
        else:
            days +=30
    for x in range(1,m2+1):
        if  x in to:
            days +=31
        elif x == 2:
            days += days_in_feb(y2)
        else:
            days +=30
    days += (days_in_month(m1,y1)-d1+1)+int((y2-y1-1)*365.25)+(d2-1)
    return days
def main():
    k =[]
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    k.append(zodiac(d1,m1))
    k.append(zodiac(d2,m2))
    print(" ".join(k))
    print(days_in_between(d1,m1,y1,d2,m2,y2))
exec(input().strip())
    
 

