n = int(input())
a = list(map(int, input().split()))
print(max(sum(a) - 2 * sum(a[i:j]) + j - i \
for i in range(n) for j in range(i+1, n+1)))
