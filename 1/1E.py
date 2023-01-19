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

#
# def solution(code):
#     answer = ''
#     # {}{{}}
#     cnt = code.count('{')
#     for i in range(cnt,0,-1):
#         a = []
#         b= []
#         print(i)
#
#         cnt = code.count('{')
#         a.append(code.find('{'))
#         b.append(code.find('}'))
#         for k in range(1,cnt):
#             a.append(code.find('{',a[k-1]+1))
#             b.append(code.find('}',b[k-1]+1))
#         print(a)
#         print(b)
#         apos = a[i-1]
#         print(apos)
#         for j in range(cnt,1,-1):
#             if(a[i-1]<b[j-1]):
#                 pos = b[j-1]
#         print(pos)
#         code = code[:apos-1]+int(code[apos-1])*code[apos+1:pos]+code[pos+1:]
#         print(code)
#     answer = code
#     return answer


def solution(words, queries):
    answer = []
    for q in queries:
        idx = q.find('?')
        ans = []

        for i in range(len(words)):
            if (len(words[i]) == len(q)):
                if (words[i].startswith(q[:idx])):
                    ans.append(words[i])


        answer.append(ans)

    return answer

def solution(start, time):
    answer = []

    t_list = sorted(list(set(start)))
    idx_list = list(range(len(start))) #[0,1,2,3,4]
    mint = 0
    for t in t_list:
        res=[]
        t = t + mint
        #t = t + mint
        for i in idx_list:
            # start를 전부 비교
           if(start[i]<=t): #원소가 t보다 작거나 같으면
               res.append(time[i]) #해당 인덱스의 time 값 append

        mint = min(res)
        min_idx = time.index(mint) if time.index(mint) in idx_list else time.index(mint, min_idx+1)
        answer.append(min_idx)
        t_list = t_list + [mint]*len(t_list)
        idx_list.pop(idx_list.index(min_idx))
    answer = answer + idx_list
    return answer


def solution(numbers):
    answer = ''
    num_list = [str(numbers[i]) for i in range(len(numbers))]
    num_list.sort()
    for n in range(len(num_list)):
        max = num_list.pop()
        if(max.find('0')):
            print()
        answer += max

        print(answer)
    return answer

from collections import deque
def solution(numbers):
    answer = ''
    deq = deque(sorted(list(map(str,numbers))))
    for i in range(len(numbers)):
        max = deq.pop()
        if('0' in max):
            deq.appendleft(max)
            max = deq.pop()
        answer += max
    return answer


# def solution(arr):
#     answer = arr.index(max(arr))
#     if(answer == len(arr)-1):
#         answer = -1
#     elif(answer == 0):
#         answer = -1
#     return answer

if __name__ == "__main__":
    print(solution([9, 5, 34, 3, 303]))
    #print(solution(["hello", "hear", "hell", "good", "goose", "children", "card", "teachable"], ["he??", "g???", "childre?", "goo????", "?"]))