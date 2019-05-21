#EUCLIDIAN DISTANCE - between two points
#bascially, the euclidian distance is a distance between two points in a Euclidian Space. Again, the Euclidian Space is nothing but a space that is created using a Euclidian planes. 


import math
point = 2
#get the x and y values of the points
a = []

x1=input("x1 = ")
y1=input("y1 = ")


x2=input("x2 = ")
y2=input("y2 = ")

a.append(pow(x2-x1,2))
a.append(pow(y2-y1,2))

for i in range(0,3):
	a.append(i)

ans = sum(a)
solution = math.sqrt(ans)

print(solution)

