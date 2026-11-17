inventory = {
    "potion": 3,
    "sword": 1,
    "gold": 100

}
def use_potion(inventory):
    if inventory["potion"] > 0:
        inventory["potion"] = inventory["potion"] - 1
        print("Вы выпили potion! Осталось:", inventory["potion"])
    else:
        print("У вас нет potion")  

def buy_potion(inventory, price):
    if inventory["gold"] >= price:
        inventory["gold"] = inventory["gold"] - price
        inventory["potion"] = inventory ["potion"] + 1
        print("вы купили potion! Gold осталось:", inventory["gold"])
    else:
        print("не хватает gold!")

def show_inventory(inventory):
    for item, count in inventory.items():
        print(item, "-", count)             

print("WELCOME IN GAME")

while True:
    print("\nЧто будем делать?")
    print("1 - Выпить зелье")
    print("2 - Купить зелье (30 золото)")
    print("3 - Посмотреть ивентарь")
    print("4 - Выйти из игры")

    choice = input("Ведите цифру: ")

    if choice == "1":
        use_potion(inventory)
    elif choice == "2":
        buy_potion(inventory, 30)
    elif choice == "3":
        show_inventory(inventory)
    elif choice == "4":
        print("Игра окончена. Пока! ")
        break
    else:
        print("Нет такой команды")
                

