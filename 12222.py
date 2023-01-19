'''def solution(a, b):
    answer = []

    a.reverse()
    b.reverse()

    if (len(a) >= len(b)):
        length = len(a)
        b = b + [0] * (len(a) - len(b))
    else:
        length = len(b)
        a = a + [0] * (len(b) - len(a))
    res = 0

    for i in range(length):
        res = a[i] + b[i] + res
        if (res > 9):
            answer.append(res % 10)
            res = res // 10
        else:
            answer.append(res)
            res = 0

    if (res != 0):
        answer.append(res)

    answer.reverse()

    return answer'''

'''def solution(N, trust):
    answer = 0
    if(len(trust)==N-1):
        temp = trust[0] #temp = [1,2]
        for t in trust:
            # t = [1,2]
            for k in temp: #k=[1]
                if(k not in t):
                    temp.remove(k)
        answer=temp[0]
    else:
        answer=-1
    return answer
'''

def solution(N, trust):
    answer = 0
    res = []

    a=trust[0][0]
    tmp=[]
    for i in range(len(trust)):
        if(a!=trust[i][0]):
            a=trust[i][0]
            res.append(tmp)
            tmp=[]
        if(trust[i][0] == a):
            tmp.append(trust[i][1])
    res.append(tmp)

    if(len(res)==N-1):
        tmp = res[0] #2,4,3
        for t in res: #2,4,3
            for k in tmp: #2
                if(k not in t):
                    tmp.remove(k)
            if(len(tmp)==0):
                answer = -1
                break
        if(len(tmp)==1):
            answer = tmp[0]
    else:
        answer = -1
    return answer


def solution(delay, N):
    answer = 0
    # 1+1*2+(1*2)+(1*2+1*2)+(1*2+1*2+1*2)
    a = []  # 분열 불가
    b = 1  # 분열 가능
    for i in range(1, N + 1):
        b = b
        size = 0
        for k in range(len(a)):
            a[k]=a[k]-1
            if(a[k]==0):
                size = size+1
        b = b + size
        for j in range(b):
            a.append(delay)

    answer = b + len(a)
    return answer

if __name__ == '__main__':
    print(solution(1, 2))