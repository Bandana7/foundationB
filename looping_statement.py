brand_name, model_name, price = input("Please input your laptop details(brand_name,model_name,price):").split(",")
def laptop_info(brand,model,price):
    return f"{brand} {model} @ Rs. {price}"
print(laptop_info(brand_name,model_name,price))



apples=input("Please provide the number of apples:")
plates=input("Please prodive the number of plates:")
print(f"The sum of apple and plate={int(apples)+int(plates)}")
print(type(apples))



#creation of addition function
def addition(num1,num2):
    sum = num1+num2
    return sum
#calling addition function
print(f"the sum of apples and plates: {addition(int(apples),int(plates))}")

##ask an info of your laptop and a function should return like this: 
"""
Brand_Name model_Name available_at price
Ex: DEll Vostro @Rs 85000
"""

brand_name, model_name, price = input("Please input your laptop details(brand_name,model_name,price):").split(",")
def laptop_info(brand,model,price):
    return "{brand} {model} @ Rs. {price}"
print(laptop_info(brand_name,model_name,price))


