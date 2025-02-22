a = input()
b = input()
c = input()

la = len(a)
lb = len(b)
lc = len(c)

minl = min(la, lb, lc)
maxl = max(la, lb, lc)
mid = (la + lb + lc) - minl - maxl

if mid == (maxl + minl) / 2:
    print('YES')
else:
    print('NO')