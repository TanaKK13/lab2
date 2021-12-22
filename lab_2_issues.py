import csv

def filter_min_quantity(file):
    anime_list = []
    for quest in ('Rating Score', 'Episodes', 'Season'):
        for row in file:
            if row[quest]< answ[quest] and answ[quest]!='':
                anime_list.append(row['Name'])
    return anime_list

def filter_tags_content(file):
    anime_list = []
    for quest in ('Tags', 'Content Warning'):
        for row in file:
            k = 0
            for answer in answ:
                if answer in row[quest]:
                    k+=1
            if k != len(answ) and answ[quest]!='':
                anime_list.append(row['Name'])
    return anime_list

def filter_studios_type(file):
    anime_list = []
    for quest in ('Studios', 'Type'):
        for row in file:
            if row[quest] != answ[quest] and answ[quest]!='':
                anime_list.append(row['Name'])
    return anime_list
    
def filter_year(file):
    anime_list = []
    for quest in ('StartYear', 'EndYear'):
        for row in file:
            if answ[quest] not in row[quest] and answ[quest]!='':
                anime_list.append(row['Name'])
    return anime_list

print('Пройдите опрос, чтобы мы подобрали подходящие аниме (если какой-то пункт не важен, нажмите "Enter")')               
questions = ('Введите минимальный рейтинг аниме от 1 до 10:',
             'Введите желаемые жанры (через запятую на английском языке):',
             'Введите предупреждения, которые стоит исключить(через запятую на английском языке):',
             'Введите формат показа(на английском языке):',
             'Введите минимальное количество эпизодов:',
             'Введите год выпуска:',
             'Введите год окончания:',
             'Введите минимальное количство сезонов:',
             'Введите студию, которая создала аниме(на английском языке):') 

answ = {'Rating Score': '',
           'Tags': '',
           'Content Warning': '',
           'Type': '',
           'Episodes': '',
           'StartYear': '',
           'EndYear': '',
           'Season': '',
           'Studios': ''} 

questions = iter(questions)
for answer in answ:
    answ[answer] = input(next(questions))

all_anime = []
with open('anime.csv', newline = '', encoding='utf-8') as csvfile:
    reader = list(csv.DictReader (csvfile, delimiter = ','))
    for row in reader:
        all_anime.append(row['Name'])

min_quantity = filter_min_quantity(reader)
tags_content = filter_tags_content(reader)
studios_type = filter_studios_type(reader)
year = filter_year(reader)

bad_anime = min_quantity+tags_content+studios_type+year
for film in bad_anime:
    if film in all_anime:
        all_anime.remove(film)
            
if len(all_anime) == 0:
    print ('По вашему запросу ничего не найдено')
else:
    with open("output.txt", 'w', encoding='utf-8') as res:
        for i in all_anime:
            res.write(f'{i}\n')

    print('Аниме по вашему запросу были добавлены в файл "output.txt!"')
