import 

n,m = map(int,input().split())
p = [_ for _ in range(1,n + 1)]
c = []
for _ in range(m):
    c.append(list(map(int,input().split()))[1:])

for i in itertools.combinations(p,2):
    i = list(i)
    r = 0
    for j in c:
        if i[0] in j and i[1] in j:
            r += 1
    if r == 0:
        print("No")
        exit()
print("Yes")