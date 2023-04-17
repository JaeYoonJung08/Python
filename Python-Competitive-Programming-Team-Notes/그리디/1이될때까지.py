N, K = map(int, input().split())


# while (1):
#     target = (N // K) * K
#     count = N - target
#     N = target
#     if N < K:
#         break
#     count += 1
#     N = N // K
    
# 정재윤의 잘못된 풀이
# count = 0
# while (1):
#     if(N % K == 0):
#         break
#     N -= 1
#     count += 1

# while (1):
#     if (N == 1):
#         break
#     N //= K
#     count += 1

# print(count)

# 다시 풀기 
#count = 0
#while(1):
#    if (N == 1):
#        break
#    if (N % K != 0):
#        N -=1
#        count += 1
#    elif(N % K == 0):
#        N //= K
#        count += 1


#책 닶
count = 0
while True:
    target = (N // K) * K
    count += (N - target)
    print("target, count ",target, count)
    N = target 
    if N < K:
        break
    count += 1
    N //= K
    print("N", N)
count += (N - 1)


print(count)

    
# print(2// 3)