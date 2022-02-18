import json
import sys

def count_questions(data: dict):
    # вывести количество вопросов (questions)
    pass


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    pass


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    pass


def main(args):
     # загрузить данные из test.json файла
    with open(args) as json_file:
        data = json.load(json_file)
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)
    print(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    # main(sys.argv[0])
    main('test.json')