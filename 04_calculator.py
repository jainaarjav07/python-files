a=int(input("Enter Your First  Number:"))
c=input("operator(+,-,*,/):")
b=int(input("Enter Your Second Number:"))
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else:
    print("Invalid Operation")
