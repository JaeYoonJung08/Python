
n = int(input())
sum = 0
i = 1
while sum <= n:
    sum += i
    if sum >= n:
        print(i)
        break
    i += 1


n = int(input())

s = 0
t = 0
while s<n :
  t = t+1
  s = s+t
  
print(t)