# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 데이터가 없을 때 데이터가 중복되어 있을 때 어떻게 해야할까 ?
# 탐색 문제에서 유의해야 할 부분
# 1. 조건을 만족하는 원소가 없을 때 2. 조건을 만족하는 원소가 두 개 이상일 때 3. 원소의 번호가 0번부터 시작하는지 1부터 시작하는지

def find_value(value, arr):
    # 데이터를 탐색하지 못하면 -1
    # 데이터를 탐색했으면 그 인덱스 0 based index
    index = -1
    for i in range(len(arr)):
        # [BEGIN]
        if (arr[i] == value):
            index = i
            break

    # [END]
    return index


n, m = map(int, input().split())
data = list(map(int, input().split()))
answer = find_value(m, data)
print(answer)