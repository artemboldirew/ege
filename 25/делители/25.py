def find_divisors(num): #Поиск всех делителей
    divs = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divs.add(i)
            divs.add(num // i)
    return sorted(divs)


arr = []
i = 800001
while len(arr) < 5:
    div = find_divisors(i)
    if len(div) == 0:
        i += 1
        continue

    m = min(div) + max(div)
    if m%10==4:
        arr.append([i, m])
    i += 1

print(arr)