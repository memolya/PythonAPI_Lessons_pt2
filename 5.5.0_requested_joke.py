import requests
#получаем список категорий через функцию в файле get_category_541
from get_category_541 import get_categories
#присваиваем глобальной переменной список категорий, который вернул get_category_541
category_list = get_categories()

class TestCreateRandomJokeCategory():
    """Класс для отправке запросов с целью получения шуток с Чаком Норрисом по заданной категории"""
    url = 'https://api.chucknorris.io/jokes/random'

    def category_invalid(self):
        """Функция для проверки валидности категории"""
        print('Ой, такой категории нет. Попробуйте снова: ')
        TestCreateRandomJokeCategory()
        test.test_create_requested_joke(category_list, 200)

    def more(self):
        """Функция для повторного использования программы"""
        print('Получить еще одну шутку? yes/no ')
        answer = input()
        if answer.lower() == 'yes':
            TestCreateRandomJokeCategory()
            test.test_create_requested_joke(category_list, 200)
        elif answer.lower() == 'no':
            print('Спасибо за использование программы, жду снова!')
            # если ответ "нет" - прерываем выполнение кода
            exit()
        #проверка на валидность ответа пользователя. Если невалиден - повторный запуск функции more()
        else:
            print('Простите, не понял вас.')

    def test_create_requested_joke(self, user_category, expected_status_code):
        """Запрос категории. Отправка запроса, проверка на соответствие категории, печать шутки."""
        user_category = input('Какую шутку вы хотите получить? Введите категорию из списка выше: ')
        #если категория есть в списке - выводим шутку и тесты
        if user_category in category_list:
            path_joke_category = "?category=" + user_category
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
            print('Категория шутки: ', joke_category)
            # в поле joke_category у joke только один индекст, у category_list - много
            assert joke_category[0] in category_list, 'ОШИБКА, Статус-код не совпадает'
            print('Категория корректна')

            print("Тест прошел успешно")
            print('\n')
            #спрашиваем у пользователя, хочет ли еще анекдотов
            self.more()
        else:
            #если шутка не прошла валидацию - показываем сообщение из category_invalid() о невалидности
            self.category_invalid()
            #после выдачи успешной шутки - спрашиваем, хочет ли еще анекдотов
            self.more()

test = TestCreateRandomJokeCategory()
test.test_create_requested_joke(category_list, 200)

