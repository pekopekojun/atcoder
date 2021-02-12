n = input()
s = input()

x = 0
m = 0
for i in s:
    if i == "I":
        x += 1
    else:
        x -= 1
    m = max([m, x])
print(m)
