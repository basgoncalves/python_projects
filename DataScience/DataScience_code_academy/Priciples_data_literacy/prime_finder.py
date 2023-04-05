import numpy as np
import math


def prime_finder(upto):
        
    primes = []
    for num in range(2, upto+1, 1):                         # check numbers from 2 onwards since 2 is the first prime
        isprime = True
        for factor in range(2, 1+int(math.sqrt(num)), 1):   # using the arc approcah, only need to check if there are deviders up to sqrt(num)
            if not num % factor:
                isprime = False                             # if num is indeed devisable by any of the factors, then num is not a prime
                break

        if isprime:
            primes.append(num)
    return primes


n = 20
primes = prime_finder(n)
print('primes of ' + str(n) + ' = ' + str(primes))


# Different smart approach!!
# import numpy as np

# is_prime = lambda n : ~np.any(n%np.array(list(range(2,n))) == 0) 
# prime_finder = lambda n : [i for i in range(2,n+1) if(is_prime(i))]