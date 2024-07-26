import requests

class Test_new_location():
    """Работа с новой локацией - создание, изменение, удаление, информация"""

    def test_create_location(self):
        """Метод для создания локации"""

        base_url = 'https://rahulshettyacademy.com' #базовый url
        key = '?key=qaclick123'                     #параметр для всех запросов

        """Создание новой локации"""

        for i in range(5):
            post_resource = '/maps/api/place/add/json'  #реурс для метода post

            post_url = base_url + post_resource + key   #полная ссылка для метода post
            print(post_url)

            json_create_new_location = {
                "location": {

                    "lat": -38.383494,

                    "lng": 33.427362

                }, "accuracy": 50,

                "name": "Frontline house",

                "phone_number": "(+91) 983 893 3937",

                "address": "29, side layout, cohen 09",

                "types": [

                    "shoe park",

                    "shop"

                ],

                "website": "http://google.com",

                "language": "French-IN"

            }

            result_post = requests.post(post_url, json = json_create_new_location) #в скобки помещаем ссылку и тело запроса
            print(result_post.text)
            print('Статус код: ' + str(result_post.status_code))

            assert 200 == result_post.status_code
            if result_post.status_code == 200:
                print('Успешно: мы создали новую локацию.')
            else:
                print('Провал: запрос ошибочный.')

            check_post = result_post.json()            #получать ответ в json формате и значения определенных полей из него
            check_info_post = check_post.get('status') #получаем значение поля status (с кодом ответа)
            print('Статус код: ' + check_info_post)
            assert check_info_post == 'OK'
            print('Статус ответа верен.')
            place_id = check_post.get('place_id')
            print('ID места: ' + place_id)

            """Запись в файл"""
            fw = open('places_590.txt', 'a')
            fw.write(place_id+'\n')                         #вставляем значение поля place_id из check_post.get('place_id) # +'\n' - с новой строки
            fw.close()

test_1 = Test_new_location()
test_1.test_create_location()