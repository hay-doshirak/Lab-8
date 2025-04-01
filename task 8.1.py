slovarik = {"Россия": "Москва", "Китай": "Пекин", "Аргентина" : "Буэнос-Айрес", "Япония": "Токио"}
for key in slovarik:
    print(key, "-", slovarik[key])
    
s = input("Введите название страны: ")
if s in slovarik:
    print("Столица - ", slovarik[s])
else: print("Страны пока нет в нашем перечне(")

sort_slovar = list(slovarik.keys())
sort_slovar.sort()
print("Отсортированный словарь: ")
for k in sort_slovar:
    print(k,"-", slovarik[k])