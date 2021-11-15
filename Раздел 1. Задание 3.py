import math

print("Введите координаты вершины A:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
print("Введите координаты вершины B:")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
print("Введите координаты вершины C:")
x3 = float(input("x3 = "))
y3 = float(input("y3 = "))
AB=math.sqrt(abs((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1)))
BC=math.sqrt(abs((y3-y2)*(y3-y2)+(x3-x2)*(x3-x2)))
CA=math.sqrt(abs((y1-y3)*(y1-y3)+(x1-x3)*(x1-x3)))
if AB + BC > CA and AB + CA > BC and BC + CA> AB:
    Ptr = AB+BC+CA
    ptr=Ptr/2
    Str = math.sqrt(ptr*(ptr-AB)*(ptr-BC)*(ptr-CA))
    r=math.sqrt(((ptr-AB)*(ptr-BC)*(ptr-CA))/ptr)
    C=2*3.14*r
    Socr=r*Ptr/2
    print ("Длина вписанной окружности: C = ", C)
    print ("Площадь круга: S = ", Socr)
else:
    print ("Треугольника не существует")


#(x1, y1); (x2, y2);(x3, y3) - Координаты вершин треугольника
#AB, BC, CA - стороны треугольника   
#Ptr - периметр описанного треугольника
#ptr - полупериметр описанного треугольника
#Str - площадь описанного треугольника
#C - длина вписанной окружности
#Socr - площадь круга
#r - адиус вписанной окружности
