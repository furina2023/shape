# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online

def xysort(lst):
    for i in range(1, len(lst)):
        for j in range(0, len(lst)-i):
            A=lst[j].split(",")
            B=lst[j+1].split(",")
            if int(A[0]) > int(B[0]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
def delList(L):
    L1 = []
    for i in L:
        if i not in L1:
            L1.append(i)
    return L1

def line(P1,P2,lst):
    P=""
    p1=P1.split(",")
    p2=P2.split(",")
    x1=int(p1[0])
    x2=int(p2[0])
    y1=int(p1[1])
    y2=int(p2[1])
    x=x1
    y=y1
    if abs(int(x1)-int(x2))>abs(int(y1)-int(y2)):
        while not(x==x2):
            x+=1
            y=y+(y2-y1)/(x2-x1)
            P=str(x)+","+str(int(y))
            lst.append(P)
    else:
        while not(y==y2):
            y+=1
            x=x+(x2-x1)/(y2-y1)
            P=str(int(x))+","+str(y)
            lst.append(P)
canvas=[]
point=[]

line("0,0","24,24",point)
line("20,10","0,24",point)

T=int(input("please enter the amount of points"))
for j in range(T):
    point.append(input("please enter a point"))
point=delList(point)
point=xysort(point) 
for y in range(25):
    P=""
    k=0
    for i in point:
        x=i.split(",")
        if int(x[1])==y:
            P=P+". "*(int(x[0])-k-1)+"0 "
            k=int(x[0])
    P=". "+P+". "*(25-k)
    canvas.append(P)        
for i in canvas:
    print(i)      