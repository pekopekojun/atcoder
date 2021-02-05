n = input()
t = input().split()
m = input()

p_x = []
while int(m) > len(p_x):
    p_x.append(input().split())

t_array = [int(i) for i in t]

for p in p_x:
    t_tmp = t_array[:]
    t_tmp[int(p[0])-1] = int(p[1])
    print(sum(t_tmp))
