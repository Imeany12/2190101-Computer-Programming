
def distance1(x1,y1,x2,y2):
    d = ((x1-x2)**2+(y1-y2)**2)**0.5
    return d
def distance2(p1,p2):
    d = (((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))**0.5
    return d
def distance3(c1,c2):
    dc = (((c1[0]-c2[0])**2)+((c1[1]-c2[1])**2))**0.5
    
    if dc>(c1[2]+c2[2]):
        overlap = False
    else:
        overlap = True
    return dc,overlap
def perimeter(points):
    d = []
    for k in range(len(points)):
        l = distance2(points[k],points[k-1])
        d.append(l)
        s = sum(d)
    return s


exec(input().strip())
