def sieve_of_Eratosthenes(n):
    primes = []

    for i in range(2,n):
        if i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0:
            primes.append(i)
        if i in [2,3,5,7]:
            primes.append(i)

    return primes

def prime_factors(x):
    prime_n = sieve_of_Eratosthenes(x)

    factors = []
    i=0
    while x >0:
        if x%prime_n[i]==0:
            x = x//prime_n[i]
            factors.append(prime_n[i])
            i = 0
        else:
            i+=1


    
    return factors

def common_from_two_lists(l1,l2):
    common = []
    for i in l1:
        if i in l2:
            l2.remove(i)
            common.append(i)
    
    return common

def middle_school_gcd(M,N):
    if M<0 or N<0:
        return "M and N must be Positive"
    N_primes = prime_factors(N)
    M_primes = prime_factors(M)

    common_factors = common_from_two_lists(N_primes,M_primes)
    gcd = 1
    for i in common_factors:
        gcd *= i
    
    print(N_primes,M_primes,common_factors,sep="\n")

    return gcd


print(middle_school_gcd(12,24))
