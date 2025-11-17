import math
print("This it the Program to demonstrate max and min methods")
number1=int(input("Enter the value of first number: "))
number2=int(input("Enter the value of second number: "))
maximum=max(number1,number2)
print("The maximum number is {}".format(maximum))
minimum=min(number1,number2)
print("The minimum value is {}".format(minimum))




##### area of 2d figures


print("Hello there, I can count the area of any 2D figures.")
print('')
print("To find the value of triangle press 1")
print("To find the value of rectangle press 2")
print("To find the value of a square press 3")
print("To find the value of a circle press 4")
print("To find the value of the semicircle press 5")
print("To find the value of a parallelogram press 6")
print("To find the value of a rhombus press 7")
print("To find the value of a trapezium press 8")
print("To find the value of a kite press 9")
print('')
a=input()
if a =='1':
    length=int(input("Please enter the value of length. "))
    breadth=int(input("Please enter the value of breadth. "))
    triangle=(1/2*(length * breadth))
    print("The area of the triangle is {}".format(triangle))
elif a =='2':
    length=int(input("Please enter the value of length. "))
    breadth=int(input("Please enter the value of breadth. "))
    rectangle=(length * breadth)
    print("The area of the rectangle is {}".format(rectangle))
elif a =='3':
    side=int(input("Please enter the value of  the side. "))
    square=(side * side)
    print("The area of the square is {}".format(square))
elif a =='4':
    radii=int(input("Please enter the value of the radius. "))
    circle=(3.14 * radii * radii)
    print("The area of the circle is {}".format(circle))
elif a =='5':
    radii=int(input("Please enter the value of the radius. "))
    semicircle=(1/2 * (3.14 * radii))
    print("The area of the semicircle is {}".format(semicircle))
elif a =='6':
    base=int(input("Please enter the value of the base."))
    height=int(input("Please enter the value of height."))
    parallelogram=(base * height)
    print("The area of the parallelogram is {}".format(parallelogram))
elif a =='7':
    diagonal1=int(input("Please enter the value of diagonal1."))
    diagonal2=int(input("Please enter the value for diagonal2."))
    rhobus=(diagonal1 * diagonal2)/2
    print("The area of the rhobus is {}".format(rhobus))
elif a=='8':
    base1=int(input("Please enter the value of base1. "))
    base2=int(input("Please enter the value of base2."))
    height=int(input("Please enter the value of the height"))
    trapezium= 1/2 * (base1 + base2)* height
    print("The area of the trapezium is {}".format(trapezium))
else:
    diagonal1=int(input("Please enter the value for diagonal1."))
    diagonal2=int(input("Please enter the value of diagonal2."))
    kite=(diagonal1 * diagonal2)/ 2
    print("The area of the kite is {}".format(kite))






### additional


import math



print(round(15))




print(round(51.6))
print(round(51.5))
print(round(51.4))





r=4
pie =math.pi

print(pie * r * r)


r=int(input("enter radius"))
p=math.pi

area=4*p*r*r
print("The surface area of sphere is ", area)
area=math.ceil(area)
print("surface area of sphere is ",area)

a=5
print("The factorial of 5 is ", end="")
print(math.factorial(a))

x =min(5, 10, 25)
y =max(5, 10, 25)

print(x)
print(y)


x =pow(4,3)

print(x)
