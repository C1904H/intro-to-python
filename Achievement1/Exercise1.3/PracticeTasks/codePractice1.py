a = int(input("Enter a number(a): "))
b = int(input("Enter another number(b): "))
c = input("Enter either + or - : ")

if c == "+":
  print("The sum of these numbers is " + str(a + b))
  
elif c == "-":
    print("The sum of (a) minus (b) is " + str(a - b))

else:
  print("Unknown operator")