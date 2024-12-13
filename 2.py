print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (x and y and w and z):
                    print(x, y, w, z)

#or - логическое ИЛИ
#and - логическое И
#<= - логическая импликация
#not() - логическое НЕ
