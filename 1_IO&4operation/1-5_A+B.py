"""
A+B 프로그램을 작성하라
링크 : https://www.acmicpc.net/problem/1000
"""

# 무식하게 받아보자
# A = input("first integer : ")
# B = input("second integer : ")

# 친절하게 받지만 아직 멀었다
# A, B = input('input two integer A, B: ').split(' ')

# 완전 깔끔
# A, B = map(int, input().split())

# 실전 풀이
A, B = input().split(' ')
A = int(A)
B = int(B)

# 중간 확인
# print(A)
# print(B)
# print(f"Sum is {A+B}")

# 출력
print(A+B)