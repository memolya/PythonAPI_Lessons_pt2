import requests

"""Получаем список категорий"""
def get_categories():
    url_categories = 'https://api.chucknorris.io/jokes/categories'
    result_categories = requests.get(url_categories)
    categories = list(result_categories.json())
    print(url_categories)
    print('Categories:', categories)
    return categories

