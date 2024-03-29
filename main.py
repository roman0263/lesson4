class User:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.name = None
        self.issue = None
        self.symptoms = None
        self.service_type = None  # 'online' или 'home_visit'
        self.contact = None  # Телефон
        self.username = None  # Ник в Telegram
        self.address = {"street": None, "house_number": None, "entrance": None, "floor": None, "apartment": None, "intercom": None}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для вызова семейного врача на дом в г. Москва в районах Бутово. Для вызова врача используйте команду /call_doctor.")

@bot.message_handler(commands=['call_doctor'])
def call_doctor(message):
    msg = bot.send_message(message.chat.id, "Что случилось?")
    bot.register_next_step_handler(msg, process_issue_step)



@bot.message_handler(commands=['confirm'])
def confirm_call(message):
    if message.chat.id != ADMIN_CHAT_ID:
        bot.reply_to(message, "Эта команда только для администратора.")
        return
    try:
        _, call_id = message.text.split()
        call_id = int(call_id)
        if call_id in call_requests:
            call_requests[call_id] = 'Принят'
            bot.send_message(ADMIN_CHAT_ID, f"Вызов {call_id} принят.")
        else:
            bot.send_message(ADMIN_CHAT_ID, "Вызов не найден.")
    except Exception as e:
        bot.send_message(ADMIN_CHAT_ID, f"Ошибка: {str(e)}")

@bot.message_handler(commands=['calls'])
def list_calls(message):
    if message.chat.id != ADMIN_CHAT_ID:
        bot.reply_to(message, "Эта команда только для администратора.")
        return
    if not call_requests:
        bot.send_message(ADMIN_CHAT_ID, "Список вызовов пуст.")
        return
    calls_list = [f"ID вызова: {call_id}, статус: {status}" for call_id, status in call_requests.items()]
    bot.send_message(ADMIN_CHAT_ID, "\n".join(calls_list))

if __name__ == '__main__':
    bot.polling(none_stop=True)

