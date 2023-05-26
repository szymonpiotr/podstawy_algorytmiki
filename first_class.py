# Dane kontaktowe:
# Szymon Chlebowski, szymon.chlebowski@amu.edu.pl lub MsTeams chat
# Dyżury (pokój 97, budynek AB) 
# wtorek 8.30-9.30, środa 11.15-12.15 (po uprzednim umówieniu się)

# 30 punktów: kolokwium (indywidualne przy komputerze), 
# 20 punktów: indywidualne wejściówki/wyjściówki i/lub praca w małych grupach.

# kod zajęć będzie dostępny na Githubie a link będzie udostepniany na stronie:
# http://sc52172.home.amu.edu.pl/

# Temat pierwszych zajęć: 
# - rozgrzewka;
# - rekurenjca, rekurencja ogonowa, iteracja

# 1a. Zdefiniuj funkcję silnia, używając standardowej rekurencji.
def factorial_rec(n):
    if n==0:
        return 1
    else:  
        return n * factorial_rec(n-1)
# 1b. Zdefiniuj funkcję silnia, używając rekurencji ogonowej.
def factorial_tail(n, temp):
    if n==0:
        return temp
    else:
        return factorial_tail(n-1, n*temp)
# 1c. Zdefiniuj funkcję silnia, używając iteracji (pętli).
def factorial_iter(n):
    if n==0:
        return 1
    else:
        wynik = 1
        for i in range(1,n+1):
            wynik = wynik * i 
        return wynik

# 2a. Zdefiniuj funkcję zwracającą największy element w liście - wersja iteracyjna.
def maximum_iter(list):
    max = list[0]
    for x in list:
        if x > max:
            max = x
    return max
# 2b. Zdefiniuj funkcję zwracającą największy element w liście - wersja rekurencyjna.
def maximum_recur(L):
    if len(L) == 1:
        return L[0]
    else:
        if L[0] > maximum_recur(L[1:]):
            return L[0]
        else:
            return maximum_recur(L[1:])

# 3a. Zdefiniuj funkcję odwracającą kolejność elementów w liście - wersja rekurencyjna.
def reverse_rec(list):
    if len(list) == 0:
        return []
    else:
        return reverse_rec(list[1:]) + [list[0]]
# 3b. Zdefiniuj funkcję odwracającą kolejność elementów w liście - wersja iteracyjna.
def reverse_iter(list):
    start = []
    for i in list:
        start = [i] + start 
    return start

# 4a. Zdefiniuj funkcję, która konkatenuje dwie listy - wersja rekurencyjna.
def concaten(list1, list2):
    if len(list1) == 0:
        return list2
    else:
        return [list1[0]] + concaten(list1[1:], list2)
# 4b. Zdefiniuj funkcję, która konkatenuje dwie listy - wersja iteracyjna.
def concaten_iter(list1, list2):
    if len(list2) == 0:
        return list1
    else:
        total = list1
        for i in list2:
           total = total + [i]
        return total

# 5a. Zdefinuj funkcję, która sprawdza, czy dany element znajduje się na liście - wersja rekurencyjna.
def check_list(elem, list):
    if len(list)==0:
        return False
    else:
        if elem == list[0]:
            return True
        else:
            return check_list(elem,list[1:])
# 5b. Zdefinuj funkcję, która sprawdza, czy dany element znajduje się na liście - wersja iteracyjna.
def check_iter(elem, list):
    if list == []:
        return False
    else:
        temp = False
        for i in list:
            if i == elem:
                temp = True
        return temp

# 6a. Zdefiniuj funkcję, która wylicza największy wspólny dzielnik dwóch liczb - wersja rekurencyjna.
def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)
# 6b. Zdefiniuj funkcję, która wylicza największy wspólny dzielnik dwóch liczb - wersja iteracyjna.
def gcd_iter(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a



    
    
