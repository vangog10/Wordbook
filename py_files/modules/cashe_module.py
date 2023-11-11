from json_module import dict_from_setting_json
import os

C_PATH = 'F:/Projects/PycharmProjects/WordBook/mp3_cashe'


def check_number_of_cache():
    if os.path.getsize(C_PATH) // 8 > dict_from_setting_json()['cashe_size']:
        return True
    return False


def remove_cache():
    if check_number_of_cache():
        for filename in os.listdir(C_PATH):
            file_path = os.path.join(C_PATH, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f'Ошибка при удалении файла {file_path}. {e}')



