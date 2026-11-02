from relevance import Relevance

n = int(input())
a = list(map(int, input().split()))
d = int(input())
f = []
for i in range(d):
    f.append(list(map(int, input().split())))

system = Relevance(n, a, d, f)

q = int(input())
query = []

for i in range(q):
    query.append(list(map(int, input().split())))

for i in range(q):
    if query[i][0] == 1:
        for value in system.top(query[i][1]):
            print(value[1] + 1, end='')
        print()
    if query[i][0] == 2:
        system.update(query[i][1] - 1, query[i][2] - 1, query[i][3])


