import requests

class TestCreateRandomJokeCategory():
    """Класс включающий сценарии по отправке запросов, с целью получения шуток с Чаком Норрисом по заданной категории"""

    url = 'https://api.chucknorris.io/jokes/random'

    def test_create_random_joke_category_positive(self, category, expected_status_code):
        """Позитивный тест по получению рандомной шутки по определенной категории, включает:
                 отправку запроса, проверка на статус-код, проверка на соответствие категории, печать шутки."""

        path_random_joke_category = f"?category={category}"
        url_random_joke_category = self.url + path_random_joke_category
        print(url_random_joke_category)

        result = requests.get(url_random_joke_category)
        print(result.json())

        print(f'Статус-код: {result.status_code}')
        assert result.status_code == expected_status_code, 'ОШИБКА, Статус-код не совпадают'
        print('Статус-код корректен')

        check_joke = result.json()
        joke_value = check_joke.get("value")
        print(joke_value)

        joke_category = check_joke.get("categories")
        print(joke_category)
        assert joke_category[0] == category, 'ОШИБКА, Статус-код не совпадает'
        print('Категория корректна')

        # Различные проверки
        print("Тест прошел успешно")



start_test = TestCreateRandomJokeCategory()
start_test.test_create_random_joke_category_positive('animal', 200)