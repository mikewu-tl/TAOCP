def gcd_euclid(a:int,b:int) -> int:
    while b:
        a,b=b,a%b
    return a

print(gcd_euclid(16,12))
print(gcd_euclid(17,13))
print(gcd_euclid(225,75))