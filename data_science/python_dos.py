def larg(num, n):
    num.sort()

    return num[-n:]

def show_mutation_of_lists():
    Num = [1, 4, 3, 2, 7, 8, 5]
    A = Num
    print(Num)
    Larg = larg(Num,2)
    print(Num)
    print(A)

def list_compreension():
    from math import sqrt
    x = [2 + i / sqrt(i) for i in range(1, 10)]
    print(x)

def multiple_arguments(*args, **kwargs):
    print(args)
    print(kwargs)
    pass

# multiple_arguments(1,2,3, x=3)
# multiple_arguments(*(3,4,6),**{'a': 2, 'b': 34})

