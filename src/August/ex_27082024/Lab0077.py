def sum_three(a, b, c):
    return a + b + c


sum_three_num = lambda a, b, c: a + b + c
print(sum_three_num(1, 2, 3))


def find_odd_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


o = find_odd_even(4)
print(o)

chech_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(chech_even_odd(9))
