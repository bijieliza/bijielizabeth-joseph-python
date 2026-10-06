#variables and types
name = "Alex"
age = 27
height = 5.9
is_student = True
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Hi, Jordan! You are approximately 24 years old.
#User input and Math
Name=input("Name")
doy=int(input("Birthyear"))
ty=datetime.date.today().year
age=str(ty-doy)
print (f"Hi, {Name}! You are approximately {age} years old.")

#Type Conversion and f-strings
number1=float(input("Enter number1"))
number2=float(input("Enter number2"))
result=number1 * number2
print(f"{number1:.2f} * {number2:.2f} = {result:.2f}")

#Formatted Receipt
Item="Python textbook"
Price=float("29.99")
Quantity=int("2")  
Total=Price * Quantity
print("===========================")
print("           Receipt")
print("===========================")
print(f"Item:       {Item}")
print(f"Price:      ${Price}")
print(f"Quantity:   {Quantity}")
print("---------------------------")
print("Total:       $"+ str(Total) )
print("===========================")

#Profile Card
import datetime
#name= input("Name")
htown=input("Hometown")
hobby=input("Hobby") 
ffact=input("Fun fact")
text = f"PROFILE: {Name}"
width = len(text) + 8
print("\u2554" + "═" * width + "\u2557")
print("    " + text)
print("\u255A" + "═" * width + "\u255D")
print(f"Hometown:",htown)
print("Hobby:",hobby)
print("Fun fact:",ffact)
print("Age:",age)

