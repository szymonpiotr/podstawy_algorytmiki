# Sortowanie

# 1a. Zdefinuj funkcję, która sortuje listę liczb - użyj rekurencji. Jeśli jest to potrzebne
# zdefiniuj funkcje pomocnicze. 
def recurSortt(list):
    if list == []:
        return []
    else:
        pivot = random.choice(list)
        smaller = [i for i in list if i < pivot]
        larger = [i for i in list if i > pivot]
        return recurSortt(smaller) + [pivot] + recurSortt(larger)
# 1b. Zdefinuj funkcję, które sortuje listę liczb - użyj iteracji.
def iterSort(list):
    for step in range(1, len(list)):
        key = list[step]
        j = step - 1      
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = key
    return list

# 2. Zdefiniuj funkcję, która wstawi daną liczbę w odpowiednie miejsce posortowanej listy - użyj rekurencji.

# 3a. Zdefiniuj funkcję, która sprawdzi ile razy dany element występuje na danej liście - użyj rekurencji.
# 3b. Zdefiniuj funkcję, która sprawdzi ile razy dany element występuje na danej liście - użyj iteracji.

# 4. Trójkąt Pacala. Zdefinuj funkcję, która dostaje dwa argumenty: numer kolumny i numer wiersza, zwraca zaś 
# liczbą Pascala która na danej współrzędnej występuje. 
# Działanie:
# pacal(3,1) = 3 (3 jest liczbą pascala występującą w 3 wierszu 1 kolumny)
# pascal(5,3) = 10 (10 jest liczbą pascala występującą w 5 wierszu 3 kolmuny)

# 5. Zdefiniuj funkcję "balance", która sprawdza, czy w danym Stringu nawiasy są ustawione w 
# prawidłowy sposób, tj. czy każde lewy nawias ma swój prawy nawias do pary i czy są one dobrze ustawione.
# Użyj rekurencji ogonowej.


