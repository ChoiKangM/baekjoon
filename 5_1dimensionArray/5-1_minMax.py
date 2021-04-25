"""
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

링크 : https://www.acmicpc.net/problem/10818
"""

N = int(input())
nIntegers = list(map(int,input().split(' ')))

print(min(nIntegers), max(nIntegers))



# A =[10,11,12,13,15]
# print(min(A), max(A))
# # Custum Max Value
# maxValue = A[0]
# for i in range(1, len(A)):
#     if maxValue < A[i]:
#         maxValue = A[i]
# # Custom Min Value
# minValue = A[0]
# for i in range(1,len(A)):
#     if minValue > A[i]:
#         minValue = A[i]
# print(maxValue)
# print(minValue)
# print(A)

