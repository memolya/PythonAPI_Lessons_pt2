import requests

class TestCreateJoke():
    """Класс рандомной шутки"""
    #глобальная переменная ссылки
    url = 'https://api.chucknorris.io/jokes/random'
    def test_create_random_joke_category(self):
        """Класс с шутками по категориям, включает:
                 отправку запроса, проверка на статус-код, проверка на соответствие категории,
                  проверку на содержание имени Chuck в теле шутки, печать шутки."""

        category = 'explicit'
        path_random_joke_category = f"?category={category}"
        url_random_joke_category = self.url + path_random_joke_category
        print(url_random_joke_category)

        result = requests.get(url_random_joke_category)
        print(result.json())

        print(f'Статус-код: {result.status_code}')
        assert result.status_code == 200, 'ОШИБКА, Статус-код не совпадают'
        print('Статус-код корректен')

        check_joke = result.json()
        joke_value = check_joke.get("value")
        print(joke_value)

        #Обратите внимание, что при сравнении мы используем индекс 0 - joke_category[0].
        # Дело в том, что поле categories хранит в себе список, и если мы просто укажем joke_category, то система выдаст нам ошибку.
        # Так как список содержит всего один элемент, то для того, чтобы к нему обратиться, нам необходимо выбрать индекс [0].
        joke_category = check_joke.get("categories")
        print(joke_category)
        assert joke_category[0] == category, 'ОШИБКА, Статус-код не совпадает'
        print('Категория корректна')

        assert_word = 'Chuck'
        assert assert_word in joke_value, 'ОШИБКА, Проверочное слово отсутствует'
        print('Проверочное слово присутствует')
        print("Тест прошел успешно")

start = TestCreateJoke()
start.test_create_random_joke_category()

