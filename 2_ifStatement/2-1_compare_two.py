"""
두 정수 A, B가 주어졌을 때, 
A와 B를 비교하는 프로그램을 작성하시오
링크 : https://www.acmicpc.net/problem/1330
"""

a, b = map(int, input().split())

if(a > b):
    print(">")
elif(a < b):
    print("<")
else:
    print("==")

# 이제 뇌가 풀리기 시작하네