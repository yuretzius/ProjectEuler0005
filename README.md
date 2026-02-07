# ProjectEuler0005
My work on

[problem #5 of projecteuler.net](https://projecteuler.net/problem=5):

Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from 1 to 20 ?

Completed on Sat, 20 Feb 2021, 18:35

#######################################################################################
Please note: Project Euler's policy allows publication of solutions for the first 100 problems,
that's why I am sharing my work here for reference and educational purposes.
#######################################################################################

This is an example of a problem that is easiest to do with a pen, paper, and calculator or perhaps a spreadsheet (see [Euler5.xlsx](https://github.com/yuretzius/ProjectEuler0005/blob/main/Euler5.xlsx)).
Indeed, just listing the numbers from 2 to 20 we see that only two prime factors are encountered in them multiple times, 2 and 3.
For 2 the maximum is: 2 * 2 * 2 * 2 = 16 and for 3: 3 * 3 = 9. Thus the immediate answer is:

16 * 9 * 5 * 7 * 11 * 13 * 17 * 19

Doing the same calculation in a program and for an arbitrary maximum number is slightly more difficult.

In Python it is a good place to introduce prime factoring tools (useful for many Project Euler problems).
My way of doing it is not very efficient for very large numbers and fast computations, but educational.
In this case we are factoring small numbers, so the computation speed is irrelevant.

I use the the Sieve of Eratosthenes implemented with numpy arrays Erat(N) to create the list of primes lower or equal than a number.
Then applying this to sqrt(N) I can easily get the list of all prime factors of N, except perhaps for one that is larger than sqrt(N)
(like e.g. 11 in 33 = 3 * 11). IncompletePrimeFactor(N) returns this list. If N is prime, it returns an empty list. 
Finally I cycle through these factors to determine the multiplicity of each of them and to check if the factor larger than sqrt(N)
is present. FactorMultiplicity(N) returns two lists: of factors and of corresponding multiplicities.
E. g. for 33 it would return [3,11] and [1,1].

Note that since these tools use numpy arrays, in FactorMultiplicity(N) we have to recast factors as python int, otherwise
the type will be the standard numpy long_scalars, which may lead to overflows. And with python ints there is no limit for
the size of numbers except for the available memory and computing power.

Now it is easy to factor each number in the list, find the max multiplicity for each prime factor, and then multiply them all together.

In C++ without using any specialized large integer tools we are limited to unsigned long long type max, which is 18446744073709551615.
Turns out this limits max N to 46. Thus we can cheat, instead of all the factoring we can see that, since 7 * 7 = 49 > 46,
primes starting with 7 can only have the multiplicity of 1. I use the list of primes < 100 for future reference, but of course
only primes up to 43 are needed. And for the remaining primes 2, 3, and 5 we are limited to only a few possible multiplicities,
which are easy to cycle through. So, apart of watching for the overflow, the C++ version is very straightforward.   
