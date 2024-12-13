from itertools import product
"""Определите количество 12-ричных пятизначных чисел, в записи которых ровно одна цифра 7 и не более трёх цифр с числовым значением, превышающим 8."""

alp = "0123456789AB"
cnt1 = 0

for x1 in "123456789AB":
    for x2 in alp:
        for x3 in alp:
            for x4 in alp:
                for x5 in alp:
                    word = x1 + x2 + x3 + x4 + x5
                    if word.count("7") == 1 and (word.count("9") + word.count("A") + word.count("B")) < 4:
                        cnt1 += 1
print("Ответ 1 способ:", cnt1)

cnt2 = 0
for x in product(alp, repeat=5):
    word = "".join(x)
    if word[0] != "0" and word.count("7") == 1 and (word.count("9") + word.count("A") + word.count("B")) < 4:
        cnt2 += 1
print("Ответ 2 способ:", cnt2)