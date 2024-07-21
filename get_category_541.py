#функция для получения списка категорий для основного скрипта
import requests

def get_categories():
    """Получаем список категорий"""
    url_categories = 'https://api.chucknorris.io/jokes/categories'
    result_categories = requests.get(url_categories)
    #преобразуем полученный json в list
    categories = list(result_categories.json())
    #печатаем результат работы скрипта
    print(url_categories)
    print('Categories:', categories)
    #возвращаем список categories для использования в основном скрипте
    return categories

