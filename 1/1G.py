# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 인덱스의 기준이 0-based 가 아닌 경우 > 기본적으로 0 based 하되 필요한 부분에만 1 based로


def get_indexes(schools, n):
    first_index = -1  # -1은 아직 발견을 못했다는 의미
    last_index = -1

    for i in range(n):
        # schools[i] := schools[0] ~ schools[n-1] 사이의 모든 학교 이름
        if (schools[i] == "AJOU"):
            # i := 학교 이름이 AJOU인 데이터의 인덱스
            last_index = i
            if (first_index == -1):
                first_index = i
    # 0 based index > 1 based index
    return first_index + 1, last_index + 1


if __name__ == '__main__':
    n = int(input())
    schools = [input() for i in range(n)]
    first_index, last_index = get_indexes(schools, n);
    print("{} {}".format(first_index, last_index))