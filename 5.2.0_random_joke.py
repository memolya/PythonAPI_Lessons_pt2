import requests

class Test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        """Создание случайной шутки"""

        url = 'https://api.chucknorris.io/jokes/random'
        print(url)
        result = requests.get(url)
        print('Статус-код: ' + str(result.status_code))

        # сравнение результатов. нет ошибки - значит, совпадает
        assert 200 == result.status_code
        print('Успешно. Мы получили новую шутку')

        # кодировка ответа в utf-8 (обычно по умолчанию, но на всякий случай)
        result.encoding = 'utf-8'
        print(result.text)

        # проверка json для отдельно взятых полей в ответе
        check = result.json()
        # check_info = check.get("categories")
        # print(check_info)
        # assert check_info == []
        # print('Категория верна')
        check_info_value = check.get("value")
        print(check_info_value)
        name = 'Chuck'
        if name in check_info_value:
            print('Chuck присутствует')
        else:
            print('Chuck отсутствует')


random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()