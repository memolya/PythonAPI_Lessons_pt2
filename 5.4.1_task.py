import requests
from get_category_541 import get_categories
category_list = get_categories()
class TestCreateRandomJokeCategory():
    """Класс для отправке запросов с целью получения шуток с Чаком Норрисом по заданной категории"""
    url = 'https://api.chucknorris.io/jokes/random'

    def test_create_random_joke(self, categories, expected_status_code):
        """Отправка запроса, проверка на соответствие категории, печать шутки."""
        for i in range(len(category_list)):
            path_joke_category = "?category=" + categories[i]
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
            #в поле joke_category у joke только один индекст, у category_list - много
            assert joke_category[0] == category_list[i], 'ОШИБКА, Статус-код не совпадает'
            print('Категория корректна')

            print("Тест прошел успешно")
            print('\n')


test = TestCreateRandomJokeCategory()
test.test_create_random_joke(category_list, 200)
