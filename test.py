class Product:
	
	def __init__(self, name, price, count, tax):
		self.price = price
		self.count = count
		self.tax = tax
		self.name = "product name"
		

	def price_incl_tax(self):
		total=self.price * self.count * self.tax
		if total > 500:
			return 0.9*total
		else:
			return total 


products = [
Product (name = "robot", price=900, count=2, tax= 1.25), 
Product(name= "book", price=100, count=1, tax=1.06), 
Product (name = "freight", price = 470, count = 1, tax=1.12)
]

total_price = 0

for product in products:
	total_price = total_price + product.price_incl_tax()

print (total_price)






