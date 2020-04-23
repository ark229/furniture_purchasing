lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. brown or black.
"""
lovely_loveseat_price = 354.00

stylish_settee_description = """
Stylish Sette. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Brown or Black.
"""
stylish_settee_price = 199.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown or Black with cream shade.
"""
luxurious_lamp_price = 60.45

sales_tax = .099

customer_one_total = 0
customer_one_itemization = ""

customer_one_total = lovely_loveseat_price + stylish_settee_price
customer_one_itemization = lovely_loveseat_description + stylish_settee_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)

print("Customer One Total:")
print(customer_one_total)