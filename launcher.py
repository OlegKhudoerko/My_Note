import Interface.interface
import json_model
from json_model import save_file
from Controller.comtroller import create_new_note, show_all_notice, search_notice, delete_notice, edit_notice
import json


def start():
    print('\n\r Программа == Мои заметки!!! ==')
    while True:
        prog = input(f'\n{"#" * 50}\n'
                     f' 1 - Создать новую заметку\n'
                     f' 2 - Показать все\n'
                     f' 3 - Найти\n'
                     f' 4 - Изменить\n'
                     f' 5 - Удалить\n'
                     f' 0 - Выйти\n'
                     f'{"#" * 50}\n'
                     f' Выберите пункт меню: ')

        menu = {
            '1': 'run',
            '2': 'show_all',
            '3': 'search',
            '4': 'edit',
            '5': 'delete',
            '0': 'quit',
        }

        try:
            prog = menu[prog]
            if prog == 'quit':
                print("Вы вышли из программы!!!")
                exit(0)

            elif prog == 'run':
                run = create_new_note()
                save_file(run)
                print(f'{"—" * 50}\nЗаметка создана!\n{"—" * 50}')

            elif prog == 'show_all':
                if len(json_model.load_file()) == 0:
                    print("Список пуст. У Вас нет ни одной заметки!")
                show_all_notice()

            elif prog == 'search':
                choice = input(f'{"—" * 50}\n'
                               f'1 - Поиск по id\n'
                               f'2 - Поиск по заголовку\n'
                               f'3 - Поиск по тексту заметки\n'
                               f'4 - Поиск по дате и времени\n'
                               f'{"—" * 50}\n'
                               f'    Выберите пункт для поиска: ')

                search_type = {
                    '1': 'id',
                    '2': 'title',
                    '3': 'msg',
                    '4': 'data'
                }
                try:
                    choice = search_type[choice]
                    temp_list = json.load(open('notes.json', encoding='utf-8'))
                    if choice == 'id':
                        search = int(input('Введите id для поиска заметки (Например: 1):'))
                        search_notice(temp_list, search, 1)
                    elif choice == 'title':
                        search = input('Введите "Название заметки" для поиска (Например: Python):')
                        search_notice(temp_list, search, 2)
                    elif choice == 'msg':
                        search = input('Введите "Текст заметки" для поиска (Например: Сегодня семинар):')
                        search_notice(temp_list, search, 3)
                    elif choice == 'data':
                        search = input('Введите "Дату и время создания заметки" (Например: 06-02-2023 18:23:59):')
                        search_notice(temp_list, search, 4)
                except FileNotFoundError:
                    print(f'Вы еще не создали ни одной заметки!')
            elif prog == 'delete':
                temp_list = json.load(open('notes.json', encoding='utf-8'))
                print('Заметки которые вы создали:')
                show_all_notice()
                notice_val = int(input(f'\nВведите id заметки, которую хотите удалить: '))
                delete_notice(temp_list, 'id', notice_val)
            elif prog == 'edit':
                temp_list = json.load(open('notes.json', encoding='utf-8'))
                print('Заметки которые вы создали:')
                show_all_notice()
                notice_val = int(input(f'\nВведите id заметки, которую хотите изменить: '))
                edit_notice(temp_list, 'id', notice_val)
        except KeyError:
            print('Неверное значение')
