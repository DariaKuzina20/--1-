import math

P = 0
S = 0
print("Координаты вершины A")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
print("Координаты вершины B")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
print("Координаты вершины C")
x3 = float(input("x3 = "))
y3 = float(input("y3 = "))
AB=math.sqrt(abs((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1)))
BC=math.sqrt(abs((y3-y2)*(y3-y2)+(x3-x2)*(x3-x2)))
CA=math.sqrt(abs((y1-y3)*(y1-y3)+(x1-x3)*(x1-x3)))
if AB + BC > CA and AB + CA > BC and BC + CA> AB:
    P = AB+BC+CA
    S = math.sqrt((P/2)*((P/2)-AB)*((P/2)-BC)*((P/2)-CA))
    print("Периметр: P = ", P)
    print("Площадь: S = ", S)
else:
    print ("Треугольника не существует")

#(x1, y1); (x2, y2);(x3, y3) - Координаты вершин треугольника
#AB, BC, CA - стороны треугольника
#S - площадь треугольника
#P - периметр треугольника
