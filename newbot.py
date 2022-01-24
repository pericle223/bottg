import telebot, datetime
from telebot import types
#1950614489:AAFSg92N5ADfKT7Kpt4W3m-xqBCiISFy8Rk

#API_TOKEN = '1950614489:AAF4In66YPxZz_epuqrgoXBobeTjXE6qScw'  # - бот оригинальный
#API_TOKEN = '1973492515:AAGgu8xygxC0Kcyu2vejW0BbuCuZ0K3-UYA'  # - бот тестовый

bot = telebot.TeleBot(API_TOKEN)

# ссылки
links = {"АКС":"https://zoom.us/aks",
         "Комп.Сети":"https://zoom.us/comp_seti",
         "Арх.Комп":"https://zoom.us/arh_compx",
         "Операц.Систем":"https://zoom.us/operac_sist",
         "Филос":"https://us04web.zoom.us/filos"}
schedule = {"АПО-20-1(а)":{"Понедельник": {"1":"1️⃣ Занятия на военной кафедре"},
                           "Вторник":{"1":"1️⃣ Архитектура компьютерных систем-лекц. 13:00-13:50 | Zoom",
                                      "2":"2️⃣ Архитектура компьютерных систем-СРОП 14:00-14:50 | Zoom",
                                      "3":"3️⃣ Компьютерные сети-лекц. 15:10-16:00 | Zoom",
                                      "4":"4️⃣ Компьютерные сети-СРОП 16:10-17:00 | Zoom"},
                           "Среда":{"1":"1️⃣ Архитектура компьютера-лекц. 8:30-9:20 | Zoom",
                                    "2":"2️⃣ Архитектура компьютера-СРОП 9:30-10:20 | Zoom",
                                    "3":"3️⃣ Операционные системы-лекц. 10:40-11:30 | Zoom",
                                    "4":"4️⃣ Операционные системы-СРОП 11:40-12:30 | Zoom",
                                    "5":"5️⃣ Философия-лекц. 13:00-16:00 | Zoom"},
                           "Четверг":{"1":"1️⃣ Философия-пр. 9:30-10:20 | 413/5",
                                      "2":"2️⃣ Архитектура компьютерных систем-пр. 10:40-11:30 | 203/5",
                                      "3":"3️⃣ Операционные системы-пр. 11:40 - 12:30 | 203/5",
                                      "4":"4️⃣ Операционные системы-лаб. 13:00 - 13:50 | 14/6",
                                      "5":"5️⃣ Архитектура компьютерных систем-лаб. 14:00-14:50 | 14/6"},
                           "Пятница":{"1":"1️⃣ Архитектура компьютера-лаб. 10:40-12:30 | 406/5",
                                      "2":"2️⃣ Компьютерные сети-лаб. 13:00-14:50 | 205,210/5",
                                      },
                           "Суббота":{"1":"🟢 Нет занятий 🟢"},
                           "Воскресенье":{"1":"🟢 Нет занятий 🟢"}
                           },

            "АПО-20-1(б)":{"Понедельник":{"1":"1️⃣ Занятия на военной кафедре"},
                           "Вторник":{"1":"1️⃣ Архитектура компьютерных систем-лекц. 13:00-13:50 | Zoom",
                                      "2":"2️⃣ Архитектура компьютерных систем-СРОП 14:00-14:50 | Zoom",
                                      "3":"3️⃣ Компьютерные сети-лекц. 15:10-16:00 | Zoom",
                                      "4":"4️⃣ Компьютерные сети-СРОП 16:10-17:00 | Zoom"},
                           "Среда":{"1":"1️⃣ Архитектура компьютера-лекц. 8:30-9:20 | Zoom",
                                    "2":"2️⃣ Архитектура компьютера-СРОП 9:30-10:20 | Zoom",
                                    "3":"3️⃣ Операционные системы-лекц. 10:40-11:30 | Zoom",
                                    "4":"4️⃣ Операционные системы-СРОП 11:40-12:30 | Zoom",
                                    "5":"5️⃣ Философия-лекц. 13:00-16:00 | Zoom"},
                           "Четверг":{"1":"1️⃣ Философия-пр. 9:30-10:20 | 413/5",
                                      "2":"2️⃣ Архитектура компьютерных систем-пр. 10:40-11:30 | 203/5",
                                      "3":"3️⃣ Операционные системы-пр. 11:40 - 12:30 | 203/5",
                                      "4":"4️⃣ Компьютерные сети-лаб. 13:00-14:50 | 205,210/5"},
                           "Пятница":{"1":"1️⃣ Архитектура компьютера-лаб. 10:40-12:30 | 406/5",
                                      "2":"2️⃣ Архитектура компьютерных систем-лаб. 13:00-13:50 | 14/6",
                                      "3":"3️⃣ Операционные системы-лаб. 14:00 - 14:50 | 14/6",},
                           "Суббота":{"1":"🟢 Нет занятий 🟢"},
                           "Воскресенье":{"1":"🟢 Нет занятий 🟢"}
                           },

            "АПО-20-2":{"Понедельник":{"1":"1️⃣ Занятия на военной кафедре"},
                        "Вторник":{"1":"1️⃣ Архитектура компьютерных систем-лекц. 13:00-13:50 | Zoom",
                                   "2":"2️⃣ Архитектура компьютерных систем-СРОП 14:00-14:50 | Zoom",
                                   "3":"3️⃣ Компьютерные сети-лекц. 15:10-16:00 | Zoom",
                                   "4":"4️⃣ Компьютерные сети-СРОП 16:10-17:00 | Zoom"},
                        "Среда":{"1":"1️⃣ Архитектура компьютера-лекц. 8:30-9:20 | Zoom",
                                 "2":"2️⃣ Архитектура компьютера-СРОП 9:30-10:20 | Zoom",
                                 "3":"3️⃣ Операционные системы-лекц. 10:40-11:30 | Zoom",
                                 "4":"4️⃣ Операционные системы-СРОП 11:40-12:30 | Zoom",
                                 "5":"5️⃣ Философия-лекц. 13:00-16:00 | Zoom"},
                        "Четверг":{"1":"1️⃣ Архитектура компьютера-пр. 15:10-17:00 | 415/5",
                                   "2":"2️⃣ Компьютерные сети-лаб. 17:10-19:00 | 205,210/5"},
                        "Пятница":{"1":"1️⃣ Архитектура компьютерных систем-пр. 8:30-9:20 | 14/6",
                                   "2":"2️⃣ Архитектура компьютерных систем-лаб. 9:30-10:20 | 14/6",
                                   "3":"3️⃣ Операционные системы-пр. 10:40 - 11:30 | 14/6",
                                   "4":"4️⃣ Операционные системы-лаб. 11:40 - 12:30 | 14/6",
                                   "5":"5️⃣ Философия-лекц. 15:10-16:00 | 415/5"},
                        "Суббота":{"1":"🟢 Нет занятий 🟢"},
                        "Воскресенье":{"1":"🟢 Нет занятий 🟢"}
                        }

            }


