if __name__=="__main__":
    data = [int(w) for w in input().split()]
    if(data[0]==1):
        for i in range(8):
            if(data[i]!=i+1):
                print("mixed")
                break
            else:
                if(i==7):
                    print("ascending")
    elif(data[0]==8):
        for i in range(8):
            if(data[i]!=8-i):
                print("mixed")
                break
            else:
                if(i==7):
                    print("descending")
    else:
        print("mixed")


def solution(delay, N):
    answer = 0
    #1+1*2+(1*2)+(1*2+1*2)+(1*2+1*2+1*2)
    a = [] # 분열 불가
    b = 1 # 분열 가능
    for i in range(1,N+1):
        b = b
        for j in range(b):
            a.append(delay)



    return answer
