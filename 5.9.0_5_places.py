import requests

class Test_new_location():
    """Работа с новой локацией - создание, изменение, удаление, информация"""

    def test_create_location(self):
        """Метод для создания локации"""

        self.base_url = 'https://rahulshettyacademy.com' #базовый url  #self для возможности использования в следующей функции
        self.key = '?key=qaclick123'                     #параметр для всех запросов

        """Создание новой локации"""

        for i in range(5):
            post_resource = '/maps/api/place/add/json'  #реурс для метода post

            post_url = self.base_url + post_resource + self.key   #полная ссылка для метода post
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

            print('Создание локаций прошло успешно.')
            print('\n')                                #завершение части теста с созданием локаций

            """Запись в файл"""
            fw = open('places_590.txt', 'a+')
            fw.write(place_id + '\n')                         #вставляем значение поля place_id из check_post.get('place_id) # +'\n' - с новой строки


    def check_txt_id(self):
        """Проверка создания новой локации при помощи файла places_590.txt"""

        get_resource = '/maps/api/place/get/json'  # ресурс для метода get
        place_id_key = '&place_id='  # добавляем к ключу place id

        with open('places_590.txt', 'r') as file:                   #открываем файл для чтения
            for line in file:                                       #перебираем файл построчно
                line_checked = line.rstrip()                        #удаляем символы переноса строк
                get_url = self.base_url + get_resource + self.key + place_id_key + line_checked # + line_checked = place_id (из цикла по файлу)
                print('ID места: ' + line_checked)
                print('Get_url = ' + get_url)
                result_get = requests.get(get_url)
                print(result_get.text)  # выдаем результат запроса get

                assert 200 == result_get.status_code
                if result_get.status_code == 200:
                    print('Статус код: ' + str(result_get.status_code))
                    print('Успешно: ID локации в файле places_590 валиден.')
                    print('\n') #разделение тестов

                else:
                    print('Провал: запрос ошибочный.')
                    print('\n')  # разделение тестов

#создание мест и получение place_id с проверками кодов
test_1 = Test_new_location()
test_1.test_create_location()
test_1.check_txt_id()