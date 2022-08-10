n = int(input())
k = 1
for i in range(1, n + 1):
    print(k)
    if i == k*(k + 1) // 2:
         k += 1
