# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 1 based index
# 큰 숫자의 데이터를 여러 개 더하는 경우 항상 이 숫자의 범위에 대해 생각해야 함
# 10만 * 1만개 = 10억 : 32비트 정수형의 표현 범위 = 21억

def find_index(data, n):
    avr = sum(data) / n
    idx = 0
    min = abs(avr - data[0])
    for i in range(n):
        # data[i] := data[0] ~ data[n-1]
        dist = abs(avr - data[i])
        if (dist < min):
            min = dist
            idx = i

    return idx + 1


if __name__ == "__main__":
    n = int(input())
    data = [int(w) for w in input().split()]
    answer = find_index(data, n)
    index = answer - 1
    print("{} {}".format(answer, data[index]))