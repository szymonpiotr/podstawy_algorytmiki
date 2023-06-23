# ITERACJA
# Zadanie 1: zdefiniuj funkcję usuwającą z listy elementy, które się powtarzają. Użyj iteracji.

# REKURENCJA
# Zadanie 2: zdefiniuj funkcję "zip", która dostając dwie listy utworzy z nich listę par, których
# pierwszymi elementami będą elementy pierwszej listy, zaś drugimi elementami obietty z drugiej listy, dopóki któraś 
# lista się nie wyczerpie. Użyj rekurencji.
# Działanie: zip([1,2,3],[True, False, True, False]) = [(1, True), (2, False), (3,True)]

# REKURENCJA OGONOWA
# Zadanie 3: zdefiniuj funkcję "filterList", która bierze listę elementów oraz 
# predykat (funkcję zwracającą wartośc boolowską), natomiast zwraca listę tych wszystkich elementów z pierwotnej 
# listy dla których dana funkcja zwraca True. Użyj rekurencji ogonowej (rekurencji z dodatkowym parametrem).
# Działanie: filterList(lambda x: x % 2 == 0, [1,2,3,4,5,6]) = [2,4,6]

# DRZEWA i REKURENCJA 

class Node:                  # klasa drzew z maksymalnie dwoma rozgałęzieniami
   def __init__(self, data): # każdy node/węzeł ma w sobie jakąś wartość (np. liczbę)
      self.data = data       # którą można odzyskać metodą .data
      self.left = None       # ma też lewe poddrzewo 
      self.right = None      # oraz prawe poddrzewo

# przykład drzewa binarnego      
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)
root.right.right.right = Node(7)  
      
class RoseNode:              # klasa rose trees
    def __init__(self,data): # każdy node/węzeł ma w sobie jakąś wartość (np. liczbę)
      self.data = data       # którą można odzyskać metodą .data
      self.subtrees = []     # oraz listę poddrzew.

# przykład rose tree
root1 = RoseNode(1)
root2 = RoseNode(2)
root1.subtrees = [root2,  RoseNode(3), RoseNode(4)]   
root2.subtrees = [RoseNode(5), RoseNode(6)]
   
# Zadanie 4: zdefiniuj funkcję "map_tree(function,tree)", 
# która bierze funkcję i drzewo (RoseNode) a następnie używając funkcji 
# "function" zamienia etykiety w liściach danego drzewa.      

# Zadanie 5: zdefiniuj funkcję "transformTree(tree1)", która jako argument bierze 
# drzewo binarne ("Node"), natomiast zwraca rose tree ("RoseNode"). Dlaczego translacja odwrotna jest niemożliwa? 
