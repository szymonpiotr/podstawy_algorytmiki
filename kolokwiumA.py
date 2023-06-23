# ITERACJA
# Zadanie 1: zdefiniuj funkcję usuwającą z listy elementy, które się powtarzają. Użyj iteracji.

# REKURENCJA
# Zadanie 2: zdefiniuj funkcję "unzip", która bierzę listę par, natomiast zwraca dwie listy (np. umieszczone w parze),
# które spełniają warunek: pierwsza z nich przechowuje wszystkie pierwsze elementy par, natomiast druga - wszystkie drugie 
# elementy par.
# Działanie: unzip([(1, True), (2, False), (3,True)]) = ([1,2,3],[True, False, True])

# REKURENCJA OGONOWA
# Zadanie 3: zdefiniuj funkcję scalającą dwie listy używając rekurencji ogonowej (rekurencji z dodatkowym parametrem).
# Użyj rekurencji ogonowej.
# Działanie: scal([3,2,1],[5,4,3]) = [3,2,1,5,4,3]

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
# "function" zamienia wszystkie etykiety w drzewie.      

# Zadanie 5: zdefiniuj funkcję "transformTree(tree1)", która jako argument bierze 
# drzewo binarne ("Node"), natomiast zwraca rose tree ("RoseNode"). Dlaczego translacja odwrotna jest niemożliwa? 
