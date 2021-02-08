k, s = map(int, input().split())
cnt = 0

if k*3 < s:
    print(cnt)
    exit()

for x in range(k+1):
    if x + (k*2) < s:
        continue
    if x > s:
        break
    for y in range(k+1):
        if x + y + k < s:
            continue
        if x + y > s:
            break
        cnt += 1
print(cnt)
