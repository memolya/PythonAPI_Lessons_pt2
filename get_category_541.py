import requests

class Categories():
    """Получаем список категорий"""

    def get_categories(self):
        url_categories = 'https://api.chucknorris.io/jokes/categories'
        result_categories = requests.get(url_categories)
        categories = list(result_categories.json())
        print(url_categories)
        print('Categories:', categories)
        return categories


test_1 = Categories()
test_1.get_categories()
