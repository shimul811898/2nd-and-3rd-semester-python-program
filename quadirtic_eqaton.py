import math
class quadirtic_eqaton:

     a=int(input("Enter a value:"))
     b=int(input("Enter a value:"))
     c=int(input("Enter a value:"))

     d=b**2-4*a*c

     if d>0:
           value1=(-b+math.sqrt(d))/(2 * a)
           value2=(-b-math.sqrt(d))/(2 * a)
           print(f"first value is {value1} & second value is {value2}")
     
     elif d==0:

           value3= -b / (2*a)
           print(value3)

     else:
         print("roots are imaginary")























