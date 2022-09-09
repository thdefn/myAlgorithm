# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 이상과 초과에 대해 주의해야함

def solve(data, n, p, q):
    S = 0  # 이 변수에 탑승할 수 있는 회원의 몸무게의 합을 계산한다
    C = 0  # 이 변수에 탑승할 수 있는 사람의 수를 계산한다
    for i in range(n):
        if (data[i] <= p):
            S += data[i]
            C += 1

    print(str(C) + " " + str(S))
    if (S <= q):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    n, p, q = [int(w) for w in input().split()]
    data = [int(w) for w in input().split()]
    solve(data, n, p, q)
