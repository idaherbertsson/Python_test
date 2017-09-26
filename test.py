class Product:
	
	def __init__(self, name, price, count, tax):
		self.price = price
		self.count = count
		self.tax = tax
		self.name = name
		

	def price_incl_tax(self):
		total=self.price * self.count * self.tax
		if total > 500:
			return 0.9*total
		else:
			return total 


products = [
Product (name = "Robot", price=900, count=2, tax= 1.25), 
Product(name= "Book", price=100, count=1, tax=1.06), 
Product (name = "Freight", price = 470, count = 1, tax=1.12)
]

total_price = 0

for product in products:
	total_price = total_price + product.price_incl_tax()


for product in products:
	print ("Produkt: {:8} Antal: {}st  Pris: {:>7} kr".format(product.name, product.count, round(product.price_incl_tax(),0)))

print("-"*80)

print ("Total summa: {:>29} kr".format(round(total_price, 0)))