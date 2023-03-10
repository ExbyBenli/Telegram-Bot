questions = ['Если ли у Вас идея для своего бизнеса?',
             'Вы разбираетесь в теме, которой хотите заниматься?',
             'У Вас уже есть опыт самостоятельного или партнерского бизнеса?',
             'Есть ли у Вас бизнес-план',
             'Зачем Вам нужен свой бизнес?',
             'Вы знаете все сложности и подводные камни, с которыми предстоит столкнуться?',
             'Если все пойдет не по плану, что Вы будете делать?',
             'У Вас есть финансовая подушка безопасности?',
             'У Вас есть необходимые для старта инвестиции?',
             'У вас есть кто то, кто поддерживает вашу идею о бизнесе?',
             'Были ли в Вашей жизни случаи провалов?',
             'Представьте себе, что у вас есть волшебная палочка, и Вы можете получить все, что захотите! Захотели ли бы Вы тогда заниматься бизнесом?,'
             'Сколько времени в день вы готовы тратить на свой бизнес?',
             'Бизнес - это?',
             'Как давно вы думаете о своем бизнесе?',
             'На сколько % Вы подготовились к открытию бизнеса, по Вашему мнению?',
             'Насколько для Вас важно, что подумают о Вас люди в связи с Вашим новым статусом?',
             'От кого (чего) зависит успех моего бизнеса?']

answers = [['\n', '1) идеи нет', '\n',
            '2) потом что-нибудь придумаю', '\n',
            '3) идей несколько, но окончательно не решил', '\n',
            '4) да, точно знаю, чем буду заниматься', '\n'],
           ['\n', '1) Нет, но у других получилось, и у меня тоже получится', '\n',
            '2) В общих чертах, но детально не разбираюсь', '\n',
            '3) Да, я профессионал в этом вопросе', '\n',
            '4) Имею опыт работы в смежных областях', '\n'],
           ['\n', '1) Нет, никогда такого опыта не было', '\n',
            '2) Был наемным сотрудником на управленческой позиции', '\n',
            '3) Да, был неудачный опыт в бизнесе, но меня это не останавливает', '\n',
            '4) Да, был успешный бизнес в другой сфере', '\n'],
           ['\n', '1) Пока нет', '\n',
            '2) Не знаю, что это такое и зачем он мне нужен', '\n',
            '3) Да, я давно все рассчитал', '\n',
            '4) Только начал его создавать', '\n'],
           ['\n', '1) Хочу новый статус', '\n',
            '2) Хочу свободы', '\n',
            '3) Хочу себя реализовать свой потенциал', '\n',
            '4) Хочу добиться определенных финансовых целей в жизни', '\n'],
           ['\n', '1) Никаких сложностей не будет', '\n',
            '2) Предполагаю, с чем придется столкнуться', '\n',
            '3) Знаю, проходил в другом бизнесе', '\n',
            '4) Знаю по опыту других людей', '\n'],
           ['\n', '1) Разберусь по ходу', '\n',
            '2) Такого быть не может', '\n',
            '3) Ошибки будут минимальные, я все хорошо рассчитал и проверил', '\n',
            '4) У меня есть 2 плана: оптимистичный и пессимистичный', '\n'],
           ['\n', '1) Она мне не нужна, я начну сразу зарабатывать много', '\n',
            '2) Нет подушки, поэтому быстрее буду крутиться', '\n',
            '3) Есть, хватит на несколько месяцев', '\n',
            '4) Да, есть на все время от старта до получения первой прибыли', '\n'],
           ['\n', '1) Есть на первый этап', '\n',
            '2) Я рассчитываю взять кредит', '\n',
            '3) Мне не нужны инвестиции', '\n',
            '4) Да, с запасом, я подготовился в соответствии со своим бизнес - планом', '\n'],
           ['\n', '1) Все мое окружение против', '\n',
            '2) Меня многие не понимают, но я им докажу, что смогу', '\n',
            '3) Мне не нужна поддержка', '\n',
            '4) Да, меня поддерживают близкие люди', '\n'],
           ['\n', '1) Никогда никаких провалов не было. И не будет', '\n',
            '2) Были случаи, переживал, но не останавливался', '\n',
            '3) Конечно были, долго переживал, потом сложно было вернуться к своим планам', '\n',
            '4) Жизнь невозможна без провалов, это нормально. Живем дальше', '\n'],
           ['\n','1) Дайте волшебную палочку!', '\n',
            '2) Да, на палочку надейся, а сам не плошай!', '\n',
            '3) Зачем столько возни, если можно получить деньги просто так?', '\n',
            '4) Да, мне это интересно', '\n',],
           ['\n', '1) Хочу пару часов в день, а иначе зачем?', '\n',
            '2) Готов работать сутками', '\n',
            '3) Рабочий день', '\n',
            '4) Первое время сколько надо, потом меньше', '\n'],
           ['\n', '1) Возможность не работать вообще', '\n',
            '2) Возможность не работать на', '\n',
            '3) Прибыль и статус', '\n',
            '4) Прибыль', '\n'],
           ['\n', '1) Думаю пару месяцев', '\n',
            '2) Думаю больше 5 лет, но никак не решусь', '\n',
            '3) Думаю около года, может, больше', '\n',
            '4) Уже даже попробовал в разных сферах', '\n'],
           ['\n', '1) Даже не знаю', '\n',
            '2) 50%', '\n',
            '3) 30-50%', '\n',
            '4) 80 %', '\n'],
           ['\n', '1) Я хочу признания', '\n',
            '2) Я всем докажу, на что способен', '\n',
            '3) Есть несколько человек, мнение которых для меня важно', '\n',
            '4) Мне все равно, ведь это моя жизнь', '\n'],
           ['\n', '1) От команды', '\n',
            '2) От экономической ситуации в Мире', '\n',
            '3) Только от меня', '\n',
            '4) От государства', '\n']]

