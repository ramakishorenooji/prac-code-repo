#simple fib approach

def fib(n):
    print('calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

#print(fib(10))
 
