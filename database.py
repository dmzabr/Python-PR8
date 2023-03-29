import view


def add_data(data_str):
    with open("file.txt", "a", encoding="UTF-8") as f:
        f.write(data_str)
        
def find_person(data_str):
    with open("file.txt", "r", encoding="UTF-8") as f:
        lst_str = f.readlines()
        for worker in lst_str:
            if data_str in worker:
                print(worker,end="")
        
def delete_person():
    data_str = input("Введите хар-ку для удаления строки: ")
    user_lst = []
    with open("file.txt", "r", encoding="UTF-8") as f:
        lst = f.readlines()
        for line in lst:
            if data_str in line:
                user_lst.append(line)
    print(*user_lst)
    answer = int(input("Введите строчку, коорую хочешь удалить: "))
    new_str = ""
    with open("file.txt", "w", encoding="UTF-8") as f:
        for line in lst:
            if user_lst[answer-1] != line:
                f.write(line)
            else:
                f.write(new_str)
    print("Готово!")
                
def change_data():
    data_str = input("Введите хар-ку для изменения строки: ")
    user_lst = []
    with open("file.txt", "r", encoding="UTF-8") as f:
        lst = f.readlines()
        for line in lst:
            if data_str in line:
                user_lst.append(line)
    print(*user_lst)
    answer = int(input("Введите строчку, коорую хочешь изменить: "))
    print("Введите новые параметры строки")
    new_str = view.get_data()
    with open("file.txt", "w", encoding="UTF-8") as f:
        for line in lst:
            if user_lst[answer-1] != line:
                f.write(line)
            else:
                f.write(new_str)
    print("Готово!")