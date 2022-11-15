"""
1. Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie go
wyświetlić (print)
"""

name = "Lukasz"
surname = "Lewicki"

def name_and_surname(name, surname):
    return str(f"Czesc {name} {surname}!")
print(name_and_surname(name, surname))

"""
2. Stworzyć funkcję, która przyjmie 2 argumenty typu int , a następnie zwróci wynik
mnożenia obu liczb.    
"""

x = 10
y = 20

def multiplied_numbers_by_themself(x, y):
    return x * y
print(multiplied_numbers_by_themself(x, y))

"""
3. Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest
parzysta i zwróci tą informację jako typ logiczny bool ( True / False ). Należy
uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie
wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" /
"Liczba nieparzysta"
"""
number_given = 10

def is_even(x):
    return (number_given % 2 == 0)

def is_number_even_or_odd(number_given) -> bool:
    if (number_given % 2 == 0):
        return "Liczba parzysta"
    else:
        return "Liczba nieparzysta"

print(is_number_even_or_odd(number_given))
"""
4. Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch
pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację
jako typ logiczny bool
"""

x = 10
y = 50
z = 100

def is_sum_of_x_and_y_greater_than_z(x, y, z) -> bool:
    if ((x + y) > z):
        return "True"
    else:
        return "False"

print(is_sum_of_x_and_y_greater_than_z(x, y, z))

"""
5. Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi typu int. 
Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z parametru
pierwszego zawiera taką wartość jaką przekazano w parametrze drugim.
"""   

list = [1, 2, 3, 4, 5]
a = 5

def is_a_inside_list(list, a) -> bool:
    if a in list:
        return "Element a exists in a list"
    else:
        return "Element a doesn't exist in a list"
        
print(is_a_inside_list(list, a))

"""
6. Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list .
Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty, każdy
element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.  
"""
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8,10,12,14,16,18,20]

def joining_lists(list1, list2):
    list3 = list1 + list2
    list3 = dict(dict.fromkeys(list3))
    list3 = [element**3 for element in list3]
    return list3
print(joining_lists(list1, list2))