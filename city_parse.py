# -*- coding: utf-8 -*-
from time import time

# province of china
class Province:
	def __init__(self, code, name):
		self.code = code
		self.name = name
		self.sub = []

	def __repr__(self):
		return '''{"code":%r ,"name": %r, "sub":%r}\n''' % (self.code, self.name, self.sub)

	def consist(self, city):
		self.sub.append(city)

# city of province
class City:
	def __init__(self, code, name):
		self.code = code
		self.name = name
		self.sub = []

	def __repr__(self):
		return '''{"code":%r ,"name": %r, "sub":%r}\n''' % (self.code, self.name, self.sub)

	def consist(self, country):
		self.sub.append(country)

# coutry of city
class Country:
	def __init__(self, code, name):
		self.code = code
		self.name = name

	def __repr__(self):
		return '''{"code":%r, "name": %r}\n''' % (self.code, self.name)

# judge the type by code
def zero(n):
	i = 1
	if n <= 0:
		return 0
	while n % i == 0:
		i *= 10
	return i/10

def get_data(filename):
	arr = []
	# open the city.txt
	with open(filename, "r", encoding="utf-8") as read:
		print("file has been open.")
		for line in read:
			arr.append(line.strip())
	print("reading finished")
	return arr


if __name__ == "__main__":

	t1 = time()
	# initial
	province = Province("","")
	city = City("","")
	country = Country("","")

	# data of city.txt
	array = get_data('city.txt')

	# open the file to be outputing
	with open("city.json", "a+") as output:

		print("start writing to the file")

		for element in array:
			# parse the city data, output code and name
			tmp = element.replace(" ","").strip("\u3000") # remove blank
			code = tmp[:6]
			name = tmp[6:].strip("\u3000")
			# while a province data finished, output it
			if zero(int(code)) == 10000:
				if province.code:
					# follow the format of json
					print(str(province).replace("\'", "\""), file = output)
				province = Province(code, name)
			elif zero(int(code)) == 100:
				city = City(code, name)
				# add the city data to the province
				province.consist(city)
			else:
				country = Country(code, name)
				# add the country data to the city
				city.consist(country)
		output.close()

	t2 = time()
	t = t2 - t1
	print("finished. cost %.3f seconds." % t )

