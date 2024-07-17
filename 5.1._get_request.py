import requests

url = 'https://api.chucknorris.io/jokes/random'
print(url)
result = requests.get(url)
print('Статус-код: ' + str(result.status_code))

#сравнение результатов. нет ошибки - значит, совпадает
assert 200 == result.status_code
print('Успешно. Мы получили новую шутку')

#кодировка ответа в utf-8 (обычно по умолчанию, но на всякий случай)
result.encoding = 'utf-8'
print(result.text)