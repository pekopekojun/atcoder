n = int(input())
a = list(map(int, input().split()))

if n % 2 == 0:
    for i in range(n):
        if a[i] % 2 == 0:
            print("0")
            exit()
else:
    for i in range(n):
        if a[i] % 2 != 0:
            print("0")
            exit()

memo = []
for left in range(n):
    right = (n - 1) - left
    memo.append(abs(left-right))
memo.sort()
a.sort()

if not memo == a:
    print("0")
else:
    ans = 2**int(n/2) % (10**9+7)
    print(ans)
