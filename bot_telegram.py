import os

import telebot
from telebot import types

from dotenv import load_dotenv


load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))
bot.remove_webhook()

@bot.message_handler(commands=["start"])
def get_text_messages(message, data="start"):
    keyboard_main = types.InlineKeyboardMarkup()

    if data == "start":
        message_content = "Привет! Добро пожаловать в школу Антарес.\nНаши менеджеры уже зарегистрировали обращение от тебя и спешат ответить, однако пока не стоит тратить время зря: изучи возможности нашего бота-помощника ниже.\nМы ответим как можно скорее!🚀"
    elif data == "back":
        message_content = "Пока наши менеджеры спешат закончить общение с другими учениками и ответить тебе, изучи функционал бота-помощника.\n\nОбрати внимание на прохождение небольшого опроса по кнопке ниже, твои ответы значительно ускорят работу наших менеджеров🚀 Мы напишем как можно скорее!"

    btn_my_site = types.InlineKeyboardButton(text="Наш сайт", url="https://antarestudy.ru")
    btn_info = types.InlineKeyboardButton(text="Информация о курсах", callback_data="info")
    btn_manager = types.InlineKeyboardButton(text="Пройти опрос!", callback_data="manager")

    keyboard_main.add(btn_my_site)
    keyboard_main.add(btn_info)
    keyboard_main.add(btn_manager)

    return bot.send_message(
        message.chat.id,
        message_content,
        reply_markup = keyboard_main
    )

def get_info(message):
    keyboard_info = types.InlineKeyboardMarkup()

    btn_math_oge = types.InlineKeyboardButton(text="Математика ОГЭ", callback_data="math_oge")
    btn_math_ege = types.InlineKeyboardButton(text="Математика ЕГЭ", callback_data="math_ege")
    btn_physics_oge = types.InlineKeyboardButton(text="Физика ОГЭ", callback_data="physics_oge")
    btn_physics_ege = types.InlineKeyboardButton(text="Физика ЕГЭ", callback_data="physics_ege")
    btn_back = types.InlineKeyboardButton(text="Назад", callback_data="back")

    keyboard_info.add(btn_math_ege)
    keyboard_info.add(btn_physics_ege)
    keyboard_info.add(btn_math_oge)
    keyboard_info.add(btn_physics_oge)
    keyboard_info.add(btn_back)

    return bot.send_message(
        message.chat.id,
        "Выбери курс, который тебе интересен👇🏻",
        reply_markup = keyboard_info
    )

def get_subject_info(message, subject):
    doc = open("test.pdf", "rb")
    keyboard_subject = types.InlineKeyboardMarkup()

    btn_url = types.InlineKeyboardButton(text="Информация о курсе", url=f"https://antarestudy.ru/{subject}.html")
    btn_back = types.InlineKeyboardButton(text="На главную", callback_data="back")

    keyboard_subject.add(btn_url)
    keyboard_subject.add(btn_back)



    bot.send_message(
        message.chat.id,
        "Наш курс поможет тебе вместе с классными преподавателями в дружной группе получить знания по предмету и уверено подготовится к сдаче экзамена!😄"
        "\n\nЗагляни в учебный план из файла ниже, чтобы узнать подробно о распределении тем на занятиях, а также обрати внимание на скрин с тарифами, которые можно выбрать при покупке курса."
        "\n\nБолее подробное описание ты можешь прочитать на страничке курса на нашем сайте:",
        reply_markup=keyboard_subject
    )
    bot.send_document(message.chat.id, doc)
    if "Здорово, ты учишься" not in message.json["text"]:
        return bot.send_message(
            message.chat.id,
            "Если у тебя остались вопросы, не стесняйся их задавать здесь нашему менеджеру!"
        )
    return bot.send_message(
        message.chat.id,
        "Почему ты обратил внимание именно на нашу школу?",
    )

def get_age(message):
    keyboard_age = types.InlineKeyboardMarkup()

    btn_15 = types.InlineKeyboardButton(text="15", callback_data="15")
    btn_16 = types.InlineKeyboardButton(text="16", callback_data="16")
    btn_17 = types.InlineKeyboardButton(text="17", callback_data="17")
    btn_18 = types.InlineKeyboardButton(text="18", callback_data="18")
    btn_poll_end = types.InlineKeyboardButton(text="Закончить опрос", callback_data="poll_end")

    keyboard_age.add(btn_15)
    keyboard_age.add(btn_16)
    keyboard_age.add(btn_17)
    keyboard_age.add(btn_18)
    keyboard_age.add(btn_poll_end)


    bot.send_message(
        message.chat.id,
        "Наш менеджер скоро с тобой свяжется. А пока можешь рассказать о себе, чтобы нам было проще."
    )
    return bot.send_message(
        message.chat.id,
        "Сколько тебе лет?",
        reply_markup=keyboard_age
    )

