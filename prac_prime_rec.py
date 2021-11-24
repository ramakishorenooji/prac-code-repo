def rec_prime(a, N):
    if N <= 1:
        return
    if N == 2 or a >= N:
        print(N)
    elif (N % a) == 0:
        return False
    else:
        rec_prime(a + 1, N)
    return True


print(rec_prime(2, 3))



