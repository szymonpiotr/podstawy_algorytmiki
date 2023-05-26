# szymon.chlebowski@amu.edu.pl
# Zdefinuj funkcję "listToSet", która usuwa z listy 
# elementy powtarzające się. 
# Zdefiniuj funkcję pomocniczą sprawdzającą
# czy dany obiekt znajduje się na liście. Użyj rekurencji. 
# Działanie:
# listToSet([1,2,3,1,4,1,5,4,3,2,4]) = [1,2,3,4,5]   

def check_list(elem, list):
    if len(list)==0:
        return False
    else:
        if elem == list[0]:
            return True
        else:
            return check_list(elem,list[1:])

def listToSet(list):
    if list == []:
        return []
    else:
        first = list[0]
        rest = list[1:]
        if check_list(first, rest):
            return listToSet(rest) 
        else:
            return [first] + listToSet(rest)   

print(listToSet([1,2,3,1,4,1,5,4,3,2,4]))            
        