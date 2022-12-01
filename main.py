# CALCULATOR CODE

print("CALCULATOR")
num1 = input("Insert first number: ")
variable = input("Insert (+, -, *, /): ")
num2 = input("Insert second number: ")

add = float(num1) + float(num2)
subtract = float(num1) - float(num2)
multiply = float(num1) * float(num2)
divide = float(num1) / float(num2)

if variable == "+":
    print (add)

elif variable == "-":
        print(subtract)

elif variable == "*":
    print(multiply)

elif variable == "/":
    print(divide)

else:
    print("Invaild input. Please try again!")
