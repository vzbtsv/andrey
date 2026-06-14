f = [int(x) for x in open("17_29349.txt").readlines()]
minn = min(list(filter(lambda x: x % 123 == 0 and x > 0, f)))

res = []
for i in range(len(f) - 1):
    x1 = f[i]
    x2 = f[i + 1]

    if x1 + x2 < minn:
        res.append(x1 + x2)

print(len(res), (max(res)))
