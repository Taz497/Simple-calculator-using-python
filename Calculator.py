#Made by Tazim
#5/10/2022 11:05

#Asks for first number
number1 = int(input("Number: "))

#Prints info
print("A for addition S for substraction M for multiplication D for division")  

#Asks for thier choice
user = input("User: ")

#Then asks for second number
number2 = int(input("Number: "))
 
#Addition, Substraction, Multiplication and Division 
def addition():
    print(number1 + number2)
   
def substraction():
    print(number1 - number2)

def multiplication():
     print(number1 * number2)    

def division():
     print(number1 / number2)

#Main logic
def calculator():
    if user.upper() == "A":
        addition()  
    elif user.upper() == "S":
        substraction()
    elif user.upper() == "M":
        multiplication()    
    elif user.upper() == "D":
        division()
    else:
        print("Invalid input!")

calculator()                  