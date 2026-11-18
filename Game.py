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

def fight_monster(inventory, hero_hp, monster_hp):

    while hero_hp > 0 and monster_hp > 0:

        if inventory["sword"] > 0:
            monster_hp = monster_hp - 15
            print("ты ударил мечом! У монстра осталась", monster_hp, "HP")
        else:
            monster_hp = monster_hp - 5
            print("Ты ударил кулаком! У монстра осталось", monster_hp, "HP")

        if monster_hp > 0:
            hero_hp = hero_hp - 10
            print("Монстер ударил тебя! У тебя осталось", hero_hp, "HP")
            print("-" * 20)
    if hero_hp > 0:
        print("Победа! Ты убил монстра!")
    else:
        print("ты проиграл... Монстер тебя одолел.")                     

print("WELCOME IN GAME")

while True:
    print("\nЧто будем делать?")
    print("1 - Выпить зелье")
    print("2 - Купить зелье (30 золото)")
    print("3 - Посмотреть ивентарь")
    print("4 - Пойти В лес на монстра")
    print("5 - выйти из игры")

    choice = input("Ведите цифру: ")

    if choice == "1":
        use_potion(inventory)
    elif choice == "2":
        buy_potion(inventory, 30)
    elif choice == "3":
        show_inventory(inventory)
    elif choice == "4":
        fight_monster(inventory, 100, 50)
    elif choice == "5":
        print("игра окончена. Пока! ")
        break
    else:
        print("нет такой команды")


