import math
class ArcLength():
    """This is a class ArcLength representing the attributes angle and radiu
    s"""
def read(al1):
    al1.radius=float(input("Radius:"))
    al1.angle=float(input("Angle:"))
def calculate_arc_length(al1):
    if al1.angle >= 360:
        print("Angle is not possible")
    else:
        result =(2* math.pi *al1.radius) *(al1.angle/360)
        #CALCULATING ARC FORMULA (circumference * angle/360)
        
    return result

al = ArcLength()
print("Enter radius and angle:")
read(al)
res=calculate_arc_length(al)
print("Arc Length is",res)