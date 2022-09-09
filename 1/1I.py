# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

"""
n=5, a = {3,5,1,2,4}
1) a = {1,5,3,2,4} b0 찾아서 a[0]으로 옮기기
2) a = {1,2,3,5,4} b1 찾아서 a[1]으로 옮기기
3) a = {1,2,3,5,4} b2 찾아서 a[2]으로 옮기기
4) a = {1,2,3,4,5} 일반화 : bi 찾아서 a[i]으로 옮기기
"""


def find_min_index(data, begin, end):
    # data[begin] ~ data[end] 사이의 최소값을 구해서 그 인덱스 반환
    min = max(data)
    for j in range(begin, end):  # j := begin~end
        if (data[j] < min):
            min = data[j]
            idx = j
    return idx


def selection_sort(data, n):
    for i in range(n - 1):
        # bi 찾아서 a[i]로 이동
        # a[i] ~ a[n-1] 중 최소값을 a[i]로 이동 -> a[0] ~ a[i-1]까지는 이미 정렬됨

        # data[i] ~ data[n]에서 최소값을 찾은 다음
        idx = find_min_index(data, i, n)
        # data[i]로 이동시키기
        var = data[idx]
        data[idx] = data[i]
        data[i] = var
    return data


if __name__ == "__main__":
    n = int(input())
    data = [int(w) for w in input().split()]
    result = selection_sort(data, n)
    print(" ".join([str(w) for w in result]))