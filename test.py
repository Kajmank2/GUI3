'''
import math
def circle(x1, y1, x2, y2, r1, r2):
    distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    radSumSq = (r1 + r2) * (r1 + r2)
    if (distSq == radSumSq):
        return 1
    elif (distSq > radSumSq):
        return -1
    else:
        return 0
def is_circle_collision(circle1, circle2):
   x1, y1, r1 = circle1
   x2, y2, r2 = circle2
   distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
   return distance <= r1 + r2
print(is_circle_collision([90,90,35],[85,20,35]))
print(circle(90,90,85,20,35,35))
intersects = math.hypot(90-85, 90-20) <= (35 + 35)
print(intersects)
'''
List=[1,2,3]
PreList=[4,5,6]
List=PreList
print(List)