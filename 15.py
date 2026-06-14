


def f(x, a1, a2):
    A = a1 <= x <= a2
    B = 22 <= x <= 40
    C = 32 <= x <= 50

    return (not A) <= (B == C)



Ox = []

for x in [22, 32, 40, 50]:
    Ox.append(x - 1)
    Ox.append(x)
    Ox.append(x + 1)

res = []
for a1 in Ox:
    for a2 in Ox:
        if a2 > a1:
            if all([f(x, a1, a2) for x in Ox]):
                res.append(a2 - a1)


print(min(res))



