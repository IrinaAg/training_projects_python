# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageColor

# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

# def make_ticket(fio, from_, to, date):
#     pass

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


class TicketMaker:

    def __init__(self, template=None, font_path=None):
        # TODO Пути старайтесь указывать относительно рабочей директории (той, в которой лежит главный запускаемый файл)
        # TODO т.к. здесь у нас проект состоит из нескольких "мини"-проектов, то можно выполнить хитрый приём, явно указав
        # TODO на рабочую директорию.
        # TODO Сделать это можно либо в Run - Edit configurations
        # TODO Либо можно просто выделить нужную папку как source root
        # TODO для этого надо нажать на неё правой кнопкой - mark directory as - source root
        self.template = "/Users/agafonova/python_base/lesson_013/images/ticket_template.png" if template is None else template
        if font_path is None:
            self.font_path = "/Users/agafonova/python_base/lesson_013/python_snippets/fonts/Bressay Display.ttf"
            # TODO загрузите свой шрифт в репозиторий пожалуйста
        else:
            self.font_path = font_path

    def make_ticket(self, save_to=None):
        im = Image.open(self.template)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.font_path, size=16)

        y = im.size[1] - 225 - (10 + font.size) * 2
        fio = f"ИВАНОВ И.И."
        draw.text((50, y), fio, font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 190 - font.size
        from_ = f"ЗЕМЛЯ"
        draw.text((50, y), from_, font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 125 - font.size
        to = f"ЛУНА"
        draw.text((50, y), to, font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 125 - font.size
        date = f"09.12"
        draw.text((290, y), date, font=font, fill=ImageColor.colormap['black'])

        im.show()
        save_to = save_to if save_to else 'ticket_image.png'
        # TODO Сохранение изображений я бы советовал выполнять в отдельную папку
        # TODO А её наличие стоит проверить и, при необходимости, создать эту папку
        im.save(save_to)
        print(f'Post card saved az {save_to}')


if __name__ == '__main__':
    maker = TicketMaker()
    maker.make_ticket()

# TODO В основном всё верно, попробуете усложненную часть с argparse?
# TODO на всякий случай оставлю полезный источник https://habr.com/ru/post/144416/