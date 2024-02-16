import pytest

from unit_tests.ex_1 import (
    create_course_list,
    get_extremum_courses,
    get_len_courses,
    get_max_duration,
    get_min_duration,
)


courses = [
        "Java-разработчик с нуля",
        "Fullstack-разработчик на Python",
        "Python-разработчик с нуля",
        "Frontend-разработчик с нуля",
    ]
mentors = [
        [
            "Филипп Воронов",
            "Анна Юшина",
            "Иван Бочаров",
            "Анатолий Корсаков",
            "Юрий Пеньков",
            "Илья Сухачев",
            "Иван Маркитан",
            "Ринат Бибиков",
            "Вадим Ерошевичев",
            "Тимур Сейсембаев",
            "Максим Батырев",
            "Никита Шумский",
            "Алексей Степанов",
            "Денис Коротков",
            "Антон Глушков",
            "Сергей Индюков",
            "Максим Воронцов",
            "Евгений Грязнов",
            "Константин Виролайнен",
            "Сергей Сердюк",
            "Павел Дерендяев",
        ],
        [
            "Евгений Шмаргунов",
            "Олег Булыгин",
            "Александр Бардин",
            "Александр Иванов",
            "Кирилл Табельский",
            "Александр Ульянцев",
            "Роман Гордиенко",
            "Адилет Асканжоев",
            "Александр Шлейко",
            "Алена Батицкая",
            "Денис Ежков",
            "Владимир Чебукин",
            "Эдгар Нуруллин",
            "Евгений Шек",
            "Максим Филипенко",
            "Елена Никитина",
        ],
        [
            "Евгений Шмаргунов",
            "Олег Булыгин",
            "Дмитрий Демидов",
            "Кирилл Табельский",
            "Александр Ульянцев",
            "Александр Бардин",
            "Александр Иванов",
            "Антон Солонилин",
            "Максим Филипенко",
            "Елена Никитина",
            "Азамат Искаков",
            "Роман Гордиенко",
        ],
        [
            "Владимир Чебукин",
            "Эдгар Нуруллин",
            "Евгений Шек",
            "Валерий Хаслер",
            "Татьяна Тен",
            "Александр Фитискин",
            "Александр Шлейко",
            "Алена Батицкая",
            "Александр Беспоясов",
            "Денис Ежков",
            "Николай Лопин",
            "Михаил Ларченко",
        ],
    ]
durations = [14, 20, 12, 20]

courses_list = create_course_list(
courses, mentors, durations
    )
min_duration = get_min_duration(durations)
max_duration = get_max_duration(durations)
maxes, minis = get_len_courses(durations)
courses_max, courses_min = get_extremum_courses(
        maxes, minis, courses_list
    )
def test_create_course_list():
    assert len(courses_list) == 4

def test_get_min_duration():
    assert min_duration == 12

def test_get_max_duration():
    assert max_duration == 20

def test_get_extremum_courses():

    assert courses_max == ["Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

    assert courses_min == ["Python-разработчик с нуля"]