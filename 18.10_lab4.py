"""
1. Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną metodę is_passed, która zwraca wartość
logiczną, pozytywną gdy średnia ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy stworzyć 2 przykładowe
obiekty klasy, tak aby dla pierwszego obiektu metoda zwracała true , a dla drugiego false .
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def is_passed(self):
        if (sum(self.marks)/len(self.marks) > 50):
            return True
        else:
            return False

Student1 = Student('Jan Kowalski', [40,55,30,20,80])
Student2 = Student('Adam Nowak', [90,75,66,80,100])
Student3 = Student('Anna Kamińska', [80, 90, 85, 70, 95])

print(Student1.is_passed())
print(Student2.is_passed())

"""
Zadanie 2. Stworzyć następujące klasy:
-> Library (klasa opisująca bibliotekę), posiadająca pola:

city
street
zip_code
open_hours (str)
phone

-> Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
first_name
last_name
hire_date
birth_date
city
street
zip_code
phone

-> Book (klasa opisująca książkę), posiadająca pola:
library
publication_date
author_name
author_surname
number_of_pages

-> Order (klasa opisująca zamówienie), posiadająca pola:
employee
student
books (lista obiektów klasy Book)
order_date

Dodatkowo:

Każda klasa ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt oraz ewentualne obiekty
znajdujące się w tym obiekcie (np. obiekt Library w obiekcie Book).

Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem
konstruktora.

Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 3 pracowników, 3 studentów, oraz 2 zamówienia.
Wyświetlić oba zamówienia ( print )
"""

class Library:
    def __init__(self, city_street, zip_code, open_hours, phone):
        self.city_street = city_street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
        pass
    def __str__(self):
        return f'city: {self.city} street: {self.street} zip code: {self.zip_code} open hours: {self.open_hours} phone: {self.phone}'

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street ,zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
        pass
    def __str__(self):
        return f'first name: {self.first_name} last name: {self.last_name} hire date: {self.hire_date} birth date: {self.birth_date} city: {self.city} street: {self.street} zip code: {self.zip_code} phone: {self.phone}'

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
        pass
    def __str__(self):
        return f'library: {self.library.__str__()}\npublication date: {self.publication_date} author name: {self.author_name} author surname: {self.author_surname} number of pages:{self.number_of_pages}'

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
        pass
    def __str__(self):
        return f'employee: {self.employee.__str__()}\nstudent: {self.student.__str__()}\nbooks:\n{nl_char.join(map(str, [str(index)+": "+book.__str__() for index, book in enumerate(self.books)]))}'
    
Library1 = ['Miejska Biblioteka Publiczna. Filia 1', 'Katowice ul. Ligonia 7', '40-036', '8:00 - 19:00', '32 251 30 47']
Library2 = ['Miejska Biblioteka Publiczna. Filia 24', 'Katowice al. Rozdzieńskiego 88A', '40-227', '8:00 - 15:00', '32 203 58 99']

Book1 = [Library1[0], '3.10.2011', 'autor1', 'autor1', '300']
Book2 = [Library2[0], '25.02.2002', 'autor2', 'autor2', '500']
Book3 = [Library1[0], '1.01.2000', 'autor3', 'autor3', '400']
Book4 = [Library2[0], '6.06.2010', 'autor4', 'autor4', '600']
Book5 = [Library1[0], '10.05.2015', 'autor5', 'autor5', '500']

Employee1 = ['Employee', '1', '1.03.2016', '1.01.1970', 'miasto1', 'ulica1', 'kod1', 'telefon1']
Employee1 = ['Employee', '2', '1.03.2016', '1.01.1970', 'miasto2', 'ulica2', 'kod2', 'telefon2']
Employee1 = ['Employee', '3', '1.03.2016', '1.01.1970', 'miasto3', 'ulica3', 'kod3', 'telefon3']

class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks
  def __str__(self):
      return f'name: {self.name} marks: {self.marks}'
  
student1 = Student('Michał', [88, 76, 94, 33])
student2 = Student('Jakub', [22, 91, 50, 64])
student3 = Student('Kamil', [50, 46, 100, 94])

order1 = Order(employee1, student2, [book1, book2, book4], '29-07-2021')
order2 = Order(employee3, student1, [book5, book4, book3], '11-07-2019')

print(order1.__str__())
print("\n")
print(order2.__str__())

"""
Zad.3
3. Stworzyć następujące klasy:
Property (klasa opisująca posiadłość/nieruchomość), posiadająca pola:
area
rooms (int)
price
address
House (klasa dziedzicząca klasę Property , która opisuje dom), posiadająca pola:
plot (rozmiar działki, int)
Flat (klasa dziedzicząca klasę Property , która opisuje mieszkanie), posiadająca pola:
floor
Dodatkowo:
Każda z klas dziedziczących ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt.
Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem
konstruktora.
Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je wyświetlić.
"""

class Property:
    def __init__(self, area, rooms: int, price, address):
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address
    @property
    def area(self):
        return self._area
    @property
    def rooms(self):
        return self._rooms
    @property
    def price(self):
        return self._price
    @property 
    def address(self):
        return self._address
    @area.setter
    def area(self, value):
        self._area = value
    @rooms.setter
    def rooms(self, value):
        self._rooms = value
    @price.setter
    def price(self, value):
        self._price = value
    @address.setter
    def address(self, value):
        self._address = value
    def __str__(self) -> str:
        return f'Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}, Address: {self.address}'

class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self._plot = plot
    @property
    def plot(self) -> int:
        return self._plot
    @plot.setter
    def plot(self, plot: int):
        self._plot = plot
    def __str__(self) -> str:
        return super().__str__() + f', Plot: {self.plot}'

class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self._floor = floor
    @property
    def floor(self) -> None:
        return self._floor
    @floor.setter
    def plot(self, floor):
        self._floor = floor
    def __str__(self) -> str:
        return super().__str__() + f', Floor: {self.floor}'
    
house1 = House(100, 5, 123999.25, 'ul. Jakaś', 120)
flat1 = Flat(125, 4, 200010.00, 'ul. Druga', 1)

print("House: "+ house1.__str__())
print("Flat: "+ flat1.__str__())