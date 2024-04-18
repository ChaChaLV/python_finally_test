import easygui
from database import *

def main():
    load_database()

    while True:
        choice = easygui.choicebox(
            "Выберите действие:",
            "Меню Телефонного справочника",
            ["/show Просмотр контактов",
             "/add Добавить контакт",
             "/find Поиск контакта",
             "/delete Удалить контакт",
             "/update Обновить контакт",
             "/exit Выход"]
        )

        if choice.startswith('/show'):
            view_contacts()
        elif choice.startswith('/add'):
            fields = ["Имя", "Номер", "Доп. номер (если есть)", "Email"]
            contact_info = easygui.multenterbox("Введите данные для добавления контакта:", "Добавить контакт", fields)
            if contact_info and contact_info[0]:
                add_contact(contact_info)
        elif choice.startswith('/find'):
            name = easygui.enterbox("Введите имя для поиска:")
            if name:
                search_contact(name)
        elif choice.startswith('/delete'):
            name = easygui.enterbox("Введите имя для удаления контакта:")
            if name:
                delete_contact(name)
        elif choice.startswith('/update'):
            name = easygui.enterbox("Введите имя контакта для обновления:")
            if name:
                fields = ["Новый номер", "Новый email"]
                contact_info = easygui.multenterbox("Введите новую информацию:", "Обновить контакт", fields)
                if contact_info:
                    update_contact(name, contact_info)
        elif choice.startswith('/exit'):
            break
        else:
            easygui.msgbox("Неверный выбор. Попробуйте снова.", "Ошибка")

if __name__ == "__main__":
    main()
