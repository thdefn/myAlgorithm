from collections import deque

def solution(values):
    answer = [0,0]
    tmp = []
    before = 0
    tmp.append(0)
    for i in range(len(values)):
        if(values[i]<=values[before]): #단조증가하지 않는 경우
            tmp.append(before) #단조증가했던 인덱스까지 tmp에 넣어줌
            if(tmp[1]-tmp[0]>answer[1]-answer[0]): #기존값과 비교해 tmp len이 긴경우
                answer = tmp
            tmp = [] #tmp는 초기화 후 현재 value 넣어줌
            tmp.append(i)
        before = i
    return answer

def solution(ingredients, items):
    answer = len(items)
    for i in range(len(items)):
        if(items[i] in ingredients):
            val = rotate(ingredients, items[i:])
            if(answer > val):
                answer = val
    return answer

#  itmes : "인삼", "커피", "생닭", "소주", "사탕", "생닭", "대추", "쌀"
#  ingredients : "생닭", "인삼", "소주", "대추"
def solution(ingredients, items):
    if(len(items)<len(ingredients)):
        return -1
    answer = len(items)
    for i in range(len(items)):
        if (items[i] in ingredients):
            val = solution(ingredients, items[i+1:])
            ingredients.remove(items[i])
            if(val != -1):
                if (answer > val):
                    answer = val
            print(ingredients)
            print(len(ingredients))
            print(items[i])
        if(len(ingredients)==0):
            if(answer > i+1):
                answer = i+1
                return answer

    if(len(ingredients)!=0):
        return -1
    return answer



if __name__ == "__main__":
    print(solution(
["생닭", "인삼", "소주", "대추"], ["물", "인삼", "커피", "생닭", "소주", "사탕", "생닭", "대추", "쌀"]))