class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def display(self):
        print("Length:",self.length)
        print("Breadth:",self.breadth)
    def area(self,length,breadth):
        print("Area:",length*breadth)
    def perimeter(self,length,breadth):
        print("Perimeter:",2*length*breadth)
    def __del__(self):
        print("Deleted Object")
rectangle1=rectangle(5,8)
rectangle1.display()
rectangle1.area(5,8)
rectangle1.perimeter(5,8)

