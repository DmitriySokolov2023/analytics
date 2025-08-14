import telebot



def main():
    TOKEN = "8332783484:AAELGrRRNTfx9dT9pO8CoxMiWrj5evHclv4"

    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        print(message)
        bot.send_message(message.chat.id, "Привет! Я твой первый бот 🤖")

    @bot.message_handler(func=lambda message: True)
    def echo_message(message):
        bot.send_message(message.chat.id, f"Ты написал: {message.text}")

    print("Бот запущен...")
    bot.infinity_polling()

if __name__ == "__main__":
    main()