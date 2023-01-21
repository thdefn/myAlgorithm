#숫자 카드 게임
#n은 행의 개수, m은 열의 개수
#행을 골라 카드를 뽑는데, 최종적으로 가장 높은 숫자의 카드를 뽑아야 함
def solution(n,m,data):
    answer=0
    for i in range(n):
        min=10001
        for j in range(m):
            if(data[i][j]<min):
                min=data[i][j]
        if(min>answer):
            answer = min
    print(answer)

def answer(n,m,data):
    answer=0
    for i in range(n):
        minVal = min(data[i])
        answer = max(minVal, answer)
    print(answer)

if __name__ == '__main__':
    data=[[3,1,2],[4,1,4],[2,2,2]]
    data2=[[7,3,1,8],[3,3,3,4]]

    solution(3,3,data)
    solution(2,4,data2)

    answer(3,3,data)
