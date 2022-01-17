# to find GCD of a number using euclid Algorithm : m and n will have atleast 1 as common divisor and if d is largest
# common divisor between m and n then m=ad and n=bd, m-n=ad-bd=(a-b)d therefore gcd(m,n)=gcd(n,m-n) gcd(m,
# n): the number m can be written as m=qn+r ---(i)  replacing this in (i) ad=qbd+r and so r will also be divisible by
# d: note assume m>n if not interchange
def findgcd(m, n):
    if m < n:
        (m, n) = (n, m)
    while m % n != 0:
        remainder = m % n
        (m, n) = (n, remainder)
    return n
