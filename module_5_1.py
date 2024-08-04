class House:
	def __init__(self, name, number_of_floors):
		self.name = name
		self.number_of_floors = number_of_floors

	def go_to(self, new_floor):
		for i in range(1, new_floor + 1):
			print(i)
		if self.number_of_floors - new_floor < 0 or new_floor < 1:
			print("Такого этажа не существует")
		print()  #Добавленно для разделения 1 и 2 вызова


h1 = House(input(), int(input()))
h2 = House(input(), int(input()))
h1.go_to(int(input()))
h2.go_to(int(input()))
