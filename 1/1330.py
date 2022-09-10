
if __name__ == "__main__":
    a, b = [int(w) for w in input().split()]
    # 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
    if(a>b):
        print(">")
    elif(a<b):
        print("<")
    else:
        print("==")