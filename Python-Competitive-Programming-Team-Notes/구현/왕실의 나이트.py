# alp, number = input()

# alpha = ['a', 'b', 'c', 'd', 'e', 'f']
# count = 0

# compare_list = []
# x, y = 0,int(number)
# count_answer = 0
# for alphas in alpha:
#     count += 1
#     if (alphas == alp):
#         break
# x = count
# print(x, y)
# move_horse1 = [2,  2, 1, -1, 1, -1, -2, -2]
# move_horse2 = [1, -1, 2, 2, -2, -2, -1, 1]
# # 1. 오른쪽 밑 오른쪽  2, 1
# # 2. 오른쪽 밑 왼쪽  2, -1
# # 3. 오른쪽 오른쪽 밑 1, 2
# # 4. 오른쪽 오른쪽 위 -1, 2
# # 5. 왼쪽 왼쪽 밑 1, -2
# # 6. 왼쪽 왼쪽 위 -1, -2
# # 7. 위 왼쪽 -2, -1 
#  # 8. 위 오른쪽 -2, 1
# for i in range(8):
#     check_x = x + move_horse1[i]
#     check_y = y + move_horse2[i]
#     #print(check_x, check_y)
#     if ((check_x >= 1 and check_x <= 8) and (check_y >= 1 and check_y <= 8)):
#         count_answer += 1
#         #print(i)
#         print(check_x, check_y)

# print(count_answer)



n = input()

first = (int(ord(n[0])) - int(ord('a'))) + 1
second = int(n[1])


move_horse1 = [2,  2, 1, -1, 1, -1, -2, -2]
move_horse2 = [1, -1, 2, 2, -2, -2, -1, 1]
# 1. 오른쪽 밑 오른쪽  2, 1
# 2. 오른쪽 밑 왼쪽  2, -1
# 3. 오른쪽 오른쪽 밑 1, 2
# 4. 오른쪽 오른쪽 위 -1, 2
# 5. 왼쪽 왼쪽 밑 1, -2
# 6. 왼쪽 왼쪽 위 -1, -2
# 7. 위 왼쪽 -2, -1 

count = 0
for i in range(8):
    dx = first + move_horse1[i]
    dy = second + move_horse2[i]
    if (dx < 1 or dy < 1 or dx > 9 or dy > 9):
        continue
    count += 1
    
print(count)
