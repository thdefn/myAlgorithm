def findMax(data):
    max = 0
    for i in range(9):
        if(data[i] > max):
            idx = i
            max = data[i]

    return max, idx


if __name__=="__main__":
    data = [int(input()) for w in range(9)]
    max, idx = findMax(data)
    print(max)
    print(idx+1)
