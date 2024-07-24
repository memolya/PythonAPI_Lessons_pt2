import requests

class Test_new_location():
    """Работа с новой локацией - создание, изменение, удаление, информация"""

    def test_create_location(self):
        """Метод для создания локации"""

        base_url = 'https://rahulshettyacademy.com' #базовый url
        key = '?key=qaclick123'                     #параметр для всех запросов

        # """Создание новой локации"""
        # post_resource = '/maps/api/place/add/json'  #реурс для метода post
        #
        # post_url = base_url + post_resource + key   #полная ссылка для метода post
        # print(post_url)
        #
        # json_create_new_location = {
        #     "location": {
        #
        #         "lat": -38.383494,
        #
        #         "lng": 33.427362
        #
        #     }, "accuracy": 50,
        #
        #     "name": "Frontline house",
        #
        #     "phone_number": "(+91) 983 893 3937",
        #
        #     "address": "29, side layout, cohen 09",
        #
        #     "types": [
        #
        #         "shoe park",
        #
        #         "shop"
        #
        #     ],
        #
        #     "website": "http://google.com",
        #
        #     "language": "French-IN"
        #
        # }
        #
        # result_post = requests.post(post_url, json = json_create_new_location) #в скобки помещаем ссылку и тело запроса
        # print(result_post.text)
        # print('Статус код: ' + str(result_post.status_code))
        # assert 200 == result_post.status_code
        # if result_post.status_code == 200:
        #     print('Успешно: мы создали новую локацию.')
        # else:
        #     print('Провал: запрос ошибочный.')
        #
        # check_post = result_post.json() #получать ответ в json формате и значения определенных полей из него
        # check_info_post = check_post.get('status') #получаем значение поля status (с кодом ответа)
        # print('Статус код: ' + check_info_post)
        # assert check_info_post == 'OK'
        # print('Статус ответа верен.')
        # place_id = check_post.get('place_id') #потом используем в методе put
        # print('ID места: ' + place_id)

        # """Проверка создания новой локации"""
        # place_id = '5555'
        # get_resource = '/maps/api/place/get/json'     #ресурс для метода get
        # #https://rahulshettyacademy.com/maps/api/place/get/json?key=qaclick123&place_id=05e78841ef75b5a76de73e6372910dc - полная ссылка (пример)
        # place_id_key = '&place_id='                   #добавляем к ключу place id
        # get_url = base_url + get_resource + key + place_id_key + place_id
        # print(get_url)
        # result_get = requests.get(get_url)            #в get запросах нет body
        # print(result_get.text)                        #выдаем результат запроса get
        #
        # assert 404 == result_get.status_code
        # if result_get.status_code == 404:
        #     print('Успешно: Валидная ошибка: локации не существует.')
        # else:
        #     print('Провал: запрос ошибочный.')


        """Изменение новой локации"""
        put_resource = '/maps/api/place/update/json'
        put_url = base_url + put_resource + key
        print(put_url)
        json_update_new_location = {
            "place_id": '5555', #изменение локации с неизвестным id
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json = json_update_new_location)
        print(result_put.text)
        print('Статус код: ' + str(result_put.status_code))

        assert 404 == result_put.status_code
        if result_put.status_code == 404:
            print('Успешно: валидная ошибка.')
        else:
            print('Провал: запрос ошибочный.')

        check_put = result_put.json()  #получать ответ в json формате и значения определенных полей из него
        check_info_put = check_put.get('msg')
        print('Сообщение: ' + check_info_put)
        assert check_info_put == 'Address successfully updated'
        print('Сообщение верно.')


new_place = Test_new_location() #экземпляр класса
new_place.test_create_location() #к экземпляру вызываем метод по созданию новой локации
