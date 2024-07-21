#функция для получения списка категорий для основного скрипта
import requests

def get_categories():
    """Получаем список категорий"""
    url_categories = 'https://api.chucknorris.io/jokes/categories'
    result_categories = requests.get(url_categories)
    categories = list(result_categories.json())
    print(url_categories)
    print('Categories:', categories)
    return categories

