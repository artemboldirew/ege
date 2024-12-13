def change_base(num, base): #Перевод из десятичной в любую другую
    s = ""
    while num > 0:
        s += str(num % base)
        num //= base
    return s[::-1]

def find_divisors(num): #Поиск всех делителей
    divs = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divs.add(i)
            divs.add(num // i)
    return sorted(divs)