start_text = 'Привет! Готов ли ты к открытию своего бизнеса? Пройди тест и узнай свою готовность, для этого нажми на ' \
             '/test'
finish_text = 'Поздравляем, вы прошли тест! Чтобы узнать результаты, нажмите /total.'

result = ['''
          Если Ваш результат такой, это значит, что Вы в самом начале пути! Возможно, Вы еще раздумываете, нужен ли Вам вообще этот бизнес! 

Сначала разберитесь, ЗАЧЕМ Вам нужен бизнес. 

Сходите к коучу, ведь часто сами мы часто не отличаем истинные цели от ложных. Когда поймете, ЗАЧЕМ, начинайте думать КАК!

Здесь могут всплыть серьезные ограничивающие убеждения, избавьтесь от них! Дорогие мои! Раз Вы здесь, значит вопрос с 
бизнесом возник в Вашей жизни. Важно понимать, что вести бизнес можно только из позиции 100% ответственности за свою 
жизнь, без лишних иллюзий, с гибким мышлением и широко открытыми глазами! Перемены должны быть экологичными. Тогда и жизнь будет радостной и гармоничной! 

Ну, и не забывайте, что без планов никуда. Сначала готовимся, потом  начинаем! Не забудьте начать с формирования 
подушки безопасности: ваш расход в месяц * 12. Это поможет вам чувствовать себя спокойно и уверенно на пути к новым доходам.

Те, кто действительно чего-то хочет, обязательно это получит!
''',

          '''
          Все получится, но надо получше подготовиться!
Отлично, что Вы стремитесь к переменам! Но пока Вам еще есть над чем поработать! Можно попробовать начать с 
монетизации собственного дела, или поработать в качестве сотрудника в том бизнесе, к которому Вы стремитесь. Изучите 
вопросы глубже, подготовьте необходимые расчеты, начните готовить план. Серьезное внимание необходимо уделить вопросу убеждений, потому что именно от того, как и что мы думаем, зависит то, что мы делаем и какой результат получаем! Не делайте резких движений. Если Вы хотите начать свой бизнес, потому что надоела наемная работа, подготовьте получше ходы отступления, не бросайтесь в неизвестное с головой. Особое внимание уделите подушке безопасности: накоплениям из расчета: ваш расход за месяц * на 12 месяцев. Если она пока не сформирована, начните ее формировать - пусть это будет одним из шагов перехода в новую жизнь!  

В любом случае, раз Вы здесь, значит желание начать свой бизнес или свое дело уже есть! А раз есть желание, значит, 
его надо превратить в цель, а цель - в план!
''',

          '''
          Неплохо, но есть куда стремиться!
Вы знаете, чего хотите, и это замечательно! Вы немного сомневаетесь, или, Вам не хватает знаний в каких то областях, но это все можно исправить! 
Продолжайте работать над своим проектом, как следует изучите все вопросы, посоветуйтесь с профессионалами, 
получите необходимые консультации. Дорогу осилит идущий! Главное, идти, хоть маленькими шагами. 
Поработайте над своими убеждениями относительно бизнеса и денег, чтобы существующие программы не могли помешать Вам достичь успеха! 
Не торопитесь, сверьте дорожные карты, и только потом приступайте к движению! Убедитесь, что все готово к старту и не навредите ли Вы себе, если начнете бизнес! 
Оцените свои ресурсы, проверьте свою финансовую подушку безопасности и подготовьте план Б на случай, если Вы не верно их рассчитали!
''',

          '''
          Поздравляем!
Вы хорошо подготовились к открытию своего бизнеса! Вы многое учли, продумали, рассчитали! Вы осознаете всю меру 
ответственности и адекватно оцениваете собственные силы и возможности! Помните, что чем лучше Вы подготовитесь, 
тем более предсказуемым будет результат! Еще  раз все проверьте, обратите внимание на финансовую безопасность в случае, если будут отклонения от плана, подготовьте план запуска, и в путь! 
''']
