def get_op():
    op = int(input("1 - Импорт\n2 - Экспорт\n3 - Изменить строку\n4 - Удалчить строку\n5 - Выход\n"))
    return op

def get_data():
    name = input("Имя: ")
    surname = input("Фамилия: ")
    telephone = input("Телефон: ")
    data_str = name + " " + surname + " " + telephone + "\n"
    return data_str

def find_person():
    data_str = input("Введите параметр: ")
    print("")
    return data_str

def delete_person():
    data_str = input("Введите параметры для удаления: ")
    return data_str


#change_data()
        