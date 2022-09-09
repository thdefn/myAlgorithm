# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 만약 아래 로직으로 오답이 나오면 Big Int 가 필요하지 않은지 체크

def get_sum(data, n):
    answer = 0
    # 배열의 원소의 합을 저장할 수 있도록 코드를 작성해보세요
    # ...
    for i in range(n):
        # i := 0 ~ (n-1)사이의 모든 정수
        # data[i] := data[0] ~ data[n-1] 사이의 모든 원소
        answer += data[i]

    return answer


if __name__ == '__main__':
    n = int(input())
    data = [int(w) for w in input().split()]
    answer = get_sum(data, n)
    print(answer)
