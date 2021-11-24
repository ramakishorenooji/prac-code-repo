import time
low = 0
high = 100
start_time = time.time()
for num in range(low, high + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
print("process finished in {} seconds".format(time.time() - start_time))
            

