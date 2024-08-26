def sum_of_three_numbers(a=5, b=10, c=15):
    return a + b + c


result = sum_of_three_numbers(10, 10, 10)
print(result)

result2 = sum_of_three_numbers(10, 20)
print(result2)

result3 = sum_of_three_numbers(10)
print(result3)

result4 = sum_of_three_numbers()
print(result4)

result5 = sum_of_three_numbers(a=12, c=22)
print(result5)