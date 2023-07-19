# HW01 (Don't delete this line or add any line above this line.)

frames = [float(x) for x in input().strip("\'").split()]

# write your program under this line
import math
d = []
while True:
  i = input()
  if i != "end":
    b = i.split()
    if b[0] == "center":
      x,y,w,h = [frames[(int(b[1])-1)*4+t] for t in range(4)]
      print("("+str((w/2)+x)+", "+str(y-(h/2))+")")
    elif b[0] == "distance":
      x1 = frames[(int(b[1])-1)*4]
      y1 = frames[(int(b[1])-1)*4+1]
      w1 = frames[(int(b[1])-1)*4+2]
      h1 = frames[(int(b[1])-1)*4+3]
      x2 = frames[(int(b[2])-1)*4]
      y2 = frames[(int(b[2])-1)*4+1]
      w2 = frames[(int(b[2])-1)*4+2]
      h2 = frames[(int(b[2])-1)*4+3]
      cx1 = (w1/2)+x1
      cy1 = y1-(h1/2)
      cx2 = (w2/2)+x2
      cy2 = y2-(h2/2)
      dx = cx1 -cx2
      dy = cy1 -cy2
      dis = math.sqrt(((dx)**2)+((dy)**2))
      print(dis)
    elif b[0] == "intersection":
      x1,y1,w1,h1 = [frames[(int(b[1])-1)*4+t] for t in range(4)]
      x2,y2,w2,h2 = [frames[(int(b[2])-1)*4+t] for t in range(4)]
      xa = max(x1,x2)
      ya = min(y1,y2)
      xb = min(x1+w1,x2+w2)
      yb = max(y1-h1,y2-h2)
      inarea = max(0,(xb-xa)*(ya-yb))
      print(float(inarea))

    elif b[0] == "union":
      x1,y1,w1,h1 = [frames[(int(b[1])-1)*4+t] for t in range(4)]
      x2,y2,w2,h2 = [frames[(int(b[2])-1)*4+t] for t in range(4)]
      ya = min(y1,y2)
      xa = max (x1,x2)
      xb = min(x1+w1,x2+w2)
      yb = max(y1-h1,y2-h2)
      inarea = max(0,(xb-xa)*(ya-yb))
      uarea = (w1*h1)+(w2*h2)-inarea
      print(float(uarea))
    elif b[0] == "iou":
      x1,y1,w1,h1 = [frames[(int(b[1])-1)*4+t] for t in range(4)]
      x2,y2,w2,h2 = [frames[(int(b[2])-1)*4+t] for t in range(4)]
      ya = min(y1,y2)
      xa = max (x1,x2)
      xb = min(x1+w1,x2+w2)
      yb = max(y1-h1,y2-h2)
      inarea = max(0,(xb-xa)*(ya-yb))
      uarea = (w1*h1)+(w2*h2)-inarea
      print(float(inarea/uarea))
  else:
    break
print("0.0")
    