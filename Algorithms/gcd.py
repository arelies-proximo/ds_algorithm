
import math


def euclids_gcd(M,N):
    if N==0:
        return M
    else:
        print(M,N)
        R = M%N
        M,N = N,R
        return euclids_gcd(M,N)


def repetitive_subt_gcd(M,N):
    if M == N or M<0 or N<0:
        #base case
        if M<0:
            return N
        return M
    print(M,N)
    if M>N:
        return repetitive_subt_gcd(M-N,N)
    else:
        return repetitive_subt_gcd(M,N-M)



def consecutive_integer_checking(M,N,small = None):
    if small is None:
        small = min(M,N)
    print(M,N,small)
    if M%small == 0 and N%small==0:
        return small
    else:
        small -= 1
        return consecutive_integer_checking(M,N,small)


