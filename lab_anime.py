import csv


with open('anime.csv', newline = '', encoding='utf-8') as csvfile:
    reader = csv.DictReader (csvfile, delimiter = ',')
    all_anime = []
    for row in reader:
        all_anime.append (row['Name']) #записываем все названия аниме в один список
        
#функция, по которой будем сортировать ответы
def res(quest, answ):
    with open('anime.csv', newline = '', encoding='utf-8') as csvfile:
        reader = csv.DictReader (csvfile, delimiter = ',')
        if quest == 'Rating Score' or quest == 'Episodes' or quest == 'Season':
            for row in reader:
                if row[quest] < answ:
                    if row['Name'] in all_anime: #проверяем есть ли еще такое аниме в нашем списке или его удалили при другом условии
                        all_anime.remove(row['Name']) #если эпизодоы/сезонов/рейтинга меньше, чем нужно, то из всего начального списка удаляем названия аниме, которые нам не подходят
        elif quest == 'Tags' or quest == 'Content Warning':
            for row in reader:
                answ_list = answ.split(',')
                for i in range (len(answ_list)):
                    if (answ_list[i]) not in row[quest]:
                        if row['Name'] in all_anime: #проверяем есть ли еще такое аниме в нашем списке или его удалили при другом условии
                            all_anime.remove(row['Name']) #если хотя бы одного жанра нет, то удаляем название аниме из списка
        elif quest == 'Studios' or quest == 'Type':
            for row in reader:
                if answ not in row[quest]:
                        if row['Name'] in all_anime: #проверяем есть ли еще такое аниме в нашем списке или его удалили при другом условии
                            all_anime.remove(row['Name']) #проверяем студию и тип, если не удовлетворяет условию, то удаляем аниме
        elif quest == 'StartYear' or quest == 'EndYear':
            for row in reader:
                if answ not in row[quest]:
                        if row['Name'] in all_anime: #проверяем есть ли еще такое аниме в нашем списке или его удалили при другом условии
                            all_anime.remove(row['Name'])#проверяем год, если не удовлетворяет условию, то удаляем аниме
        else:
            if quest == 'Finished':
                for row in reader:
                    if answ not in row[quest]:
                            if row['Name'] in all_anime: #проверяем есть ли еще такое аниме в нашем списке или его удалили при другом условии
                                all_anime.remove(row['Name'])#проверяем условие на True/False, если не удовлетворяет условию, то удаляем аниме
                                
print('Пройдите опрос, чтобы мы подобрали подходящие аниме (если какой-то пункт не важен, нажмите "Enter")')               
questions = ('Введите минимальный рейтинг аниме от 1 до 10:',
             'Введите желаемые жанры (через запятую на английском языке):',
             'Введите предупреждения, которые стоит исключить(через запятую на английском языке):',
             'Введите формат показа(на английском языке):',
             'Введите минимальное количество эпизодов:',
             'Аниме должно быть закончено?(введите True/False)',
             'Введите год выпуска:',
             'Введите год окончания:',
             'Введите минимальное количство сезонов:',
             'Введите студию, которая создала аниме(на английском языке):') #список вопросов

answers = {'Rating Score': '',
           'Tags': '',
           'Content Warning': '',
           'Type': '',
           'Episodes': '',
           'Finished': '',
           'StartYear': '',
           'EndYear': '',
           'Season': '',
           'Studios': ''} #словарь с ответами пользователя

questions = iter(questions)
for answer in answers:
    answers[answer] = input(next(questions))#записываем ответы

for question in answers:
    answer = answers[question]
    if answer !='': #проверяем есть ли ответ от пользователя
        if '012345678' not in answer:
            res(question, answer.title()) #делаем первую букву заглавной, если ответ не является числом
        else:
            res(question, answer)
            
#записываем ответ    
with open("output.txt", 'w', encoding='utf-8') as res:
    for i in all_anime:
        res.write(f'{i}\n')

print('Результаты сформированы и помещены в файл output.txt!')
