# -*- coding: utf-8 -*-
def get_score(result):
    global analized_res, total
    analized_res = {}
    total = 0
    frames = 0
    for _ in result:
        for i, k in enumerate(zip(result.replace('X', 'X-')[0::2], result.replace('X', 'X-')[1::2]), start=1):
            analized_res[i] = k
    for k, v in analized_res.items():
        frames += 1
        check_errors(v)
        game_result(v)
    print(result, '–', total)
    if frames != 10:
        raise Exception('Не правильное количество фреймов!')
    return total


def game_result(v):
    global total
    if 'X' in v:
        total += 20
    elif '/' in v:
        total += 15
    elif '-' in v:
        total += 0
    else:
        total += int(v[0]) + int(v[1])
    return v


def check_errors(v):
    if '0' in v:
        raise ValueError('Введено неправильное значение')
    elif '/' in v[0]:
        raise ValueError('Spare на первом броске')
    elif 'X' in v[1]:
        raise ValueError('Strike на втором броске')
    if v[0].isdigit() and v[1].isdigit() and int(v[0]) + int(v[1]) >= 10:
        raise ValueError('Введено неправильное значение, сумма одного фрейма больше 9 очков')
