# Zdefiniuj funkcję "apply", która bierze funkcję "f" oraz listę "list" 
# obiektów a następnie zwraca listę, której elementy są wartościam 
# funkcji "f" dla argumentów z listy "list".
# Działanie:
# my_list = list(range(10))
# function = lambda x: x*2
# apply(function, my_list) = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


def apply(function, arg):
    if arg == []:
        return []
    else:
        return [function(arg[0])] + apply(function, arg[1:])



