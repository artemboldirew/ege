def F(x, p):
    if x <= 19 and p == 3: return True
    if x <= 19 and p < 3: return False
    if x > 19 and p == 3: return False
    if p%2 != 0:
        return F(x - 2, p + 1) and F(x - 5, p + 1) and F(x // 3, p + 1)
    else:
        return F(x - 2, p + 1) or F(x - 5, p + 1) or F(x // 3, p + 1)

for s in range(20, 100):
    if F(s,1):
        print(s)
        break