def get_timezone(message, age):
    keyboard_timezone = types.InlineKeyboardMarkup()

    btn_neg1 = types.InlineKeyboardButton(text="МСК -1", callback_data="-1")
    btn_0 = types.InlineKeyboardButton(text="МСК", callback_data="0")
    btn_1 = types.InlineKeyboardButton(text="МСК +1", callback_data="1")
    btn_2 = types.InlineKeyboardButton(text="МСК +2", callback_data="2")
    btn_3 = types.InlineKeyboardButton(text="МСК +3", callback_data="3")
    btn_4 = types.InlineKeyboardButton(text="МСК +4", callback_data="4")
    btn_5 = types.InlineKeyboardButton(text="МСК +5", callback_data="5")
    btn_6 = types.InlineKeyboardButton(text="МСК +6", callback_data="6")
    btn_7 = types.InlineKeyboardButton(text="МСК +7", callback_data="7")
    btn_8 = types.InlineKeyboardButton(text="МСК +8", callback_data="8")
    btn_9 = types.InlineKeyboardButton(text="МСК +9", callback_data="9")
    btn_poll_end = types.InlineKeyboardButton(text="Закончить опрос", callback_data="poll_end")

    keyboard_timezone.add(btn_neg1)
    keyboard_timezone.add(btn_0)
    keyboard_timezone.add(btn_1)
    keyboard_timezone.add(btn_2)
    keyboard_timezone.add(btn_3)
    keyboard_timezone.add(btn_4)
    keyboard_timezone.add(btn_5)
    keyboard_timezone.add(btn_6)
    keyboard_timezone.add(btn_7)
    keyboard_timezone.add(btn_8)
    keyboard_timezone.add(btn_9)
    keyboard_timezone.add(btn_poll_end)

    return bot.send_message(
        message.chat.id,
        f"Здорово, тебе {age} лет!"
        "\n\n А теперь выбери свой часовой пояс:",
        reply_markup=keyboard_timezone
    )

def get_grade(message, timezone):
    keyboard_grade = types.InlineKeyboardMarkup()

    btn_9 = types.InlineKeyboardButton(text="9", callback_data="9 grade")
    btn_10 = types.InlineKeyboardButton(text="10", callback_data="10 grade")
    btn_11 = types.InlineKeyboardButton(text="11", callback_data="11 grade")
    btn_poll_end = types.InlineKeyboardButton(text="Закончить опрос", callback_data="poll_end")

    keyboard_grade.add(btn_9)
    keyboard_grade.add(btn_10)
    keyboard_grade.add(btn_11)
    keyboard_grade.add(btn_poll_end)

    return bot.send_message(
        message.chat.id,
        f"Здорово, твоя разница с Москвой в {timezone} час/а/ов!"
        "\n\nВ каком классе ты учишься?",
        reply_markup=keyboard_grade
    )

def get_exam(message, grade):
    grade = grade.split()[0]

    keyboard_exam = types.InlineKeyboardMarkup()

    btn_math_oge = types.InlineKeyboardButton(text="Математика ОГЭ", callback_data="math_oge")
    btn_math_ege = types.InlineKeyboardButton(text="Математика ЕГЭ", callback_data="math_ege")
    btn_physics_oge = types.InlineKeyboardButton(text="Физика ОГЭ", callback_data="physics_oge")
    btn_physics_ege = types.InlineKeyboardButton(text="Физика ЕГЭ", callback_data="physics_ege")
    btn_poll_end = types.InlineKeyboardButton(text="Закончить опрос", callback_data="poll_end")

    keyboard_exam.add(btn_math_ege)
    keyboard_exam.add(btn_physics_ege)
    keyboard_exam.add(btn_math_oge)
    keyboard_exam.add(btn_physics_oge)
    keyboard_exam.add(btn_poll_end)

    return bot.send_message(
        message.chat.id,
        f"Здорово, ты учишься в {grade} классе!"
        "\n\nКакие курсы тебя интересуют?",
        reply_markup=keyboard_exam
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
    if call.data == "info":
        return get_info(call.message)
    elif call.data == "math_oge" or call.data == "math_ege" or call.data == "physics_oge" or call.data == "physics_ege":
        return get_subject_info(call.message, call.data)
    elif call.data == "manager":
        return get_age(call.message)
    elif call.data >= "15" and call.data <= "18":
        age = call.data
        return get_timezone(call.message, age)
    elif call.data == "9 grade" or call.data == "10 grade" or call.data == "11 grade":
        grade = call.data
        return get_exam(call.message, grade)
    elif call.data >= "-1" and call.data <= "9":
        timezone = call.data
        return get_grade(call.message, timezone)
    elif call.data == "back":
        return get_text_messages(call.message, call.data)

bot.polling()
