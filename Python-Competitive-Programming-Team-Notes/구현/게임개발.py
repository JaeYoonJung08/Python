n, m = map(int, input().split())
loc_x , loc_y, see = map(int, input().split())

arr = [n for _ in range(n)]
for i in range(n):    
	arr[i] = list(map(int, input().split()))

count = 1
math = 0
rotation = 0
#왼0 밑3 오2 위1
check_loc_x = [0, 1, 0, -1]
check_loc_y = [-1, 0, 1, 0]
while True:
    # 1. 자신이 보고 있는 왼쪽을 검사 하는 알고리즘
    # 0, -1 빼기
    if (math == 360):
        math = 0
    if (see == 0):
        i = 0
        check_x = loc_x + check_loc_x[i]
        check_y = loc_y + check_loc_y[i]
    elif (see == 3):
        i = 1
        check_x = loc_x + check_loc_x[i]
        check_y = loc_y + check_loc_y[i]
    elif (see == 2):
        i = 2
        check_x = loc_x + check_loc_x[i]
        check_y = loc_y + check_loc_y[i]
    elif (see == 1):
        i = 3
        check_x = loc_x + check_loc_x[i]
        check_y = loc_y + check_loc_y[i]    
    print("loc_x, loc_y check_x, check_y", loc_x, loc_y, check_x, check_y, end= ' ')
    if (arr[check_x][check_y] == 0):
        math += 90
        loc_x = check_x
        loc_y = check_y
        count += 1
        rotation = 0
    elif (arr[check_x][check_y] == 1 or arr[check_x][check_y] == 2):
        math += 90
        rotation += 1
    if (arr[loc_x][loc_y] == 0):
            arr[loc_x][loc_y] = 2
    if (math == 90):
        see = 3
    elif (math == 180):
        see = 2
    elif (math == 270):
        see = 1
    elif (math == 360):
        see = 0 
    print("see" , see)
    # if (rotation == 4):
    #     break
    if (rotation == 4):
        if (see == 3):
            loc_x = loc_x + 0
            loc_y = loc_y + 1
            rotation = 0
            if(arr[loc_x][loc_y] == 1):
                    break
        elif (see == 2):
            loc_x = loc_x - 1
            loc_y = loc_y + 0
            rotation = 0
            if(arr[loc_x][loc_y] == 1):
                    break
        elif (see == 1):
            loc_x = loc_x + 0
            loc_y = loc_y - 1
            rotation = 0
            if(arr[loc_x][loc_y] == 1):
                    break
        elif (see == 0):
            loc_x = loc_x + 1
            loc_y = loc_y + 0
            rotation = 0
            if(arr[loc_x][loc_y] == 1):
                    break



print(see ,loc_x, loc_y ,count)
# # 2. 그 왼쪽이 갈 수 있는 지 판단 갈 수 있으면 
# # 왼쪽 방향으로 회전 한 후 앞으로 이동

# # 3. 없으면 그냥 왼쪽으로 회전만 하고 다시 1로 이동

# # 4. 네 방향 모두 이미 가본 칸 이거나 바다이면 
# # 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1로 이동

# #만약 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없으면 멈춤.



n , m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y , direction = map(int, input().split())
d[x][y] = 1
count = 1
turn_time = 0
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if (d[nx][ny] == 0 and array[nx][ny] == 0):
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        print("x, y, dir, nx, ny", x, y, direction, nx, ny)
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(x, y, count)


