from Interface.interface import Notes
from datetime import datetime
from json_model import load_file, rewrite_file


def create_new_note():

    title = create_tittle()
    msg = create_msg()
    new_notes = Notes(title, msg)
    ready_note = save_note_to_data(new_notes.get_id(), title, msg, new_notes.get_change_date())
    return ready_note


def create_tittle():

    title = input('Введите заголовок заметки: ')
    return title


def create_msg():

    msg = input('Введите текст заметки: ')
    return msg


def save_note_to_data(id, title, msg, date):

    date_list = {
        'id': id,
        'title': title,
        'msg': msg,
        'date': date
    }
    return date_list


def show(dictonary):

    for value in dictonary.values():
        print(f'{value}   ', end='')
    print()



def show_search(data):

    global _data
    print(f'\n\nНайдены следующие заметки:')
    for x in data:
        _data = x
    show(_data)


def show_all_notice():

    try:
        data = load_file()
        for line in data:
            show(line)
    except FileNotFoundError:
        print(f'{"-" * 15}\nЗаметок нет\n{"-" * 15}')


def search_notice(data_list, search_data, choice):

    if choice == 1:
        data = list(filter(lambda x: x['id'] == search_data, data_list))
        if not data:
            print(f'\n\nЗаметок с таким id нет.\n\n')
        else:
            show_search(data)

    elif choice == 2:
        data = list(filter(lambda x: x['title'] == search_data, data_list))
        if not data:
            print(f'\n\nЗаметок с таким заголовком не найдено.\n\n')
        else:
            show_search(data)

    elif choice == 3:
        data = list(filter(lambda x: x['msg'] == search_data, data_list))
        if not data:
            print(f'\n\nЗаметки с таким текстом не найдены.\n\n')
        else:
            show_search(data)

    elif choice == 4:
        data = list(filter(lambda x: x['date'] == search_data, data_list))
        if not data:
            print(f'\n\nЗаметок на эту дату и время не найдено.\n\n')
        else:
            show_search(data)


def delete_notice(data_list: list, key, value):

    for index, dict_ in enumerate(data_list):
        if key in dict_ and dict_[key] == value:
            data_list.remove(dict_)
            print(f'Произведено удаление заметки: ', end='')
            show(dict_)

        rewrite_file(data_list)


def edit_notice(data_list: list, key, value):

    for index, dict_ in enumerate(data_list):
        if key in dict_ and dict_[key] == value:
            new_title = ''
            new_msg = ''
            change_title = input(f'Заменить название заметки: "{dict_.get("title")}"?\n'
                                 f'1 - Заменить\n'
                                 f'2 - Оставить\n')
            if change_title == '1':
                new_title = input(f'Введите новое название заметки: ')
            elif change_title == '2':
                new_title = dict_.get('title')
            else:
                print('\nНеверное значение!\n')
            change_msg = input(f'Заменить текст заметки: "{dict_.get("msg")}"?\n'
                               f'1 - Заменить\n'
                               f'2 - Оставить\n')
            if change_msg == '1':
                new_msg = input(f'Введите новый текст заметки: ')
            elif change_msg == '2':
                new_msg = dict_.get('msg')
            else:
                print('\nНеверное значение!\n')
            data_list[index] = {
                'id': value,
                'title': new_title,
                'msg': new_msg,
                'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            }
            show(dict_)
            print(f'Заметка изменена на')
            show(data_list[index])

    rewrite_file(data_list)
