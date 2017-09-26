class Product:
	
	def __init__(self, price, count, tax):
		self.price = price
		self.count = count
		self.tax = tax

	def price_incl_tax(self):
		return (self.price * self.count * self.tax)


products = [Product (price=900, count=2, tax= 1.25), Product(price=100, count=1, tax=1.06)]

total_price = products[0].price_incl_tax() + products[1].price_incl_tax()

print(total_price)





