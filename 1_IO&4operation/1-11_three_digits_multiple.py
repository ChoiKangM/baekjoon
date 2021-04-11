"""
(세자리 수) * (세자리 수) 과정을 풀어서 보여주라
링크 : https://www.acmicpc.net/problem/2588
"""

# 무식한 풀이
# a = 472
# b = 385

# first_factor = b % 10
# second_factor = int(b / 10 % 10)
# third_factor = int(b / 100)

# print(first_factor)
# print(second_factor)
# print(third_output)

# first_output = a * first_factor
# second_output = a * second_factor
# third_output = a * third_factor

# print(first_output)
# print(second_output)
# print(third_output)
# print(first_output + 10*second_output + 100*third_output)

# 정리된 풀이
# 주어지는 입력값을 꼭 참고하자!
a = int(input())
b = int(input())
first_output = a * (b % 10)
second_output = a * int(b / 10 % 10)
third_output = a * int(b / 100)

print(a * (b % 10))
print(a * int(b / 10 % 10))
print(a * int(b / 100))
print(a * b)