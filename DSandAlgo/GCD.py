# to find GCD of a number using euclid Algorithm
# gcd(m,n) m=qn+r if m = ad and n=bd where d is common divisor between m and n , then ad=qbd+r and r is divisible by d
def findgcd(m, n):
    if m < n:
        (m, n) = (n, m)
    while m % n != 0:
        remainder = m % n
        (m, n) = (n, remainder)
    return n
