n = int(input())      #개수를 입력받아 n에 정수로 저장
a = input().split()

for i in range(n-1, -1, -1):
    print(a[i], end = ' ')