# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class Human:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None

    def __str__(self):
        return ('Я - {}, сытость {}, степень счастья {}'.format(
            self.name, self.fullness, self.happiness))

    def eat(self):
        if self.house.food >= 20:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food -= 20
            Husband.total_eat += 20
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} вьехал в дом'.format(self.name), color='cyan')

    def stroke_cat(self):
        self.happiness += 5


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return 'Во доме еды осталось {}, денег осталось {}, грязи {}%'.format(self.food, self.money, self.dirt)


class Husband(Human):
    total_money = 0
    total_eat = 0

    def __init__(self, name):
        super().__init__(name=name)
        self.pets = []

    def __str__(self):
         return super().__str__()

    def work(self):
        if self.house.money <= 500:
            cprint('{} сходил на работу'.format(self.name), color='blue')
            self.house.money += 150
            self.fullness -= 10
            self.happiness -= 10
            Husband.total_money += 150

    def gaming(self):
        cprint('{} играл целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 20

    def pick_up(self, cat):
        cprint('{} подобрал кота'.format(self.name), color='cyan')
        cat.house = self.house
        self.pets.append(cat)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.house.dirt > 90:
            self.happiness -= 10
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.happiness <= 10:
            cprint('{} умирает от депрессии'.format(self.name), color='red')
            self.gaming()
        elif self.house.money < 500:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.stroke_cat()
        else:
            self.gaming()


class Wife(Human):
    total_fur_coat = 0
    total_eat = 0

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
         return super().__str__()

    def shopping(self):
        if self.house.money >= 70:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 70
            self.house.food += 70
            self.happiness -= 10
            self.fullness -= 10
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_cat_food(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой коту'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        if self.house.money >= 350:
            cprint('{} купила шубу'.format(self.name), color='magenta')
            self.house.money -= 350
            self.happiness += 60
            Wife.total_fur_coat += 1

    def clean_house(self):
        cprint('{} убралась в доме'.format(self.name), color='blue')
        self.fullness -= 20
        self.house.dirt -= 100
        self.happiness -= 10

    def act(self):
        self.house.dirt += 5
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness <= 0:
            cprint('{} умера...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food < 70:
            self.shopping()
        elif self.house.cat_food < 50:
            self.shopping_cat_food()
        elif self.happiness <= 10:
            cprint('{} умирает от депрессии'.format(self.name), color='red')
            self.buy_fur_coat()
        elif self.happiness <= 20:
            self.stroke_cat()
        elif self.house.dirt >= 100:
            self.clean_house()
        elif dice == 1:
            self.stroke_cat()
        elif dice == 2:
            self.shopping()
        else:
            self.eat()

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.house = house

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()
        else:
            self.soil()

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.cat_food -= 5
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} спит'.format(self.name), color='blue')
        self.fullness -= 10

    def soil(self):
        cprint('{} дерет обои'.format(self.name), color='green')
        self.fullness -= 10
        self.house.dirt += 5


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Human):
    total_eat = 0

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
            Child.total_eat += 10

    def sleep(self):
        cprint('{} спит'.format(self.name), color='blue')
        self.fullness -= 10

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} приехал в дом'.format(self.name), color='cyan')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик', house=home)

members = [
    serge,
    masha,
    kolya
]

pets = [
    murzik
]

for member in members:
    member.go_to_the_house(house=home)

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    for member in members:
        member.act()
    for pet in pets:
        pet.act()
    # serge.act()
    # masha.act()
    # kolya.act()
    # murzik.act()
    print('----- в конце дня -----')
    for member in members:
        cprint(member, color='cyan')
    for pet in pets:
        cprint(pet, color='cyan')
    cprint(home, color='cyan')
    # cprint(serge, color='cyan')
    # cprint(masha, color='cyan')
    # cprint(kolya, color='cyan')
    # cprint(murzik, color='cyan')
print('---------- За {} дня ----------'.format(day))
print('Было заработано денег - {}'.format(Husband.total_money))
print('Было сьедено еды - {}'.format(Husband.total_eat + Wife.total_eat + Child.total_eat))
print('Было куплено шуб - {}'.format(Wife.total_fur_coat))

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

#зачет!