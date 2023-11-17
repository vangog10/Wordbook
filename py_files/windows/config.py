import PySimpleGUI as sg
from py_files.modules.json_module import dict_from_setting_json, dict_from_languages_json
from py_files.modules.csv_module import list_csv, list_file, get_history

config: dict = {
    'theme_list': [
        'Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack',
        'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14',
        'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6',
        'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4',
        'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4',
        'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12',
        'DarkGrey13', 'DarkGrey14', 'DarkGrey15', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6',
        'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4',
        'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal',
        'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5',
        'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging',
        'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1',
        'LightBlue2',
        'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1',
        'LightBrown10',
        'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5',
        'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1',
        'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7',
        'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5',
        'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple',
        'Python', 'PythonPlus', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1',
        'SystemDefaultForReal',
        'Tan', 'TanBlue', 'TealMono', 'Topanga'
    ],
    'languages': ['ru', 'en'],
    'languages_list': ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian',
                       'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)',
                       'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english',
                       'esperanto',
                       'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german',
                       'greek',
                       'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong',
                       'hungarian',
                       'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada',
                       'kazakh',
                       'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian',
                       'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi',
                       'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish',
                       'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho',
                       'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili',
                       'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek',
                       'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu']

}

sg.theme(dict_from_setting_json()['theme'])

difficulty: dict[int:int] = {
    1: 20,  # very easy
    2: 10,  # easy
    3: 5,  # medium
    4: 3,  # hard
    5: 2  # very hard
}

