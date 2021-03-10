class student:
    "common base class for all students"
    def __init__(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def display(self):
        print("Rollno:",self.rollno)
        print("Name:",self.name)
        print("Course:",self.course)
    def __del__(self):
        print("object deleted")
student1=student(10,"Jack","MCA")
student1.display()
del student1



