# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 더 작은 문제를 통해 큰 문제를 푼다

#배열(data)의 원소 중 가장 큰 정수를 반환하는 함수를 작성해보자
def get_max(data, n):
	# begin
	max = data[0]
	# 반복문에서 가장 첫 루프, 가장 마지막 루프는 꼭 검증한다
	for i in range(n):
		# i := 0 ~ n-1 사이의 정수, 차례로 한 번씩 등장
		# data[i] := data[0] ~ data[n-1] 원소들이 차례로 한번씩 등장
		if(data[i]>max):
			max = data[i]
	return max # max : = data[0] ~ data[n-1] 중 최대값
	# end


#데이터의 수를 입력받는다
n = int(input())
#데이터들을 입력받는다
data = map(int, input().split())
data = list(data)
#배열의 최대값을 저장한다
answer = get_max(data, n)
#답을 출력한다
print(answer)