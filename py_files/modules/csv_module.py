from collections import defaultdict, deque, Counter
from py_files.modules.json_module import dict_from_languages_json
from random import sample
import csv
import os

DIR = r'F:\Projects\PycharmProjects\Wordbook\word_lists'
P = r'{}\{}'
list_file = []
training_dict = defaultdict(str)
steak = deque()
score_of_training = Counter()
FILE = ''
columns = ['№', 'word', 'translation', 'progress']


def dictionary_list_from_dir():
    directory = os.listdir(DIR)
    return [[str(j) + ' ' * 16, i + ' ' * (16 - len(i))]
            for j, i in zip(range(1, len(directory) + 1), directory)]


list_csv = dictionary_list_from_dir()


def list_from_file(filename):
    global list_file

    with open(P.format(DIR, filename), 'r', encoding='utf8') as f:
        rows = csv.DictReader(f)
        for row in rows:
            lst = [row['№'], row['word'] + ' ' * (13 - len(row['word'])),
                   row['translation'] + ' ' * (13 - len(row['translation'])), row['progress'] + '%']
            list_file.append(lst)


def create_new_list(name):
    global list_csv
    with open(P.format(DIR, name), 'w+', encoding='utf8') as f:
        f.write('№,word,translation,progress')

    list_csv.append([len(list_csv) + 1, f'{name}.csv'])


def create_new_word(word, translate, name):
    global list_file

    with open(P.format(DIR, name), 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow([len(list_file) + 1, word, translate, 0])
    list_file.append([len(list_file) + 1, word, translate, '0' + '%'])


def create_training_dict(mod, file):
    global training_dict, FILE
    FILE = file

    d = defaultdict(str)

    with open(P.format(DIR, file), 'r', encoding='utf-8') as f:
        rows = csv.DictReader(f)
        for row in rows:
            if mod == dict_from_languages_json()['find translation']:
                d[row['word']] = row['translation']
            elif mod == dict_from_languages_json()['find word']:
                d[row['translation']] = row['word']
    training_dict |= d


def fill_steak():
    global training_dict, steak

    shuf_dict, temp = defaultdict(list), []

    for key in sample(list(training_dict.keys()), len(training_dict.keys())):
        temp.append(training_dict[key])
        temp.extend(sample([i for i in training_dict.values() if i != training_dict[key]], 3))
        shuf_dict[key] = sample(temp, len(temp))
        temp.clear()
    steak.extend([(key, values) for key, values in shuf_dict.items()])


def check_answer(quest, answ):
    global training_dict
    if training_dict[quest] == answ:
        return True
    return False


def change_progress():
    global score_of_training, FILE

    t = []

    with open(P.format(DIR, FILE), 'r', encoding='utf-8') as f:
        rows = csv.DictReader(f)

        for row in rows:
            if row['word'] in score_of_training.keys():
                t.append({'№': row['№'], 'word': row['word'], 'translation': row['translation'],
                          'progress': str(int(row['progress']) + score_of_training[row['word']])})
            elif row['translation'] in score_of_training.keys():
                t.append({'№': row['№'], 'word': row['word'], 'translation': row['translation'],
                          'progress': str(int(row['progress']) + score_of_training[row['translation']])})
            else:
                t.append(row)
    for i in range(len(t)):
        if int(t[i]['progress']) < 0:
            t[i]['progress'] = '0'
        elif int(t[i]['progress']) > 100:
            t[i]['progress'] = '100'

    with open(P.format(DIR, FILE), 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in t:
            writer.writerow(row)

