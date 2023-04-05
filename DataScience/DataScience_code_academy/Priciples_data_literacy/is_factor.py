

def is_factor(num, factor):
    remainder = num % factor    # '%' returns the remainder of the devision num / factor
    isfactor = not num % factor

    print(str(num) + ' % ' + str(factor) + ' = ' + str(remainder))
    print('isfactor = ' + str(isfactor))

    if not num % factor:
        print(str(factor) + ' is a factor of ' + str(num))

    return isfactor

num = 4
factor = 2
print(is_factor(num,factor))