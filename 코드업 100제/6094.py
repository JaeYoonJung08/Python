n = int(input())      #개수를 입력받아 n에 정수로 저장
a =  input().split()
for i in range(n):
    a[i] = int(a[i])
d = a[0]

for i in range(n-1, 0, -1):
    if(a[i] < d):
        d = a[i]

print(d)
