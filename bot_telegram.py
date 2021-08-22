import os
import telebot
from telebot import types

from dotenv import load_dotenv


load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))
bot.remove_webhook()

info = {
    "username": "",
    "course": "",
    "age": "",
    "timezone": "",
    "grade": "",
}

@bot.message_handler(commands=["start"])
def get_text_messages(message, data="start"):
    keyboard_main = types.InlineKeyboardMarkup()

    if data == "start":
        message_content = "Привет! Добро пожаловать в школу Антарес.\nИзучи возможности нашего бота-помощника, по всем вопросам не стесняйся писать нашим менеджерам: @antarestudy"
    if data == "back":
        message_content = "С возвращением!\nУзнай подробнее о курсах из меню ниже или напиши нашим менеджерам: @antarestudy"

    btn_my_site = types.InlineKeyboardButton(text="Наш сайт", url="https://antarestudy.ru")
    btn_info = types.InlineKeyboardButton(text="Информация о курсах", callback_data="info")

    keyboard_main.add(btn_my_site)
    keyboard_main.add(btn_info)

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

    doc = open(f"{subject}.pdf", "rb")
    img = open(f"{subject}.png", "rb")

    keyboard_subject = types.InlineKeyboardMarkup()

    btn_url = types.InlineKeyboardButton(text="Описание курса на сайте", url=f"https://antarestudy.ru/{subject}.html")
    btn_back = types.InlineKeyboardButton(text="На главную", callback_data="back")

    keyboard_subject.add(btn_url)
    keyboard_subject.add(btn_back)

    bot.send_message(
        message.chat.id,
        "Наш курс поможет тебе вместе с классными преподавателями в дружной группе получить знания по предмету и уверено подготовится к сдаче экзамена!😄"
        "\n\nЗагляни в учебный план из файла ниже, чтобы узнать подробно о распределении тем на занятиях, а также обрати внимание на скрин с тарифами, которые можно выбрать при покупке курса."
    )
    bot.send_document(message.chat.id, doc)
    bot.send_photo(message.chat.id, img)
    return bot.send_message(
        message.chat.id,
        "\n\nБолее подробное описание ты можешь прочитать на страничке курса на нашем сайте:",
        reply_markup=keyboard_subject
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
    if call.data == "info":
        return get_info(call.message)
    elif call.data == "math_oge" or call.data == "math_ege" or call.data == "physics_oge" or call.data == "physics_ege":
        return get_subject_info(call.message, call.data)
    elif call.data == "back":
        return get_text_messages(call.message, call.data)

bot.polling()
