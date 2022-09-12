age = int( input("Please provide your age:"))

#conditional statement
#if block only

print("code started...")
if age>18:
    print(f"You can play this game because you are above {age}")

print("Code ended....")

#if-else block
if age>18:
    print(f"You can play this game because you are above {age}")
else:
    print("you need to be above 18 years to play this game")
    print("code ended")


## proper use of if-elif-else block

if age<0:
    print("Please input valid age")
elif 0<age<=10:
    print("Since you are a kid, your ticket price will be Rs 100.")
elif 10<age<20:
    print("Your ticket price is Rs 200")
else:
    print("Your ticket price is Rs 300")

    
