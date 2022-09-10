

if __name__ == "__main__":
    a, b = [int(w) for w in input().split()]
    # a / b
    # 10^-9 이하의 오차를 허용한다 0.00000001
    print(str(float(a)/float(b)))

