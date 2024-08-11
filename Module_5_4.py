class House:
	houses_history = []

	def __new__(cls, *args, **kwargs):
		args = args[0]
		cls.houses_history.append(args)
		return super().__new__(cls)

	def __init__(self, name, number_of_floors):
		self.name = name
		self.number_of_floors = number_of_floors

	def __len__(self):
		return self.number_of_floors

	def __str__(self):
		return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

	def go_to(self, new_floor):
		for i in range(1, new_floor + 1):
			print(i)
		if self.number_of_floors - new_floor < 0 or new_floor < 1:
			print("Такого этажа не существует")
		print()  #Добавленно для разделения 1 и 2 вызова

	def __eq__(self, other):
		return self.number_of_floors == other

	def __lt__(self, other):
		return self.number_of_floors < other.number_of_floors

	def __le__(self, other):
		return self.number_of_floors <= other.number_of_floors

	def __gt__(self, other):
		return self.number_of_floors > other.number_of_floors

	def __ge__(self, other):
		return self.number_of_floors >= other.number_of_floors

	def __ne__(self, other):
		return self.number_of_floors != other.number_of_floors

	def __add__(self, value):
		self.number_of_floors = self.number_of_floors + value
		return self

	def __radd__(self, value):
		self.number_of_floors = self.number_of_floors + value
		return self

	def __iadd__(self, value):
		self.number_of_floors = self.number_of_floors + value
		return self

	def __del__(self):
		print(f'{self.name} снесён, но он останется в истории')


h1 = House(input(), int(input()))
print(House.houses_history)
h2 = House(input(), int(input()))
print(House.houses_history)
h3 = House(input(), int(input()))
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

