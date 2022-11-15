"""
A) Utwórz funkcję która otrzyma w parametrze listę 5 imion, a następnie wyświetli każde z nich
"""

imiona = {"Lukasz", "Kuba", "Julia", "Michal", "Zuza"}
print(imiona)

"""
B) Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych
liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci. Zadanie
należy wykonać w 2 wersjach:
1. Wykorzystując pętle for .
2. Wykorzystując listę składaną.
"""
#pętla for

lista = [1, 2, 3, 4, 5]
listaPomnożonaPrzezDwa = []
for element in lista:
    listaPomnożonaPrzezDwa.append(element*2)
print(listaPomnożonaPrzezDwa)

#comprehension list

listaPomnożonaPrzezDwa = [element*2 for element in lista]
print(listaPomnożonaPrzezDwa)

"""
C) Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane
wykorzystanie funkcji range ), a następnie wyświetli jedynie parzyste elementy.
"""
firstTenNumbers = []
def first_10_numbers():
    for number in range(10):
        if (number % 2 == 0):
            firstTenNumbers.append(number)
    return firstTenNumbers
print(first_10_numbers())

"""
D) Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane
wykorzystanie funkcji range ), a następnie wyświetli co drugi element.
"""

list = [1,3,5,7,9,11,13,15,17,19,21]
def every_second_number(list):
    return list[::2]

print(every_second_number(list))
        
            
