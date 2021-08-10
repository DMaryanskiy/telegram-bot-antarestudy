import telebot
from telebot import types


bot = telebot.TeleBot("1919927766:AAGH0dBYZ4yuw46vgw5L5F4uw6jKE5FPzHI")
bot.remove_webhook()

@bot.message_handler(commands=["start"])
def get_text_messages(message):
    keyboard_main = types.InlineKeyboardMarkup()

    btn_my_site = types.InlineKeyboardButton(text="Наш сайт", url="https://antarestudy.ru")
    btn_info = types.InlineKeyboardButton(text="Информация о школе", callback_data="info")
    btn_manager = types.InlineKeyboardButton(text="Связаться с менеджером", callback_data="manager")

    keyboard_main.add(btn_my_site)
    keyboard_main.add(btn_info)
    keyboard_main.add(btn_manager)

    return bot.send_message(
        message.chat.id,
        "Здравствуйте! Выберите, что Вас интересует:"
        "\n 1) Информация о школе."
        "\n 2) Связаться с менеджером."
        "\n\n Также Вы можете перейти на наш сайт и ознакомиться со всем материалом там.",
        reply_markup = keyboard_main
    )

def get_info(message):
    keyboard_info = types.InlineKeyboardMarkup()

    btn_math_oge = types.InlineKeyboardButton(text="Математика ОГЭ", callback_data="math_oge")
    btn_math_ege = types.InlineKeyboardButton(text="Математика ЕГЭ", callback_data="math_ege")
    btn_physics_oge = types.InlineKeyboardButton(text="Физика ОГЭ", callback_data="physics_oge")
    btn_physics_ege = types.InlineKeyboardButton(text="Физика ЕГЭ", callback_data="physics_ege")
    btn_back = types.InlineKeyboardButton(text="Назад", callback_data="back")

    keyboard_info.add(btn_math_oge)
    keyboard_info.add(btn_math_ege)
    keyboard_info.add(btn_physics_oge)
    keyboard_info.add(btn_physics_ege)
    keyboard_info.add(btn_back)

    return bot.send_message(
        message.chat.id,
        "Выберите интересующий Вас курс:"
        "\n 1) Математика ОГЭ."
        "\n 2) Математика ЕГЭ."
        "\n 3) Физика ОГЭ."
        "\n 4) Физика ЕГЭ.",
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
        "Всю информацию Вы можете найти на нашем сайте и в pdf файле",
        reply_markup=keyboard_subject
    )
    return bot.send_document(message.chat.id, doc)

def get_age(message):
    keyboard_age = types.InlineKeyboardMarkup()

    btn_15 = types.InlineKeyboardButton(text="15", callback_data="15")
    btn_16 = types.InlineKeyboardButton(text="16", callback_data="16")
    btn_17 = types.InlineKeyboardButton(text="17", callback_data="17")
    btn_18 = types.InlineKeyboardButton(text="18", callback_data="18")

    keyboard_age.add(btn_15)
    keyboard_age.add(btn_16)
    keyboard_age.add(btn_17)
    keyboard_age.add(btn_18)

    bot.send_message(
        message.chat.id,
        "Наш менеджер скоро с Вами свяжется. А пока можете рассказать о себе,"
        "чтобы было проще Вам помочь."
    )
    return bot.send_message(
        message.chat.id,
        "Укажите Ваш возраст.",
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

    return bot.send_message(
        message.chat.id,
        f"Отлично, Ваш возраст {age} лет!"
        "\n\nУкажите Ваш часовой пояс.",
        reply_markup=keyboard_timezone
    )

def get_exam(message, timezone):
    keyboard_exam = types.InlineKeyboardMarkup()

    btn_oge = types.InlineKeyboardButton(text="ОГЭ", callback_data="oge")
    btn_ege = types.InlineKeyboardButton(text="ЕГЭ", callback_data="ege")

    keyboard_exam.add(btn_oge)
    keyboard_exam.add(btn_ege)

    return bot.send_message(
        message.chat.id,
        f"Отлично, Ваша разница с Москвой в {timezone} час/а/ов!"
        "\n\nУкажите Ваш уровень подготовки.",
        reply_markup=keyboard_exam
    )

def get_subject(message, exam):
    keyboard_subj = types.InlineKeyboardMarkup()

    btn_math = types.InlineKeyboardButton(text="Математика", callback_data="math")
    btn_physics = types.InlineKeyboardButton(text="Физика", callback_data="physics")

    keyboard_subj.add(btn_math)
    keyboard_subj.add(btn_physics)

    return bot.send_message(
        message.chat.id,
        f"Отлично, Ваш уровень подготовки {exam}!"
        "\n\nУкажите интересующий Вас предмет.",
        reply_markup=keyboard_subj
    )

def end_poll(message, subject):
    subj_dict = {
        "math": "математика",
        "physics": "физика",
    }
    return bot.send_message(
        message.chat.id,
        f"Отлично, Ваc интересует {subj_dict[subject]}!"
        "\n\nСпасибо за прохождение опроса! Наш менеджер скоро свяжется с Вами.",
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
    elif call.data >= "-1" and call.data <= "9":
        timezone = call.data
        return get_exam(call.message, timezone)
    elif call.data == "oge" or call.data == "ege":
        exam = call.data
        return get_subject(call.message, exam)
    elif call.data == "math" or call.data == "physics":
        subject = call.data
        return end_poll(call.message, subject)
    elif call.data == "back":
        return get_text_messages(call.message)

bot.polling()
