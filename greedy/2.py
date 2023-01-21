#큰수의 법칙
#주어진 수를 m번 더해서 가장 큰 수를 만들자
#k 초과해서 중복 불가


def getSum(n, m, k, data):
    data.sort()
    answer = 0
    i = 0
    isFirst = True
    first = data[n - 1]
    second = data[n - 2]

    while (i < m):
        if (isFirst == True):
            for j in range(k):
                answer += first
                i = i + 1
                if (i == m): break
            isFirst = False
        else:
            answer += second
            i = i + 1
            isFirst = True

    print(answer)

def answer(n, m, k, data):
    data.sort()
    first = data[n-1]
    second = data[n-2]
    countFirst = int(m/(k+1))*k #first가 곱해지는 수
    countFirst += m%(k+1) #m이 k+1로 나누어지지 않는 경우를 더하기

    result = 0
    result += (countFirst)*first
    result += (m-countFirst)*second

    print(result)
    


if __name__ == '__main__':
    getSum(5, 8, 3, [2,4,5,4,6])
    answer(5, 8, 3, [2,4,5,4,6])

    # n, m, k = map(int, input().split())
    # data = list(map(int, input().split()))
    # getSum(n, m, k, data)
