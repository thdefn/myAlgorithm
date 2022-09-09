# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

#데이터 N, M, S을 입력받는다
n, m, s = map(int, input().split())

#공백으로 구분된 N개의 정수(사람들의 키)를 입력받는다
data = list(map(int, input().split()))

#사람들의 수를 셀 변수 count를 0으로 초기화한다
count = 0 #확인해보아야 할 후보의 수

#[BEGIN ]
#count 변수에 정답(조사해야 할 사람의 수)이 저장되도록 코드를 작성해보자

for i in range(n):
	# i := 0 ~ n-1 사이의 모든 정수
	# data[i] := data[0] ~ data[n-1] 의 모든 원소가
	if(data[i] == m or data[i] == s):
		# data[i] := data[0] ~ data[n-1] 사이의 원소중 m이거나 s와 일치하는 모든 원소가
		count += 1

#[END]


print(count) # m 혹은 s와 일치하는 원소의 수