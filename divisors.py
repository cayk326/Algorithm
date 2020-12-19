def divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i**2 <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

if __name__ == '__main__':
    print(divisors(10))