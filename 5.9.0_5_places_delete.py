import requests

class Test_new_location():
    """Работа с новой локацией - создание, изменение, удаление, информация"""

    def __init__(self):
        """Складываем все необходимые в тестах ключи и ссылки"""
        self.base_url = 'https://rahulshettyacademy.com'     # базовый url self
        self.place_id_key = '&place_id='                     # добавляем к ключу place id ключ
        self.key = '?key=qaclick123'                         # параметр для всех запросов
        self.post_resource = '/maps/api/place/add/json'      # реурс метода post
        self.get_resource = '/maps/api/place/get/json'       # ресурс метода get
        self.delete_resource = '/maps/api/place/delete/json' # ресурс метода delete

    def test_create_location(self):
        """Метод для создания локации"""

        for i in range(5):
            post_url = self.base_url + self.post_resource + self.key  #полная ссылка для метода post
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

            result_post = requests.post(post_url, json=json_create_new_location)  #в скобки помещаем ссылку и тело запроса
            print(result_post.text)
            print('Статус код: ' + str(result_post.status_code))

            assert 200 == result_post.status_code, 'Провал: запрос ошибочный.'
            print('Успешно: мы создали новую локацию.')

            check_post = result_post.json()  #получать ответ в json формате и значения определенных полей из него
            check_info_post = check_post.get('status')  #получаем значение поля status (с кодом ответа)
            print('Статус код: ' + check_info_post)
            assert check_info_post == 'OK', 'Ошибка: статус ответа не верен.'
            print('Статус ответа верен.')
            place_id = check_post.get('place_id')
            print('ID места: ' + place_id)

            print('Создание локаций прошло успешно.')
            print('\n')  #завершение части теста с созданием локаций

            """Запись в файл"""
            fw = open('places_590.txt', 'a+')
            fw.write(place_id + '\n')  #вставляем значение поля place_id из check_post.get('place_id) # +'\n' - с новой строки

    def check_txt_id(self):
        """Проверка создания новой локации при помощи файла places_590.txt"""

        with (open('places_590.txt', 'r') as file):  #открываем файл для чтения
            for line in file:  #перебираем файл построчно
                place_id = line.rstrip()  #удаляем символы переноса строк
                get_url = self.base_url + self.get_resource + self.key + self.place_id_key + place_id
                print('ID места: ' + place_id)
                print('Get_url = ' + get_url)
                result_get = requests.get(get_url)
                print(result_get.text)  # выдаем результат запроса get

                assert 200 == result_get.status_code, 'Провал: запрос ошибочный.'
                print('Успешно: ID локации в файле places_590 валиден.')
                print('Статус код: ' + str(result_get.status_code))
                print('\n')  #разделение тестов

    def delete_places(self):
        delete_url = self.base_url + self.delete_resource + self.key
        print(delete_url)

        with open('places_590_removed.txt', 'a') as m: #открываем целевой файл для записи
            with open('places_590.txt') as f:          #открываем исходный файл для чтения
                for i, line in enumerate(f):
                    if i == 1 or i == 3:            #Ищем нужные строки - 2 и 4
                        place_id = line.rstrip()    #с rstrip, чтобы в place_id не включался перенос строки
                        print('Локация под удаление: ' + place_id)

                        """Удаление созданной локации"""
                        json_delete_new_location = {
                            "place_id": place_id
                        }
                        result_delete = requests.delete(delete_url, json=json_delete_new_location)

                        print(result_delete.text)
                        print('Статус код: ' + str(result_delete.status_code))

                        assert 200 == result_delete.status_code
                        if result_delete.status_code == 200:
                            print('Успешно: удаление новой локации прошло успешно.')
                        else:
                            print('Провал: запрос ошибочный.')

                        check_status = result_delete.json()  # получать ответ в json формате и значения определенных полей из него
                        check_info_status = check_status.get('status')
                        print('Сообщение: ' + str(check_info_status))
                        assert check_info_status == 'OK', 'Ошибка: сообщение не верно.'
                        print('Сообщение верно.\n')

                        """Проверка удаления новой локации"""
                        get_url = self.base_url + self.get_resource + self.key + self.place_id_key + line
                        result_get = requests.get(get_url)
                        print(result_get.text)
                        print('Статус код: ' + str(result_get.status_code))

                        assert 404 == result_get.status_code, 'Провал: запрос ошибочный.'
                        print('Успешно: проверка удаления новой локации прошла успешно.')

                        check_msg = result_get.json()  # получать ответ в json формате и значения определенных полей из него
                        check_msg_info = check_msg.get('msg')
                        print('Сообщение: ' + check_msg_info)
                        assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists", 'Ошибка: неправильное сообщение об ошибке.'
                        print('Сообщение верно.\n')

                    else:                              #пишем id локаций не с номером 2 и 4 в целевой файл
                        m.write(line)

            print('Тестирование Test_new_location завершено успешно. Существующие локации находятся в файле places_590_removed.txt.')


test_1 = Test_new_location()
test_1.test_create_location()   #создание мест и получение place_id с проверками кодов
test_1.check_txt_id()           #проверка существования мест с id из файла places_590.txt
test_1.delete_places()          #удаление 2 и 4 локации и сохранение оставшихся в файл places_590_removed.txt
