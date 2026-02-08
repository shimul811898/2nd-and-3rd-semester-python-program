Sdef fectorial(n):
    if n==0:
        return 1
    else:
        return n*fectorial(n-1)
n=int(input("Enter a positive number:"))
if n<0:
        print("You entered a negitive number so try again!")
        exit(0)
else:
     print("The fectorial of",n,"is",fectorial(n))