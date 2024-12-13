f = open("27_B.txt")
s = f.readline()
cls1 =[]
cls2 = []
cls3 = []
for s in f:
    x, y = map(float, s.replace(',','.').split())
    if 0 <= x <= 3 and 0 <= y <= 4:
        cls1.append([x, y])
    elif 2 <= x <= 5 and 7 <= y <= 11:
        cls2.append([x, y])
    elif 5 <= x <= 8 and 4 <= y <= 7:
        cls3.append([x, y])

def find_centre(arr):
    mn = 10**10
    x_c = 0
    y_c = 0
    for i in range(len(arr)):
        res = 0
        x1, y1 = arr[i]
        for j in range(len(arr)):
            x2, y2 = arr[j]
            res += ((x2-x1)**2 + (y2-y1)**2) ** 0.5
        if res < mn:
            mn = res
            x_c = x1
            y_c = y1
    return x_c, y_c

x1, y1 = find_centre(cls1)
x2, y2 = find_centre(cls2)
x3, y3 = find_centre(cls3)
print((x1+x2+x3)/3 * 10000, (y1+y2+y3)/3 * 10000)