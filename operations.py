import json

# Загрузка данных телефонной книги из файла phone_book.json
def load_phone_book():
    try:
        with open('phone_book.json', 'r', encoding='utf-8') as file:
            phone_book = json.load(file)
    except FileNotFoundError:
        phone_book = {}
    return phone_book

# Сохранение данных телефонной книги в файл phone_book.json
def save_phone_book(phone_book):
    with open('phone_book.json', 'w', encoding='utf-8') as file:
        json.dump(phone_book, file, ensure_ascii=False, indent=4)

# Импорт данных телефонной книги из указанного файла
def import_phone_book(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            imported_data = json.load(file)
        save_phone_book(imported_data)
        print("Данные успешно импортированы.")
    except FileNotFoundError:
        print("Указанный файл не найден.")

# Добавление нового контакта в телефонную книгу
def add_contact(name, number, email, extra_number=None):
    phone_book = load_phone_book()
    contact_info = {'номер': number, 'email': email}
    if extra_number:
        contact_info['доп_номер'] = extra_number
    phone_book[name] = contact_info
    save_phone_book(phone_book)

# Просмотр контактов в телефонной книге
def view_contacts():
    phone_book = load_phone_book()
    if phone_book:
        for name, contact in phone_book.items():
            print(f'Имя: {name}, Номер: {contact["номер"]}, Доп. номер: {contact.get("доп_номер", "нет")}, Email: {contact["email"]}')
    else:
        print('Телефонная книга пуста.')

# Поиск контакта
def search_contact(name):
    phone_book = load_phone_book()
    if name in phone_book:
        contact = phone_book[name]
        print(f'Имя: {name}, Номер: {contact["номер"]}, Email: {contact["email"]}')
    else:
        print(f'Контакт {name} не найден.')

# Удаление контакта
def delete_contact(name):
    phone_book = load_phone_book()
    if name in phone_book:
        del phone_book[name]
        save_phone_book(phone_book)
        print(f'Контакт {name} удалён.')
    else:
        print(f'Контакт {name} не найден.')

# Обновление контакта
def update_contact(name, number, email):
    phone_book = load_phone_book()
    if name in phone_book:
        phone_book[name] = {'номер': number, 'email': email}
        save_phone_book(phone_book)
        print(f'Контакт {name} изменен.')
    else:
        print(f'Контакт {name} не найден.')