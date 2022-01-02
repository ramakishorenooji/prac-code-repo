


def minimum_egg_drop(x, e, f):

    sum = 0
    term = 1
    i = 1
    while i <= e and sum < f:
        term *= x - i + 1
        term /= i
        sum += term
        i += 1
    return sum



def min_drops(e, f):

 
    low = 1
    high = f
  
    while low < high:

        mid = int((low + high) / 2)
        if minimum_egg_drop(mid, e, f) < f:
            low = mid + 1
        else:
            high = mid

    return int(low)

print(min_drops(2, 100))

# This code is contributed
# by mits
