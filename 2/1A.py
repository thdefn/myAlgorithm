
def get_max(n, height, month , current):
    ans = -1
    for i in reversed(range(n)):
        if(month[i]==current):
            ans = height[i]
            break
    return ans




if __name__ == '__main__':
    n = int(input())
    height = [int(w) for w in input().split()]
    month = [int(w) for w in input().split()]
    current = int(input())
    answer = get_max(n, height, month, current)
    print(answer)