M = 1946
name = input('Здравствуйте, как вас зовут? ')
print(f'Очень приятно, {name}! Меня зовут Марк.')
age = int(input('Сколько вам лет? '))
if 2024 - age < M:
    print(f'Да, {name}, Вы старше меня на', M - (2024 - age), 'лет.')
    print('Вам нравится программировать?')
    answer = input()
    if answer == 'да':
        print('Превосходно! Уверен, что у вас получится написать множество полезных и хороших программ.')
    elif answer == 'нет':
        print('Жаль. Я думал, Вы сможете написать интересную программу для меня.')
else:
    print(f'Да, {name}, я старше Вас на', (2024 - age) - M, 'лет.')
    print('Вам нравится программировать?')
    answer = input()
    if answer == 'да':
        print('Превосходно! Уверен, что у вас получится написать множество полезных и хороших программ.')
    elif answer == 'нет':
        print('Жаль. Я думал, Вы сможете написать интересную программу для меня.')
