n = int(input())

people = list(map(int , input().split()))

people.sort()

# 1 2 3 3 4
# 1 1
# 3 1 + 2
# 6 1 + 2 + 3
# 9 1 + 2 + 3 + 3
# 13 1 + 2 + 3 + 3 + 4

# 32 
 
result = 0
fin = 0
for i in people:
    result += i 
    fin += result
    
print(fin)