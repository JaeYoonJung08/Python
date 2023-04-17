n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))
array.sort(reverse=True)
#print(array)
result = []
for j in range(n):
    result.append(array[j] * (j + 1))
print(max(result))

#https://covenant.tistory.com/128