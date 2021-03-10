class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
a=int(input("Enter the length of rectangle1"))
b=int(input("Enter the width of rectangle1"))
obj1=rectangle(a,b)
c=int(input("Enter the length of rectangle2"))
d=int(input("Enter the width of rectangle2"))
obj2=rectangle(c,d)
area1=obj1.area()
area2=obj2.area()
if area1>area2:
    print('The area of rectangle one is: ', area1)
    print("The area of rectangle two is:",area2)
    print("Rectangle ones area is greatest")
elif area2>area1:
    print('The area of rectangle one is: ', area1)
    print("The area of rectangle two is:",area2)
    print("Rectangle twos area is greatest")
elif area1==area2:
    print('The area of rectangle one is: ', area1)
    print("The area of rectangle two is:",area2)
    print("Rectangle ones area is equal to rectangle twos area")


