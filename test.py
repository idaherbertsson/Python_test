class Product:
	price = 0
	count = 0
	tax = 1.25

	def price_incl_tax(self):
		return(self.price * self.tax)


robot = Product()
robot.price = 900
robot.count = 2

book = Product()
book.price = 100
book.count = 1
book.tax = 1.06


print(robot.price_incl_tax()*robot.count +book.price_incl_tax()*book.count)


