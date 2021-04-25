"""
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

링크 : https://www.acmicpc.net/problem/4344
"""
C = int(input())
data = []
mean = 0
count = 0
number = 0
for i in range(C):
    data = list(map(int, input().split(' ')))
    # print(data)
    number = data[0]
    # print(number)
    for datum_value in data:
        mean += datum_value
        # print(datum_value)
    mean -= number
    mean /= number
    # print(mean)
    for datum_comp in data:
        if mean < datum_comp:
            count += 1
    # print(count)
    print("{:.3f}%".format(count/number*100))
    mean = 0
    count = 0
    