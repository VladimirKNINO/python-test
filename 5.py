import os
import re
import threading


def task1():
    # в папке test найти все файлы filenames вывести колличество
    count = 0
    path = 'test'
    # используя функцию walk пройдемся по папкам и найдем все файлы
    for path, dirs, files in os.walk(path):
        for file in files:
            # проверяем название файлов по шаблону начинается на filenames (filenames с припиской "копия" ,
            #  и дубликаты по названию)
            if file.startswith('filenames'):
                count += 1
    return count





def task2():
    # в папке test найти все email адреса записанные в файлы
    # Шаблон регулярки
    pattern = '\w+@\w+.[a-zA-z]+'

    email_all = []
    path = 'test'
    for path, dirs, files in os.walk(path):
        for file in files:
            path_file = os.path.join(path, file)  # обьединяем путь и имя файла
            with open(path_file, 'r') as h:
                my_file = h.readlines()
                for line in my_file:
                    email =re.search(pattern, line)
                    if email:
                        g = email.group()  # re.Match переводим в стр
                        email_all.append(g)

    return email_all




def get_pаth():
    """ Возвращает пути всех файлов в папке test"""
    path_files = []
    for path, dirs, files in os.walk('test'):
        for file in files:
            path_file = os.path.join(path, file)
            path_files.append(path_file)
    return path_files

def get_email(path):
    """ Возвращает  email адреса записанный в файле"""
    pattern = '\w+@\w+.[a-zA-z]+'
    with open(path, 'r') as h:
        my_file = h.readlines()
        for line in my_file:
            email = re.search(pattern, line)
            if email:
                print(email)



def task3():
    for path in get_pаth():
        t = threading.Thread(target=get_email(path))
        t.start()


print(task3())
def main():
    task1()
    task2()
    # дополнительно: придумать над механизм оптимизации 2-й задачи (используя threading)
    task3()

if __name__ == '__main__':
    main()
