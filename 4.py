import json
import sys


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    count = 0
    for i in data['game']['rounds']:
        count += len(i['questions'])
    print(count)


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    correct_answers = []
    for i in data['game']['rounds']:
        for a in i['questions']:
            correct_answers.append(a['correct_answer'])
    print(correct_answers)


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    time_to_answers = []
    for i in data['game']['rounds']:
        time_to_answers.append(i['settings']['time_to_answer'])
        for a in i['questions']:
            k= a.get('time_to_answer')
            if k is not None:
                time_to_answers.append(k)

    print(max(time_to_answers))



def main(args):
    # загрузить данные из test.json файла
    with open(args) as json_file:
        data = json.load(json_file)
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    main(sys.argv[1])
    # main('test.json')