layout: dict = {
    'main_menu': [
        [sg.Text(dict_from_languages_json()['     WordBook'], font=('Harlow Solid Italic', 35, 'bold'), expand_x=True,
                 expand_y=True)],
        [sg.Button(dict_from_languages_json()['Open dictionaries'], font=dict_from_setting_json()['font'],
                   expand_x=True, expand_y=True)],
        [sg.Button(dict_from_languages_json()['+   Create new   +'], font=dict_from_setting_json()['font'],
                   expand_x=True, expand_y=True)],
        [sg.Button(dict_from_languages_json()['🛠    Settings    🛠'], font=dict_from_setting_json()['font'],
                   expand_x=True, expand_y=True)],
        [sg.Button(dict_from_languages_json()['Translator'], font=dict_from_setting_json()['font'],
                   expand_x=True, expand_y=True)]
    ],
    'settings': [
        [sg.Text(dict_from_languages_json()['Settings'], font=dict_from_setting_json()['font'], expand_x=True)],

        [sg.Text(dict_from_languages_json()['Theme:'], font=('Times New Roman', 14, 'bold')),
         sg.Combo(config['theme_list'], default_value=dict_from_setting_json()['theme']),
         sg.Text(dict_from_languages_json()['language:'], font=('Times New Roman', 14, 'bold')),
         sg.Combo(config['languages'], default_value=dict_from_setting_json()['language'])],
        [sg.Text(dict_from_languages_json()['Font size'], font=('Times New Roman', 14, 'bold')),
         sg.Slider(range=(1, 5), default_value=3, resolution=0.5, orientation='h', key='-SLIDER-')],
        [sg.Txt(dict_from_languages_json()['Cashe size:'], font=('Times New Roman', 14, 'bold')), sg.InputText(default_text=dict_from_setting_json()['cashe_size'], font=('Times New Roman', 14, 'bold'), s=(10, 14), key='-CASHE-'),
         sg.Txt(dict_from_languages_json()['Bytes'], font=('Times New Roman', 14, 'bold')), sg.Button(dict_from_languages_json()['Clear'], font=('Times New Roman', 14, 'bold'), expand_x=True)],
        [sg.Button(dict_from_languages_json()['About program'], size=(15, 2), expand_x=True)],
        [sg.OK(size=(10, 2)), sg.Cancel(size=(10, 2))]
    ],
    'list_of_dictionaries': [
        [sg.Button(dict_from_languages_json()['+ Create new '], font=["Times New Roman", 12]),
         sg.Button('🔁', font=["Times New Roman", 12])],
        [sg.Table(headings=[dict_from_languages_json()['number'], dict_from_languages_json()['name']], key='-TABLE-',
                  values=list_csv, justification='left', num_rows=20, font=["Times New Roman", 12],
                  enable_events=True)]
    ],
    'new dictionary': [
        [sg.Text(dict_from_languages_json()['name:']), sg.InputText(expand_x=True, key='-NAME-')],
        [sg.OK(), sg.Cancel()]
    ],
    'file': [
        [sg.Button(dict_from_languages_json()['+ Add new word'], font=["Times New Roman", 12]),
         sg.Button('🔁', font=["Times New Roman", 12]),
         sg.Button(dict_from_languages_json()['Learn'], font=["Times New Roman", 12])],
        [sg.Table(headings=['   №  ', dict_from_languages_json()[' word '], dict_from_languages_json()[' translate '],
                            dict_from_languages_json()[' progress ']],
                  values=list_file, justification='left', key='-FILE-', num_rows=20, font=["Times New Roman", 12],
                  enable_events=True)]
    ],
    'new_word': [
        [sg.Text(dict_from_languages_json()['word:']), sg.InputText(expand_x=True)],
        [sg.Text(dict_from_languages_json()['translation:']), sg.InputText(expand_x=True)],
        [sg.OK(), sg.Cancel()]
    ],
    'mod': [
        [sg.Text(dict_from_languages_json()['mod']),
         sg.Combo(values=[dict_from_languages_json()['find translation'], dict_from_languages_json()['find word'],
                          dict_from_languages_json()['match words'], dict_from_languages_json()['write word'],
                          dict_from_languages_json()['write translation'], dict_from_languages_json()['word from audio']],
                  key='-MOD-')],
        [sg.Text(dict_from_languages_json()['difficult']),
         sg.Slider(range=(1, 5), default_value=3, resolution=1, orientation='h', key='-DIFFICULTY-')],
        [sg.OK(), sg.Cancel()]
    ],
    'about_program': [
        [sg.Listbox(
            values=[
                '                                                  WordBook',
                '    Wordbook - это словарь для изучения иностранных слов',
                '',
                'Вес программы: 12 КВ.',
                'Версия Python: 3.11+.',
                '',
                '                                             Как пользоваться',
                '',
                '    После запуска программы, у вас появится меню с тремя кнопками: "Настройки", "Открыть словари" и "Создать новый".',
                '    В разделе "Настройки" вы можете поменять следующие параметры:',
                '',
                '\t* Язык. Доступен английский и русский.',
                '\t* Тема. Выберите тему по вкусу.',
                '\t* Шрифт. Можно немного изменить размер',
                '',
                'Также вы можете нажать кнопку "О программе", и прочитать этот файл). После того, как вы нажмёте "ОК", программа закроет-',
                'ся, чтобы обновить настройки. Запустите её снова и наслаждайтесь!',
                '    С помощью кнопки "Создать новый" вы создаёте новый файл (формата .csv), в котором будут хранится ваши слова. Переза-',
                'пустите программу, чтобы всё успешно создалось. Чтобы увидеть все созданные файлы, нужно нажать на кнопку "Открыть сло-',
                'вари".',
                '    После того, как вы откроете словари перед вами появися таблица со словарями и две кнопки: "Создать новый" и "Обно-',
                'вить". Последняя нужна для того, чтобы после создания ваш словарь появился в списке. Чтобы открыть словарь нужно клик-',
                'нуть по названию одного из них.',
                '    Затем, перед вами откроется словарь со словами. Имеются аналогичные кнопки: "Создать новый" и "Обновить". Также есть',
                'таблица со следующими параметрами:',
                '',
                'Слово: слово на иностранном языке',
                'Перевод: слово на вашем языке',
                'Прогресс: от 0 до 100%',
                '',
                'Также есть кнопка "Учить" для тренеровки новых слов. Вы можете услышать, как произносится слово, нажав на него.',
                '    При нажатии на кнопку "Учить", открываются настройки тренировки на данный момент доступно 2 режима: "Найти слово"',
                'и "Найти перевод" также вы можете изменить сложность тренировки. Она влияет на прогрес изучения. После выбора режима',
                'вам откроется тренировка, представленная в виде теста. Выбераете вариант, он подсвечивается (в зависимости от правиль-',
                'ного ответа.) Чтобы перейти дальше нажмите на кнопу "Дальше". Вы также можете завершить тренировку досрочно, нажав на',
                'соседнюю кноку',
                '',

                'Проект создан учениом 11Б класса, школы "МАОУ Гимназия имени Н. Д. Лицмана г. Тобольск" Гвяздовским Иваном Андреивичем в',
                'рамках XXXIV Научно-практической конференции 2024 года. Все права защищены!',
                '',
                ''], expand_y=True

        )
        ]
    ],
    'translator': [
        [sg.Combo(config['languages_list'], default_value='russian', expand_x=True, font=["Times New Roman", 12], key='-L1-'), sg.Button('🔁', font=["Times New Roman", 16]),
         sg.Combo(config['languages_list'], default_value='english', expand_x=True, font=["Times New Roman", 12], key='-L2-')],
        [sg.InputText(default_text='', font=["Times New Roman", 16], s=(23, 16), key='-T1-'), sg.Button('→', font=["Times New Roman", 16]),
         sg.InputText(default_text='', font=["Times New Roman", 16], s=(23, 16), key='-T2-')],
        [sg.Btn('🔊', font=["Times New Roman", 16]), sg.Txt('              ', font=["Times New Roman", 16], expand_x=True, key='-S1-'),
         sg.Btn('🔊', font=["Times New Roman", 16]), sg.Txt('   ', font=["Times New Roman", 16], expand_x=True, key='-S2-')],
        [sg.Txt('   ', font=["Times New Roman", 16], expand_y=True)],
        [
            sg.Txt('   ', font=["Times New Roman", 20], expand_x=True),
            sg.Btn('🎤', font=["Times New Roman", 20]),
            sg.Txt(' ', font=["Times New Roman", 20], expand_x=True),
            sg.Btn('🕒', font=["Times New Roman", 20]),
            sg.Txt(' ', font=["Times New Roman", 20], expand_x=True),
            sg.Btn(' + ', font=["Times New Roman",  20, 'bold']),
            sg.Txt('   ', font=["Times New Roman", 20], expand_x=True)],
        [sg.Txt('   ', font=["Times New Roman", 16], expand_y=True)]
    ],
    'history': [
        [sg.Table(values=get_history(), headings=[dict_from_languages_json()['word->transl.'], dict_from_languages_json()['lang->lang']],
                  justification='center', expand_x=True, expand_y=True)]
    ],
}
