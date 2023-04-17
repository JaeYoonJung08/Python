#못품

# n = input()

# for i in n:
#     if (i == '0' or i == '1'):
#         s += int(i)
#     elif (i >= '2' and i <= '9'):
#         s *= int(i)

# print(s)

#책답
n = input()

data = int(n[0])

for i in range(1, len(n)):
    num = int(n[i])
    if (data <= 1 or num <= 1):
        data += num
    else:
        data *= num

print(data)