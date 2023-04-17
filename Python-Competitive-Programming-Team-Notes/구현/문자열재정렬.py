# n = input()
# alpha = []

# x = 0
# for i in n:
#     if (i >= 'A' and i <= 'Z'):
#         alpha.append(i)
#     elif (i >= '0' and i <= '9'):
#         x += int(i)
# alpha.sort()

# if x != 0:
#     alpha.append(str(x))
# print(alpha)



n = input()
alpha = []

x = 0
for i in n:
    if i.isalpha():
        alpha.append(i)
    else:
        x += int(i)
alpha.sort()

if x != 0:
    alpha.append(str(x))
print(''.join(alpha))