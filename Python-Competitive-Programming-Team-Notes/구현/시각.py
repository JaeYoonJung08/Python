# n = int(input())

# h, m, s = 00, 00, 00
# h = h + n

# for i in range(h):
#     for j in range(61):
#         for k in range(61):
#             second_check_front = j / 10
#             second_check_back = j % 10
#             if (second_check_back == 3 or second_check_front == 3):
#                 print(i, j)
#                 three_check_front = k / 10
#                 three_check_back = k % 10
#                 if (three_check_back == 3 or three_check_front == 3):
#                     print(k, end= " ")
#             if (k == 60):
#                 break 


n = int(input())

count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
    
print(count)