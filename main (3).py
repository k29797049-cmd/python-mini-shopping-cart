print("======MINI SHOPPING CART======")
name=input("Enter your name")
products=["T-Shirt","Jeans","Shoes","Watch"]
prices=(699,899,1499,1699)
print("\nAvailable Products:")
print("1.", products[0], "- ₹", prices[0])
print("2.", products[1], "- ₹", prices[1])
print("3.", products[2], "- ₹", prices[2])
print("4.", products[3], "- ₹", prices[3])

choice = int(input("\nChoose product number (1-4): "))
quantity = int(input("Enter quantity: "))

product_name = products[choice - 1]
price = prices[choice - 1]

total = price * quantity

print("\n====== BILL ======")
print("Customer:", name)
print("Product:", product_name)
print("Price: ₹", price)
print("Quantity:", quantity)
print("Total: ₹", total)

print("\nThank you for shopping,", name + "!")