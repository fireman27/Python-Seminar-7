def main_menu() -> int:
    print('Главное меню.')
    menu_list = ['Показать все контакты', 'Создать контакт', 'Изменить контакт',
                'Удалить контакт', 'Выход']
    for i in range(len(menu_list)):
        print(f'{i + 1}. {menu_list[i]}')   
    user_input = int(input('Введи команду => '))
    if user_input in range(1, 6):
        return user_input
    else:
        print('Команда введена некорректно. Поробуй ещё раз!')  


def exit_program():
    print('Завершение программы.')
    exit()

   
def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(v, end=' ')
            print()


def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False


def create_contact():
    print('Создание нового контакта.')
    new_contact = dict()
    new_contact['фамилия'] = input('   Введите фамилию => ')
    new_contact['имя'] = input('   Введите имя => ')
    new_contact['телефон'] = input('   Введите телефон => ')
    new_contact['коментарий'] = input('   Введите комментарий => ')
    return new_contact


def del_contact(db: list):
    fc = input('Введите фамилию и имя через пробел => ').split()
    for item in db:
        if item.get('фамилия') == fc[0] and item.get('имя') == fc[1]:
            db.remove(item)
            print(f'{item} удален из базы')
            break
    else:
        print('Удалять нечего - такого контака нет!')
    return db


def change_contact(db: list):
    fc = input('Введите фамилию и имя через пробел => ').split()
    for item in db:
        if item.get('фамилия') == fc[0] and item.get('имя') == fc[1]:
            change_list = ['фамилия', 'имя', 'телефон', 'коментарий']
            for i in range(len(change_list)):
                print(f'{i + 1}. {change_list[i]}') 
            item_for_change = input('Введите, что хотите изменить =>  ')
            new_item = dict()
            match int(item_for_change):
                case 1: # lastname
                    new_item['фамилия'] = input('   Введите новую фамилию =>: ')
                    new_item['имя'] = item.get('имя')
                    new_item['телефон'] = item.get('телефон')
                    new_item['коментарий'] = item.get('коментарий')
                case 2: # firstname
                    new_item['фамилия'] = item.get('фамилия')
                    new_item['имя'] = input('   Введите новое имя =>: ')
                    new_item['телефон'] = item.get('телефон')
                    new_item['коментарий'] = item.get('коментарий')
                case 3: # phone
                    new_item['фамилия'] = item.get('фамилия')
                    new_item['имя'] = item.get('имя')
                    new_item['телефон'] = input('   Введите новый телефон =>: ')
                    new_item['коментарий'] = item.get('коментарий')
                case 4: # comment
                    new_item['фамилия'] = item.get('фамилия')
                    new_item['имя'] = item.get('имя')
                    new_item['телефон'] = item.get('телефон')
                    new_item['коментарий'] = input('   Введите новый комментарий =>: ')
            db.append(new_item)
            db.remove(item)
            print(f'{item} заменен на {new_item}')
            break
    else:
        print('Изменять нечего - такого контака нет!')
    return db 