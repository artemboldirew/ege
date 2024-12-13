mn = 10**10
for A1 in range(99):
    for A2 in range(A1 + 1, 100):
        flag = True
        for x in range(1, 300):
            if ((15<=x<=40) <= (((21<=x<=63) and (x < A1 or x > A2)) <= (x < 15 or x > 40))) == False:
                flag = False
                break
        if flag:
            mn = min(mn, A2-A1)
print(mn)