if __name__=="__main__":
    n = int(input())
    data = [input() for w in range(n)]

    for i in range(n):
        sum = 0
        cnt = 0
        for r in list(data[i]):
            if(r == "O"):
                cnt += 1
                sum += cnt
            else:
                cnt = 0
        print(sum)
