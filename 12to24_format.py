# this program converts give tim ein 12 hour format to 24 hour format in python without using any builtin funcs.


def timeConversion(str1):
    # Write your code here
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]
    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:

        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]


inp_time = "01:10:00PM"
print(timeConversion(inp_time))
