if __name__=="__main__":
    n = int(input())
    for i in range(n):
        a, b = input().split()
        a = int(a)
        data = list(b)
        print("".join(w*a for w in data))
