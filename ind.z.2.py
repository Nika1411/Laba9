#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 11
# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения (список из трех чисел). Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть упорядочены по датам рождения; вывод на экран информации о
# человеке, номер телефона которого введен с клавиатуры; если такого нет, выдать на
# дисплей соответствующее сообщение.

import json
import sys

if __name__ == '__main__':
    clo = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            surname = input("Фамилия ")
            name = input("Имя ")
            number = int(input("Номер телефона "))
            year = list(map(int, input("Дата рождения в формате: дд,мм,гггг ").split('.')))

            if not number:
                print("Поле не заполнено")
                exit(1)

            clos = {
                'surname': surname,
                'name': name,
                'number': number,
                'year': year,
            }
            clo.append(clos)
            if len(clo) > 1:
                clo.sort(key=lambda item: item.get('year', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 20,
                '-' * 20,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^20} | {:^20} | {:^20} | {:^15} |'.format(
                    "№",
                    "Фамилия ",
                    "Имя",
                    "Номер телефона",
                    "Дата рождения"
                )
            )
            print(line)
            for idx, worker in enumerate(clo, 1):
                print(
                    '| {:^4} | {:^20} | {:^20} | {:^20} | {:^15} |'.format(
                        idx,
                        worker.get('surname', ''),
                        worker.get('name', ''),
                        worker.get('number', ''),
                        worker.get('year', 0)
                    )
                )
            print(line)

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)

            with open(parts[1], 'r') as f:
                clo = json.load(f)

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)

            with open(parts[1], 'w') as f:
                json.dump(clo, f)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить ученика;")
            print("list - вывести список учеников;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
