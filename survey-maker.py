print('''
╔══════════════════════════════╗
║                              ║
║     Создатель Опросников     ║
║                              ║
╚══════════════════════════════╝
''')
guesseers = []

def enter_members():
    counter = 0
    names_count = int(input('Введите количество участников: '))
    while counter < names_count:
        txt = ('Введите имя участника №' + str(counter + 1) + ': ')
        guesseers.append(input(txt))
        counter += 1
    
def show_members():
    show = ' / '.join(guesseers)
    print('Участники опроса: ', show)

all_data = [] 
answer = []
def enter_question_and_variants():
    counter2 = 0
    opros = (str(input('Введите тему опросника: ')))
    variants_count = int(input('Введите количество вариантов ответа: '))
    answer.append(opros)
    for counter2 in range(variants_count):
      txt2 = ('Вариант ответа №' + str(counter2 + 1) + ': ')
      all_data.append(str(input(txt2)))  
      counter2 += 1
      
    print('Вопрос: ',opros)
    counter3 = 0
    for all in all_data:
        txt3 = (str(counter3 + 1) + ')')
        print(txt3 + all)
        counter3 += 1
    
all_choice = []

def enter_your_choice():
    counter4 = 0
    guesseers2 = []
    guesseers2.extend(guesseers)
    for counter4 in range(len(guesseers2)):
        txt4 = str('ответ '+'Участника '+ guesseers2[0] + ': ')
        all_choice.append(input(txt4))
        guesseers2.pop(0)
        counter4 += 1

def show_ansfers():
    counter5 = 0
    guesseers3 = []
    guesseers3.extend(guesseers)
    all_choice2 = []
    all_choice2.extend(all_choice)
    
    print('\n')
    
    while counter5 < (len(guesseers)):
       print('Вопрос:', answer[0])
       vse_guesseers = ('Голосующий №'+ str(counter5 + 1) + ': ')
        
       print(vse_guesseers)
       print('Имя:',guesseers3[0])
       print('Выбрал:', all_choice2[0])
       print('\n')
       guesseers3.pop(0)
       all_choice2.pop(0)
       counter5 += 1

enter_members()
show_members()
enter_question_and_variants()
enter_your_choice()
show_ansfers()

# print(guesseers)
# print(all_data)
# print(all_choice)







        







