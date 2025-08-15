def calculate_discount(price,discount_price):
    if discount_price>=0.2:
        return price*discount_price
    else:
        return price

price = int(input("Enter the original price of the item"))
discount=float(input("enter the discount percentage e.g 20"))
discounted = discount/100

print(f'the price of the item is {calculate_discount(price,discounted)}')