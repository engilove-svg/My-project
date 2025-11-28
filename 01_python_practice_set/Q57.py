#give a dictionary of products and their prices. Find the product with the highest price.
products={}
n=int(input("how many products do you want to add:\n"))
for i in range(n):
    name= (input("enter the product name:\n"))
    price= (float(input("enter the price of a product:\n")))
    products[name]=price
highest_price=max(products,key=products.get)
print("products and prices\n",products)
print("product of highest price\n",highest_price)
print("highest price of product\n",products[highest_price])
            