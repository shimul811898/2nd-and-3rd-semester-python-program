import math
def triangle_area():
    a=int(input("Enter value of a:"))
    b=int(input("Enter value of b:"))
    c=int(input("Enter value of c:"))
    if (a+b)>c and (b+c)>a and (c+a)>b:
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print(area)
    else:
        print("Triangle is not possible")
    
triangle_area()