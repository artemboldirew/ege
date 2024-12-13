s = open("24.txt").readlines()[0]
g = "*-"
mx = -1

for i in range(1,10):
    s = s.replace("-0"+str(i), "+"+str(i))
    s = s.replace("*0" + str(i), "+" + str(i))

s = s.replace("--", "+")
s = s.replace("**", "+")
s = s.replace("*-", "+")
s = s.replace("-*", "+")
d = s.split("+")

f = list(filter(lambda x: x != "", d))
for i in range(len(f)):
    ln = len(f[i]) - int(f[i][0] in g) - int(f[i][-1] in g)
    mx = max(mx, ln)
print(mx)