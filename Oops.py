class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        return (self.a+self.b+self.c)
t=Triangle(10,20,30)
print(t.perimeter())