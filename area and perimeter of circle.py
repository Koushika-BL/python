class circle():
    radius=int(input("enter the radius"))
    def area(self):
        area1=3.14*(self.radius**2)
        print(area1)
    def perimeter(self):
        perimeter1=3.14*2*self.radius
        print(perimeter1)
ob1=circle()
ob1.area()
ob1.perimeter()
