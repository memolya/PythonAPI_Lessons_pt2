import requests
result_categories_list = []

class GetCategories():
    """Получаем список категорий"""
    def __init__(self):
        pass
    def get_categories(self):
        url_categories = 'https://api.chucknorris.io/jokes/categories'
        categories = requests.get(url_categories)
        result_categories = requests.get(url_categories)
        result_categories_list.append(result_categories.json())
        print(url_categories)
        print(result_categories.json())
        print('\n')
        # print(type(result_categories.json()))

class TestCreateRandomJokeCategory():
    """Класс для отправке запросов с целью получения шуток с Чаком Норрисом по заданной категории"""

    url = 'https://api.chucknorris.io/jokes/random'

    def test_create_random_joke(self, expected_status_code):
        """Отправка запроса, проверка на соответствие категории, проверка на содержание имени Chuck в теле шутки, печать шутки."""

        # Цикл для итерации по списку категорий
        for i in range(len(result_categories_list)):
            category = result_categories_list[i]
            print(category[i])

            path_joke_category = "?category=" + category[i]
            url_joke_category = self.url + path_joke_category
            print(url_joke_category)

            result = requests.get(url_joke_category)
            print(result.json())

            print(f'Статус-код: {result.status_code}')
            assert result.status_code == expected_status_code, 'Ошибка: статус-код не совпадает'
            print('Статус-код корректен')

            check_joke = result.json()
            joke_value = check_joke.get("value")
            print(joke_value)

            joke_category = check_joke.get("categories")
            print(joke_category)
            assert joke_category[i] == category[i], 'ОШИБКА, Статус-код не совпадает'
            print('Категория корректна')

            print("Тест прошел успешно")
            print('\n')

test_1 = GetCategories()
test_1.get_categories()
test_2 = TestCreateRandomJokeCategory()
test_2.test_create_random_joke(200)
