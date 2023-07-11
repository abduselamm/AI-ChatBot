import telebot
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup  # States
# States storage
from telebot.storage import StateMemoryStorage
from chatBot import *

API_KEY = "6375285184:AAHPD3UZNrmbA4YfDLFKOcw7dWVoJMSW8vw"
state_storage = StateMemoryStorage()

bot = telebot.TeleBot(API_KEY, parse_mode=None,
                      state_storage=state_storage)


class MyStates(StatesGroup):
    question = State()


@bot.message_handler(commands=['start'])
def start_ex(message):
    """
    Start command. Here we are starting state
    """
    bot.set_state(message.from_user.id, MyStates.question, message.chat.id)
    bot.send_message(
        message.chat.id, 'Welcome to hubo Chatbot write any message you have')


@bot.message_handler(state=MyStates.question)
def ask_questions(message):
    print("me", message.text)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        # msg = (f"ans: {chat(data['question'])}\n"
        #        )
        data["question"] = message.text
        answer = chat(data["question"])
        msg = (f"ans: {answer}\n"
               )
        print("msg:", msg)
        bot.send_message(message.chat.id, msg, parse_mode="html")


# register filters
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())

bot.infinity_polling(skip_pending=True)
