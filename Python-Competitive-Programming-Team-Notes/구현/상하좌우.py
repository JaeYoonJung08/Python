# n = int(input())
# move = input().split()
# x, y = 1, 1
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]

# move_list = ['R', 'L', 'U', 'D']

# for move_S in move:
#     for i in range(len(move_list)):
#         #print(i)
#         if (move_S == move_list[i]):
#             xx = x + dx[i]
#             yy = y + dy[i]
#     if xx < 1 or yy < 1 or xx > n or yy >n:
#         continue
#     x , y = xx, yy
    


# print(x, y)



n = int(input())
move = input().split()
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
move_list = ['R', 'L', 'U', 'D']


for i in move:
    for j in range(len(move_list)):
        if (i == move_list[j]):
            nx = x + dx[j]
            ny = y + dy[j]
            
    if (nx < 1 or ny < 1 or nx > n or ny > n):
        continue
    x = nx
    y = ny

print(x , y)