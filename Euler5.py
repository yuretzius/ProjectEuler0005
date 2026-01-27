import numpy as np
from functools import reduce
from time import perf_counter


def Erat(N):
    """
    The Sieve of Eratosthenes implemented with numpy arrays
    Returns the list of primes lower or equal than N
    """
    if N == 0 or N == 1 : return []
    elif N == 2: return [2]
    elif N == 3: return [2,3]
    else:
        N_bool = np.array([True]*(N+1))
        N_bool[0] = False
        N_bool[1] = False
        N_bool[2] = True
        N_bool[3] = True
        N_bool[2**2::2] = False # eiminating even numbers
        p = 3
        while p*p <= N:
            # start from p**2
            # because all the smaller composites have factors <p
            # and are already eliminated in previous steps
            N_bool[p**2::p] = False # python doesn't care if ::p goes beyond existing array
            p = p + 2 # only odd numbers can be primes larger than 3
            while not N_bool[p]:
                p = p + 2 # skip p if it has already been eliminated in previous steps
    # returns indices of nonzero elements, which in this case
    # ARE the correcponding natural numbers, which were not eliminated
    # Have to use index [0], because for technical reasons it produces a 2D array
    return list(np.nonzero(N_bool)[0]) 
    
def IncompletePrimeFactor(N): 
    """
    Returns the list of all prime factors of N with a possible exception
    of a single factor > sqrt(N). If N is prime, it returns an empty list.
    """
    # create the list of primes lower or equal to sqrt(N)
    primes = np.array(Erat(int(np.ceil(np.sqrt(N)))))
    # if N is divisible by a prime, N%p = 0
    # so when we create an array of N%p for all primes
    # it has 0 entries for factors and non-zero one for non-factors
    # recasting it as bool turns 0 into False and non-zero to True
    # after we invert them, we get True for factors and False for non-factors
    prime_mask = np.invert(np.array(N%primes, dtype = bool))
    # now we only need to apply this mask to return only prime factors
    # but since we limited ourselves to p < sqrt(N)
    # we might miss a factor > sqrt(N), like e.g. 33 = 3*11
    # so be careful when using this output
    return list(primes[prime_mask])

def FactorMultiplicity(N):
    """
    Returns two lists, the first with all the factors of N
    the second with corresponding multimlicities of each of them.
    """
    factors = IncompletePrimeFactor(N)
    if not factors: return [N],[1] # N is prime
    multiplicity = []
    # just cycle through all the factors 
    # and check how many time N is divisible by each
    for p in factors:
        m = 0
        while N%p == 0:
            m += 1
            N = N//p
        multiplicity.append(m)
    if N != 1: # the case of a single additional factor > sqrt(N)
        factors.append(N)
        multiplicity.append(1)
        
    # must recast them as python int, because
    # since we used numpy array before, their
    # type was changed to long_scalars, the default
    # int type of numpy. If we don't do this
    # we quickly get overflow when multiplying these
    # numbers
    
    factors = [int(x) for x in factors]
    return factors, multiplicity

start = perf_counter()

N = 20 

numbers = [u for u in range(2,N+1)]

fmdict = {}

for n in numbers:
    flist, mlist = FactorMultiplicity(n)
    for i in range(len(flist)):
        f, m = flist[i], mlist[i]
        try:
            m_old = fmdict[f]
            # if we don't have enough multiplicity for this factor
            # it must be increased:
            if m > m_old: fmdict[f] = m 
        except KeyError: # this factor was not encountered before
            fmdict[f] = m 

list_comp = [u[0]**u[1] for u in fmdict.items()] # array of all the relevant factors, p**m_max                                                                                     

# reduce uses the starting number (the second argument) 1
# and then applies the lambda-expression to all the list elements
# in this case, mulitiplies all the list items

res = reduce(lambda x, y: x*y, list_comp, 1)

end = perf_counter()

# the beauty of python is that its ints have no limit, so you can run
# this script with large max numbers
# e.g. for N = 100 the answer is 
# 69720375229712477164533808935312303556800

print(res)

print(end - start, 'sec')