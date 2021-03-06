def black_box(page: int):
    if page <= 7922400:
        return True
    else:
        return False


def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.

    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_box) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.

    Уточнение:
        black_box возвращает True, если страница последняя
                  возвращает False, если страница не последняя.


    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """
    # Для выполнения этой задачи предлагаю использовать бинарный поиск его сложность logO(N)
    # в худшем случае нам понадобиться 27 +1 итерация

    last_page = 10 ** 7
    first_page = 0

    while first_page - last_page != 0:
        mid = (first_page + last_page) // 2
        if black_box(mid):
            first_page = mid + 1
        else:
            last_page = mid - 1

    if black_box(last_page):
        page = last_page
    else:
        page = last_page - 1

    return page


if __name__ == '__main__':
    main()
