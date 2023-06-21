class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)
root.right.right.right = Node(7) 

#            1
#      2           3
#               4     5
#                    6 7

def printTree(root):
   print(root.data)
   if root.left == None:
        print("no left")
   else:
        printTree(root.left)
   if root.right == None:
        print("no right")
   else:
        printTree(root.right)    

def is_element(root, element):
    if root.left == None and root.right == None:
        return element == root.data
    else:
        return (is_element(root.left, element)) or (is_element(root.right, element)) or (element == root.data)
    

#print(is_element(root, 10))

def how_many_nodes(root):
    if root.left == None and root.right == None:
        return 1
    else:
        return how_many_nodes(root.left) + how_many_nodes(root.right)     


# Zadanie 1: zdefiniuj funkcję "map_tree(function,tree)", która bierze 
# funkcję i drzewo etykietowane oraz zamienia etykiety w drzewie używając funkcji "function".


def mapTree(function, tree):
    if tree.left == None and tree.right == None:
        tree.data = function(tree.data)
        return tree
    else:
        tree.data = function(tree.data)
        tree.left = mapTree(function, tree.left)
        tree.right = mapTree(function, tree.right)
        return tree
    
printTree(mapTree(lambda x: x+2, root))


class RoseNode:
    def __init__(self,data):
      self.data = data
      self.subtrees = []

root1 = RoseNode(1)
root1.subtrees = [RoseNode(2),  RoseNode(3), RoseNode(4)]

# Zadanie 2: zdefiniuj funkcję "howManyRose", która bierze RoseTree i zwraca liczbę 
# wszystkich węzłów tego drzewa. 

def howManyRose(tree):
    if tree.subtrees == []:
        return 1
    else:
        total = 1
        for i in tree.subtrees:
            total += howManyRose(i)
        return total 

# Zadanie 3: zdefiniuj funkcję "isElementRose(element,tree)", która sprawdza, czy dany element jest na drzewie.

# Zadanie 4: zdefiniuj funkcję "howManyBranchesRose(tree)", któa sprawdza ile gałęzi ma dane drzewo.
