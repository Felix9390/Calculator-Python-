# Calculator

name = "Calculator"
print(name.upper())

num1 = input("Insert a number")
variable = input("+,-,*,/")
num2 = input("Insert a number")

addition = float(num1) + float(num2)
subtraction = float(num1) - float(num2)
multiplication = float(num1) * float(num2)
division = float(num1) / float(num2)

if variable == '+':
    print("Answer: " + str(addition))
    
elif variable == '-':
      print("Answer: " + str(subtraction))
      
elif variable == '*':
      print("Answer: " + str(multiplication))
      
elif variable == '/':
      print("Answer: " + str(division))
      

else:
    print("Error: Invaild Input")
      
