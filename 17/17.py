f = open("17.txt")
a =[int(x) for x in f]
mn = min(a)

cnt = 0 #Кол во пар
mx = -1

for i in range(len(a) - 1):
    if a[i]%16 == mn or a[i+1]%16 == mn:
        cnt += 1
        mx = max(mx, a[i] + a[i+1])

print(cnt, mx)