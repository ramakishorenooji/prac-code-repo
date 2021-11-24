#prime number in the recursive manner evaluation.
def prime_recursive(a,N):
    if N <= 1:
        return 
    if N == 2 or a >= N: 
        print(N)
    elif (N % a) == 0:
        return False
    else:
        return prime_recursive(a+1,N)

    return True
import time
start_time = time.time()
for i in range(10):  
    print(prime_recursive(2, i))
print("process finished in {} seconds".format(time.time() - start_time))