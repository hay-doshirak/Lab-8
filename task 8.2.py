slovarik = {1: "АВЕИНОРСТ", 2: "ДКЛМПУ", 3: "БГЁЬЯ", 4: "ЙЫ", 5: "ЖЗХЦЧ", 8: "ШЭЮ", 10: "ФЩЪ"}
slovo = input("Введите любое слово: ").upper()
cost=0
for s in slovo:
    for key, value in slovarik.items():
        if s in value:
            cost+=key
            break
print("Стоимость слова ", slovo.lower(), "-", cost, " очков.")

