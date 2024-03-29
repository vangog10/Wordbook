from functools import cache
import json


JSON = 'F:/Projects/PycharmProjects/WordBook/JSONs/setting.json'
LANGUAGE_PACK = 'F:/Projects/PycharmProjects/WordBook/JSONs/languages/{}.json'


@cache
def dict_from_setting_json() -> dict:
    with open(JSON, 'r', encoding='utf8') as f:
        return json.load(f)


@cache
def dict_from_languages_json() -> dict:
    way = LANGUAGE_PACK.format(dict_from_setting_json()['language'])
    with open(way, 'r', encoding='utf8') as f:
        return json.load(f)


def change_setting(changes: dict) -> None:
    data_for_json: dict = {
        "font": [
            "Times New Roman",
            17 + int(changes['-SLIDER-']),
            "bold"
        ],
        "theme": changes[0],
        "language": changes[1],
        "cashe_size": changes['-CASHE-']
    }
    with open(JSON, 'w', encoding='utf8') as f:
        json.dump(data_for_json, f)

