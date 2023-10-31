from config import *
from py_files.modules.json_module import *
from py_files.modules.csv_module import *
from py_files.modules.tts_module import *
from py_files.modules.translate_module import *


def setting_menu():
    window = sg.Window('Settings', layout['settings'], size=(450, 225))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == dict_from_languages_json()['About program']:
            about_program()
        elif event == 'OK':
            change_setting(values)
            break
    window.close()


def open_list_of_dictionaries():
    window = sg.Window(dict_from_languages_json()['list of dictionaries'], layout['list_of_dictionaries'],
                       size=(400, 400))

    while True:
        event, values = window.read()
        window['-TABLE-'].update(values=list_csv)
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == '+ Create new ':
            create_new_list_window()
        else:
            window.close()
            open_file_window(values['-TABLE-'][0])
            return

    window.close()
    return


def create_new_list_window():
    window = sg.Window(dict_from_languages_json()['new dictionary'], layout['new dictionary'], size=(200, 100))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'OK':
            create_new_list(values['-NAME-'])
            break
    window.close()


def open_file_window(number_of_file):
    name = list_csv[number_of_file][-1]
    list_from_file(name.strip())

    window = sg.Window(name[:-4], layout['file'], size=(540, 400))

    while True:
        event, values = window.read()
        window['-FILE-'].update(values=list_file)
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == '+ Add new word':
            add_word_window(name)
        elif event == 'Learn':
            window.close()
            choose_mod(name)
            break
        else:
            try:
                speak(list_file[values['-FILE-'][0]][1].strip())
            except IndexError:
                pass
    window.close()


def add_word_window(name_f):
    window = sg.Window(dict_from_languages_json()['new word'], layout['new_word'], size=(200, 100))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'OK':
            create_new_word(values[0], values[1], name_f)
            break
    window.close()


def choose_mod(name_f):
    window = sg.Window('select mod', layout['mod'])

    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'OK':
            create_training_dict(value['-MOD-'], name_f)
            break
    window.close()
    train(value['-DIFFICULTY-'])


def train(diff):
    fill_steak()
    txt, btns = steak.popleft()
    delta = difficulty[diff]
    train_layout = [
        [sg.Text(text='', font=("Times New Roman", 35, "bold"))],
        [sg.Text(text=f'{txt.zfill(22).replace("0", " ")}', font=("Times New Roman", 35, "bold"), key='--TXT--')],
        [sg.Text(text='', font=("Times New Roman", 35, "bold"))],
        [sg.Button(button_text=btns[0], button_color='gray', expand_x=True, expand_y=True, key='--B1--', font=("Times New Roman", 20, "bold")),
         sg.Button(button_text=btns[1], button_color='gray', expand_x=True, expand_y=True, key='--B2--', font=("Times New Roman", 20, "bold"))],
        [sg.Button(button_text=btns[2], button_color='gray', expand_x=True, expand_y=True, key='--B3--', font=("Times New Roman", 20, "bold")),
         sg.Button(button_text=btns[3], button_color='gray', expand_x=True, expand_y=True, key='--B4--', font=("Times New Roman", 20, "bold"))],
        [sg.Button(button_text=dict_from_languages_json()['continue ⏩'], expand_x=True, expand_y=True, font=("Times New Roman", 20, "bold")),
         sg.Button(button_text=dict_from_languages_json()['finish train'], expand_x=True, expand_y=True, font=("Times New Roman", 20, "bold"))]
    ]
    window = sg.Window('training...', layout=train_layout, size=(540, 400))

    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED or event == dict_from_languages_json()['finish train']:
            break
        elif event in ('--B1--', '--B2--', '--B3--', '--B4--'):
            condition = check_answer(txt, window[event].ButtonText)
            window[event].update(button_color=('green' if condition else 'red'))
            if condition:
                score_of_training.update({txt: delta})
            else:
                score_of_training.update({txt: -delta})
        elif event == dict_from_languages_json()['continue ⏩']:
            if not steak:
                break
            txt, btns = steak.popleft()
            window['--TXT--'].update(f'{txt.zfill(22).replace("0", " ")}')
            window['--B1--'].update(btns[0], button_color='gray')
            window['--B2--'].update(btns[1], button_color='gray')
            window['--B3--'].update(btns[2], button_color='gray')
            window['--B4--'].update(btns[3], button_color='gray')
    print(score_of_training)
    change_progress()


def about_program():
    window = sg.Window('About', layout=layout['about_program'], size=(850, 400))
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
    window.close()


def open_translator():
    window = sg.Window('Translator', layout=layout['translator'], size=(600, 400))
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break


if __name__ == '__main__':
    sg.theme(dict_from_setting_json()['theme'])
    main_window = sg.Window('WordBook', layout['main_menu'], size=(400, 400))

    while True:
        e, v = main_window.read()
        if e == sg.WIN_CLOSED:
            main_window.close()
            break
        elif e == dict_from_languages_json()['Open dictionaries']:
            main_window.close()
            open_list_of_dictionaries()
            break
        elif e == dict_from_languages_json()['+   Create new   +']:
            create_new_list_window()
            open_list_of_dictionaries()
        elif e == dict_from_languages_json()['🛠    Settings    🛠']:
            main_window.close()
            setting_menu()
            break
        elif e == dict_from_languages_json()['Translator']:
            main_window.close()
            open_translator()
    main_window.close()
