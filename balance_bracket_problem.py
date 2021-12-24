# balance_bracket_problem.py

open_list = ["[", "(", "{"]
close_list = ["]", ")", "}"]


def balance_bracket(mystr):
    arr = []
    for i in mystr:
        if i in open_list:
            arr.append(i)
        elif i in close_list:
            pos = close_list.index(i)  # why do i need position?
            print(open_list[pos])
            if (len(arr) > 0) and (open_list[pos] == arr[len(arr) - 1]):
                arr.pop()
                print(arr)
        else:
            return "Unbalanced"

    if len(arr) == 0:
        return "Balanced"
    else:
        return "unbalanced"


mystr = "(())"
print(balance_bracket(mystr))
