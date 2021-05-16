"""
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 
그 수를 한수라고 한다. 
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
링크 : https://www.acmicpc.net/problem/1065
"""
# 한수 판별기
def isHansu(n):
    if n < 100:
        return True
    else:
        a = list(map(int,str(n)))
        if a[1] - a[0] == a[2] - a[1]:
            return True
        else:
            return False
        
# def isHansu(n):
#     if n < 100:
#         return True
#     else:
#         temp = list(map(int,str(n)))
#         return isIsometric(temp)

# def isIsometric(a: list):
#     if a[1] - a[0] == a[2] - a[1]:
#         result = True
#     else:
#         result = False
#     return result
        
# 갯수 체크
N = int(input("1000이하의 자연수 입력: "))
numberofHansu = 0
for i in range(1,N+1):
    if isHansu(i):
        numberofHansu += 1

# 출력
print(numberofHansu)