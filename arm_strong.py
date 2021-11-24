# To check if sum of cube of each number in x is same as the number x, 1^3+5^3+3^3 = 153

x = 371
l = []

def arm_strong(num):
    s = num
    result = 0
    while num > 0:
        # if num == 0:
        #     break
        t = num % 10
        result = result + pow(t, 3)
        num = (num // 10)
        
    print(s, result)
    if result == s:
        return "Arm_strong"
    else:
        return "Not Arm_strong"


res = arm_strong(x)
print(res)

