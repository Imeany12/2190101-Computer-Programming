def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def is_coprime(a, b, c):
    return min([gcd(a,b), gcd(b,c), gcd(a,c)]) == 1

def primitive_Pythagorean_triples(max_len):
    triple = []
    
    if max_len < 5:
        return triple
    
    c,m = 0,2
    while m**2 < max_len:
        for n in range(1, m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            
            if c > max_len:
                break

            if is_coprime(a,b,c):
                triple.append(sorted([a,b,c]))
        m += 1
    return sorted(triple, key= lambda x: [x[-1], x[0], x[1]])

exec(input().strip())

