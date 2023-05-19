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
# 2b. Zdefiniuj funkcję zwracającą największy element w liście - wersja rekurencyjna.

# 3a. Zdefiniuj funkcję odwracającą kolejność elementów w liście - wersja rekurencyjna.
# 3b. Zdefiniuj funkcję odwracającą kolejność elementów w liście - wersja iteracyjna.

# 4a. Zdefiniuj funkcję, która konkatenuje dwie listy - wersja rekurencyjna.
# 4b. Zdefiniuj funkcję, która konkatenuje dwie listy - wersja iteracyjna.

# 5a. Zdefinuj funkcję, która sprawdza, czy dany element znajduje się na liście - wersja rekurencyjna.
# 5b. Zdefinuj funkcję, która sprawdza, czy dany element znajduje się na liście - wersja iteracyjna.

# 6a. Zdefiniuj funkcję, która wylicza największy wspólny dzielnik dwóch liczb - wersja rekurencyjna.
# 6b. Zdefiniuj funkcję, która wylicza największy wspólny dzielnik dwóch liczb - wersja iteracyjna.

# Sortowanie

# 1a. Zdefinuj funkcję, która sortuje listę liczb - użyj rekurencji. Jeśli jest to potrzebne
# zdefiniuj funkcje pomocnicze. 
# 1b. Zdefinuj funkcję, które sortuje listę liczb - użyj iteracji.

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

    
    
