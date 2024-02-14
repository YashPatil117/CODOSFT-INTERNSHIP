print("Calulator")
while(True):

  print("\n1.Addition\n2.Subtraction\n3.Multuplication\n4.Division\n5.EXIT")
  x=int(input("ENTER YOUR CHOICE:\n"))

  if(x==1):
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    add=a+b
    print("Result:",add)
  elif(x==2):
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    sub=a-b
    print("result:",sub)
  elif(x==3):
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    mult=a*b
    print("resut:",a*b)
  elif(x==4):
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    if(b==0):
      print("division cannot be performed because denominator cannot be '0'")
    else:
      div=a/b
      print("resut:",div)
  elif(x==5):
    print("exiting Calculator")
    break
