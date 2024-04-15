"""
In the calculatePrice(100, 0.07, 0.05) function call, we pass each argument as a positional argument. In other words, we pass the price argument first and the discount argument second.
However, the function call calculatePrice(100, 0.07, 0.05) has a readability issue. Because by looking at that function call only, you don’t know which argument is price and which one is the discount.
On top of that, when you call the calculatePrice() function, you need to know the position of each argument.
"""

def calculatePrice(price: any, tax: any, discount: any):
    print(price * (1 + tax - discount))

calculatePrice(discount=0.05, price=100, tax=0.07)