
#
def fib(n):
    first, second = 0, 1
    
    while first <= n: 
        yield first
        first, second = second, first + second

x = fib(5)
print("using for loop to get next element")
for i in fib(5):
    print(i)