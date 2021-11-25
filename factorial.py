def factorial(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        print(f'{cache} found in cache')
        return cache[n]
    else:
        print('calculaing {}!'.format(n))
        result = n * factorial(n - 1)
        cache[n] = result
        return result

print(factorial(5))