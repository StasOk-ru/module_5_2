# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".
#
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
#
# Пример результата выполнения программы:
# Пример выполняемого кода:
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# # __str__
# print(h1)
# print(h2)
#
# # __len__
# print(len(h1))
# print(len(h2))
#
# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# 10
# 20

class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floors:
            print("Такого этажа не существует",'\n')
        else:
            for i in range(1, new_floor + 1):
                print(i)
            print("Приехали",'\n')

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'

    def __len__(self):
        return self.floors

'''h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Зарядье', 9)
h1.go_to(5)
h2.go_to(10)
h3.go_to(7)

h3.info()'''

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print()

print(h1)
print(h2)
# print(str(h2)) рабочий код в чем разница с print(h2)?

print()

print(len(h1))
print(len(h2))
