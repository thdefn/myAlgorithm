# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 합을 구하는 과정에서 결과가 int의 범위를 벗어나지느 않는가?
# 이러한 누적합을 더 빠르고 간결하게 구하는 방법은 없는가 ?

"""
검증방법
추산, 검정, long을 넣어 최악의 케이스를 가정하고 돌려봄
"""

def range_sum_from_one(n):
	# 1~n까지 더한 값
	# 가능하면 반복문과 같은 무거운 연산을 사용하지 않고 구할 수 있는 방법 사용 etc 등차수열
	sum = 0
	for i in range(1,n+1):
		# i := 1 ~ n
		sum += i
	return sum

def get_answer(n):
	tot = 0 # 1 + (1+2) + (1+2+3) + ...
	for i in range(1,n+1):
		# i := 1 ~ n
		sum = range_sum_from_one(i)
		tot += sum
	return tot


if __name__ == "__main__":
	n = int(input())
	answer = get_answer(n)
	print(answer)