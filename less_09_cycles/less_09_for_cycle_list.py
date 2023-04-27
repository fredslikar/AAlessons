basket = ["Milk", "Bread", "Sugar", "Butter", "Cheese", "Pasta"]

for f in basket:
    some = f + "+"
    if some == "Sugar+":
        print(some)

for f in basket:
    print(len(f))
    if len(f) > 5:
        print(f)
    else:
        c = f + "+"
        print(c)

#Для ограничения количества циклов используєтся запись [:3], что означает провести все ціклі, кроме первіх трех
#Цикл для кроме певіх трех єлементов [3:].
for f in basket[:3]:
    print("[:3] Кроме последних трех")
    print(str(len(f))+f)


for f in basket[2:]:
    print("[2:] Кроме первіх двух")
    print(str(len(f))+f)



