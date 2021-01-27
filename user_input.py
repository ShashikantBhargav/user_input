#name= input("enter your name:")

#age = int(input("enter your age:"))


#secure input
try:
    name= input("Enter your name:")
    age = int(input("Enter your age:"))

except valueerror:
    name = "unknown"
    age = "unknown"
finally:
    print(f"Name: {name}\nAge: {age}")
    