def schedule_today(group, day):
    number_of_subj = len(schedule.get(group).get(day).keys())
    pokej = list(schedule.get(group).get(day).values())
    text = ''
    for i in range(0,number_of_subj):
        text = text +pokej[i] + "\n"
    return (text)


@bot.message_handler(commands=['start'])
def start_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('АПО-20-1(а)')
    itembtn2 = types.KeyboardButton('АПО-20-1(б)')
    itembtn3 = types.KeyboardButton('АПО-20-2')
    markup.add(itembtn1, itembtn2, itembtn3)

    bot.send_message(message.from_user.id, "*Бот для просмотра расписания, выбери группу:*\n_P.s Расписание обновляется каждый день в 6 утра._", reply_markup=markup, parse_mode="Markdown")



@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Author: @loremipsum69")

@bot.message_handler(commands=['links'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    aks = types.InlineKeyboardButton(text="Zoom|АКС|Касимов И.Р.", url=links.get("АКС"))
    comp_seti = types.InlineKeyboardButton(text="Zoom|Комп.Сети|Куликов В.П.", url=links.get("Комп.Сети"))
    arh_comp = types.InlineKeyboardButton(text="Zoom|Архитект.комп|Касимов И.Р.", url=links.get("Арх.Комп"))
    operac_sistem = types.InlineKeyboardButton(text="Zoom|Операц.сист.|Куликов В.П.", url=links.get("Операц.Систем"))
    filos = types.InlineKeyboardButton(text="Zoom|Философия|Баёв А.В.", url=links.get("Филос"))

    keyboard.add(aks, comp_seti,arh_comp,operac_sistem,filos)
    bot.send_message(message.chat.id, "*Ссылки на конференции:*", reply_markup=keyboard, parse_mode="Markdown")

@bot.message_handler(commands=['day_1']) # группа а
def days_buttons(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    monday = types.KeyboardButton("📕Понедельник")
    tuesday = types.KeyboardButton('📕Вторник')
    wednesday = types.KeyboardButton('📕Среда')
    thursday = types.KeyboardButton('📕Четверг')
    friday = types.KeyboardButton('📕Пятница')
    back = types.KeyboardButton('/start')
    markup.add(monday, tuesday, wednesday, thursday, friday, back)

    bot.send_message(message.from_user.id, "*Расписание группы АПО-20-1(а) по дням:*", reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(commands=['day_2']) # группа б
def days_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    monday = types.KeyboardButton("📗Понедельник")
    tuesday = types.KeyboardButton('📗Вторник')
    wednesday = types.KeyboardButton('📗Среда')
    thursday = types.KeyboardButton('📗Четверг')
    friday = types.KeyboardButton('📗Пятница')
    back = types.KeyboardButton('/start')
    markup.add(monday, tuesday, wednesday, thursday, friday, back)

    bot.send_message(message.from_user.id, "*Расписание группы АПО-20-1(б) по дням:*", reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(commands=['day_3']) # группа 2
def days_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    monday = types.KeyboardButton("📘Понедельник")
    tuesday = types.KeyboardButton('📘Вторник')
    wednesday = types.KeyboardButton('📘Среда')
    thursday = types.KeyboardButton('📘Четверг')
    friday = types.KeyboardButton('📘Пятница')
    back = types.KeyboardButton('/start')
    markup.add(monday, tuesday, wednesday, thursday, friday, back)

    bot.send_message(message.from_user.id, "*Расписание группы АПО-20-2 по дням:*", reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(content_types=['text'])
def handle_text(message):


    if message.text == 'АПО-20-1(а)':
        current_day = datetime.datetime.today().isoweekday()
        #current_day = 5

        if current_day == 1:
            b = 'Понедельник\n'

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(а)", "Понедельник")), parse_mode="markdown")

        elif current_day == 2:
            b = 'Вторник\n'

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(а)", "Вторник")), parse_mode="markdown")
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            aks = types.InlineKeyboardButton(text="Zoom|АКС|Касимов И.Р.", url=links.get("АКС"))
            comp_seti = types.InlineKeyboardButton(text="Zoom|Комп.Сети|Куликов В.П.", url=links.get("Комп.Сети"))
            keyboard.add(aks,comp_seti)
            bot.send_message(message.chat.id, "*Ссылки на конференции:*", reply_markup=keyboard, parse_mode="Markdown")

        elif current_day == 3:
            b = 'Среда\n'
            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(а)", "Среда")), parse_mode="markdown")
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            arh_comp = types.InlineKeyboardButton(text="Zoom|Архитект.комп|Касимов И.Р.", url=links.get("Арх.Комп"))
            operac_sistem = types.InlineKeyboardButton(text="Zoom|Операц.сист.|Куликов В.П.", url=links.get("Операц.Систем"))
            filos = types.InlineKeyboardButton(text="Zoom|Философия|Баёв А.В.", url=links.get("Филос"))
            keyboard.add(arh_comp,operac_sistem,filos)
            bot.send_message(message.chat.id, "*Ссылки на конференции:*", reply_markup=keyboard, parse_mode="Markdown")

        elif current_day == 4:
            b = 'Четверг\n'
            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(а)", "Четверг")), parse_mode="markdown")

        elif current_day == 5:
            b = 'Пятница\n'
            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(а)", "Пятница")), parse_mode="markdown")


        elif current_day == 6:
            b = 'Суббота\n'

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(а)", "Суббота")), parse_mode="markdown")

        else:
            b = "Воскресенье\n"

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(а)", "Воскресенье")), parse_mode="markdown")


    elif message.text == 'АПО-20-1(б)':
        current_day = datetime.datetime.today().isoweekday()
        #current_day = 5

        if current_day == 1:
            b = 'Понедельник\n'

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(б)", "Понедельник")), parse_mode="markdown")
        elif current_day == 2:
            b = 'Вторник\n'
            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(а)", "Вторник")), parse_mode="markdown")
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            aks = types.InlineKeyboardButton(text="Zoom|АКС|Касимов И.Р.", url=links.get("АКС"))
            comp_seti = types.InlineKeyboardButton(text="Zoom|Комп.Сети|Куликов В.П.", url=links.get("Комп.Сети"))
            keyboard.add(aks,comp_seti)
            bot.send_message(message.chat.id, "*Ссылки на конференции:*", reply_markup=keyboard, parse_mode="Markdown")
        elif current_day == 3:
            b = 'Среда\n'
            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(б)", "Среда")), parse_mode="markdown")
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            arh_comp = types.InlineKeyboardButton(text="Zoom|Архитект.комп|Касимов И.Р.", url=links.get("Арх.Комп"))
            operac_sistem = types.InlineKeyboardButton(text="Zoom|Операц.сист.|Куликов В.П.", url=links.get("Операц.Систем"))
            filos = types.InlineKeyboardButton(text="Zoom|Философия|Баёв А.В.", url=links.get("Филос"))
            keyboard.add(arh_comp,operac_sistem,filos)
            bot.send_message(message.chat.id, "*Ссылки на конференции:*", reply_markup=keyboard, parse_mode="Markdown")
        elif current_day == 4:
            b = 'Четверг\n'

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(б)", "Четверг")), parse_mode="markdown")

        elif current_day == 5:
            b = 'Пятница\n'

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(б)", "Пятница")), parse_mode="markdown")

        elif current_day == 6:
            b = 'Суббота\n'

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(б)", "Суббота")), parse_mode="markdown")
        else:
            b = 'Воскресенье\n'

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(б)", "Воскресенье")), parse_mode="markdown")
    elif message.text == 'АПО-20-2':
        current_day = datetime.datetime.today().isoweekday()
        #current_day = 5

        if current_day == 1:
            b = 'Понедельник\n'

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-2", "Понедельник")), parse_mode="markdown")
        elif current_day == 2:
            b = 'Вторник\n'
            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-1(а)", "Вторник")), parse_mode="markdown")
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            aks = types.InlineKeyboardButton(text="Zoom|АКС|Касимов И.Р.", url=links.get("АКС"))
            comp_seti = types.InlineKeyboardButton(text="Zoom|Комп.Сети|Куликов В.П.", url=links.get("Комп.Сети"))
            keyboard.add(aks,comp_seti)
            bot.send_message(message.chat.id, "*Ссылки на конференции:*", reply_markup=keyboard, parse_mode="Markdown")

        elif current_day == 3:
            b = 'Среда\n'
            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-2", "Среда")), parse_mode="markdown")
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            arh_comp = types.InlineKeyboardButton(text="Zoom|Архитект.комп|Касимов И.Р.", url=links.get("Арх.Комп"))
            operac_sistem = types.InlineKeyboardButton(text="Zoom|Операц.сист.|Куликов В.П.", url=links.get("Операц.Систем"))
            filos = types.InlineKeyboardButton(text="Zoom|Философия|Баёв А.В.", url=links.get("Филос"))
            keyboard.add(arh_comp,operac_sistem,filos)
            bot.send_message(message.chat.id, "*Ссылки на конференции:*", reply_markup=keyboard, parse_mode="Markdown")

        elif current_day == 4:
            b = 'Четверг\n'

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-2", "Четверг")), parse_mode="markdown")


        elif current_day == 5:
            b = 'Пятница\n'

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-2", "Пятница")), parse_mode="markdown")


        elif current_day == 6:
            b = 'Суббота\n'

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-2", "Суббота")), parse_mode="markdown")
        else:
            b = 'Воскресенье\n'

            bot.send_message(message.from_user.id, "*{0}*\n{1}".format(b,schedule_today("АПО-20-2", "Воскресенье")), parse_mode="markdown")
# пн а
    elif message.text == "📕Понедельник":  # пн а

        bot.send_message(message.from_user.id, schedule_today("АПО-20-1(а)", "Понедельник"))
    elif message.text == "📕Вторник":
        bot.send_message(message.from_user.id, schedule_today("АПО-20-1(а)", "Вторник"))
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        aks = types.InlineKeyboardButton(text="Zoom|АКС|Касимов И.Р.", url=links.get("АКС"))
        comp_seti = types.InlineKeyboardButton(text="Zoom|Комп.Сети|Куликов В.П.", url=links.get("Комп.Сети"))
        keyboard.add(aks,comp_seti)
        bot.send_message(message.chat.id, "*Ссылки на конференции:*", reply_markup=keyboard, parse_mode="Markdown")
    elif message.text == "📕Среда":

        bot.send_message(message.from_user.id, schedule_today("АПО-20-1(а)", "Среда"))
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        arh_comp = types.InlineKeyboardButton(text="Zoom|Архитект.комп|Касимов И.Р.", url=links.get("Арх.Комп"))
        operac_sistem = types.InlineKeyboardButton(text="Zoom|Операц.сист.|Куликов В.П.", url=links.get("Операц.Систем"))
        filos = types.InlineKeyboardButton(text="Zoom|Философия|Баёв А.В.", url=links.get("Филос"))
        keyboard.add(arh_comp,operac_sistem,filos)
        bot.send_message(message.chat.id, "*Ссылки на конференции:*", reply_markup=keyboard, parse_mode="Markdown")
    elif message.text == "📕Четверг":

        bot.send_message(message.from_user.id, schedule_today("АПО-20-1(а)", "Четверг"))


    elif message.text == "📕Пятница":


        bot.send_message(message.from_user.id, schedule_today("АПО-20-1(а)", "Пятница"))

# конец а

# пн б
    elif message.text == "📗Понедельник":

        bot.send_message(message.from_user.id, schedule_today("АПО-20-1(б)", "Понедельник"))

    elif message.text == "📗Вторник":

        bot.send_message(message.from_user.id, schedule_today("АПО-20-1(а)", "Вторник"))
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        aks = types.InlineKeyboardButton(text="Zoom|АКС|Касимов И.Р.", url=links.get("АКС"))
        comp_seti = types.InlineKeyboardButton(text="Zoom|Комп.Сети|Куликов В.П.", url=links.get("Комп.Сети"))
        keyboard.add(aks,comp_seti)
        bot.send_message(message.chat.id, "*Ссылки на конференции:*", reply_markup=keyboard, parse_mode="Markdown")

    elif message.text == "📗Среда":

        bot.send_message(message.from_user.id, schedule_today("АПО-20-1(б)", "Среда"))
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        arh_comp = types.InlineKeyboardButton(text="Zoom|Архитект.комп|Касимов И.Р.", url=links.get("Арх.Комп"))
        operac_sistem = types.InlineKeyboardButton(text="Zoom|Операц.сист.|Куликов В.П.", url=links.get("Операц.Систем"))
        filos = types.InlineKeyboardButton(text="Zoom|Философия|Баёв А.В.", url=links.get("Филос"))
        keyboard.add(arh_comp,operac_sistem,filos)
        bot.send_message(message.chat.id, "*Ссылки на конференции:*", reply_markup=keyboard, parse_mode="Markdown")

    elif message.text == "📗Четверг":

        bot.send_message(message.from_user.id, schedule_today("АПО-20-1(б)", "Четверг"))


    elif message.text == "📗Пятница":

        bot.send_message(message.from_user.id, schedule_today("АПО-20-1(б)", "Пятница"))

# конец б

# пн 2
    elif message.text == "📘Понедельник":

        bot.send_message(message.from_user.id, schedule_today("АПО-20-2", "Понедельник"))

    elif message.text == "📘Вторник":

        bot.send_message(message.from_user.id, schedule_today("АПО-20-1(а)", "Вторник"))
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        aks = types.InlineKeyboardButton(text="Zoom|АКС|Касимов И.Р.", url=links.get("АКС"))
        comp_seti = types.InlineKeyboardButton(text="Zoom|Комп.Сети|Куликов В.П.", url=links.get("Комп.Сети"))
        keyboard.add(aks,comp_seti)
        bot.send_message(message.chat.id, "*Ссылки на конференции:*", reply_markup=keyboard, parse_mode="Markdown")

    elif message.text == "📘Среда":

        bot.send_message(message.from_user.id, schedule_today("АПО-20-2", "Среда"))
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        arh_comp = types.InlineKeyboardButton(text="Zoom|Архитект.комп|Касимов И.Р.", url=links.get("Арх.Комп"))
        operac_sistem = types.InlineKeyboardButton(text="Zoom|Операц.сист.|Куликов В.П.", url=links.get("Операц.Систем"))
        filos = types.InlineKeyboardButton(text="Zoom|Философия|Баёв А.В.", url=links.get("Филос"))
        keyboard.add(arh_comp,operac_sistem,filos)
        bot.send_message(message.chat.id, "*Ссылки на конференции:*", reply_markup=keyboard, parse_mode="Markdown")

    elif message.text == "📘Четверг":

        bot.send_message(message.from_user.id, schedule_today("АПО-20-2", "Четверг"))

    elif message.text == "📘Пятница":

        bot.send_message(message.from_user.id, schedule_today("АПО-20-2", "Пятница"))
#конец 2

while True:
    bot.polling(True)
