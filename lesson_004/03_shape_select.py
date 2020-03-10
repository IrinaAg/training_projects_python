# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def draw_figure(point, angle, length):
    for angle in range(0, 360 - angle, angle):
        v = sd.get_vector(start_point=point, angle=angle + 25, length=length, width=3)
        v.draw()
        point = v.end_point
    sd.line(start_point=point, end_point=point_0, width=3)


def triangle(point, angle, length):
    draw_figure(point=point, angle=angle, length=length)


def square(point, angle, length):
    draw_figure(point=point, angle=360 // 4, length=length)


def pentagon(point, angle, length):
    draw_figure(point=point, angle=360 // 5, length=length)


def hexagon(point, angle, length):
    draw_figure(point=point, angle=360 // 6, length=length)


point_0 = sd.get_point(300, 250)
side = 3

functions = {
    '0': {'func_name': 'треугольник', 'func': triangle},
    '1': {'func_name': 'квадрат', 'func': square},
    '2': {'func_name': 'пятиугольник', 'func': pentagon},
    '3': {'func_name': 'шестиугольник', 'func': hexagon}
}
print('Возможные фигуры:')
for code, val in functions.items():
    print(code, ':', val['func_name'])

while True:
    user_input = input('Введите желаемую фигуру >')
    if user_input in functions:
        function = functions[user_input]['func']
        function(point=point_0, angle=360 // side, length=100)
        break
    else:
        print("Вы ввели некорректный номер")

sd.pause()
