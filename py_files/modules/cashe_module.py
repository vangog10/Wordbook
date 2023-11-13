from json_module import dict_from_setting_json
import csv
import os

C_PATH = 'F:/Projects/PycharmProjects/WordBook/mp3_cashe'
H_PATH = 'F:/Projects/PycharmProjects/WordBook/other/history.csv'


def check_number_of_cache():
    if os.path.getsize(C_PATH) + os.path.getsize(H_PATH) > dict_from_setting_json()['cashe_size']:
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


def clear_histrory():
    if check_number_of_cache():
        with open(H_PATH, 'w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, fieldnames=['word', 'traslate', 'word_lang', 'translate_lang'])
            w.writeheader()



