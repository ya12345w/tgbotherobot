import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7758387247:AAEF-7dFTkHCYZ4esD2zduaLXC61Zcbw1qk"

bot = telebot.TeleBot(TOKEN)

class Hero:
    def __str__(self):
        return f"{self.Name}"
    def __init__(self, name , damage, health, magic_list, speed, energy, mana, classes):
        self.Name=name
        self.Damage=damage
        self.Health=health
        self.Magic_list=magic_list
        self.Speed=speed
        self.Energy=energy
        self.Mana=mana
        self.Classes=classes
    def wait(self):
        return "герой ждет ваш ход"
    def atack(self):
        if random.randint() <= self.Speed:
            pass
        #допиши шанс уклонения

commands = [
    "start",
    "help",
    "choise_race",
    "choise_class",
    "show_info"
]

rasez = [
    Hero("Человек", 100, 2000, [], 50, 100, 100, []),
    Hero("Орк",150, 2000, [], 30, 100, 100, []),
    Hero("Эльф", 100, 1600, [], 75, 100, 100, []),
    Hero("Голем", 100, 2500, [], 20, 100, 100, []),
    Hero("Демон", 200,1000, [], 50, 100, 150, [])
]

magics = [

]

races = []
for i in rasez:
    races.append(i)

@bot.message_handler(commands=commands[0])
def start(message):
    bot.reply_to(message,
        f"Привет, {message.from_user.first_name}! \n"
        "Я бот по RPG игре. Рад познакомиться! \n"
        "/help"
    )

@bot.message_handler(commands=commands[1])
def help(message):
    all='\n/'.join(commands)
    bot.send_message(message.chat.id,f"/{all}")

def generate_race_buttons():
    markup = InlineKeyboardMarkup()
    for race in races:
        markup.add(InlineKeyboardButton(text=race.Name, callback_data=f'race_{race.Name}'))
    return markup

@bot.message_handler(commands=commands[2])
def send_welcome(message):
    bot.send_message(message.chat.id, "Выберите свою расу:", reply_markup=generate_race_buttons())

@bot.callback_query_handler(func=lambda call: call.data.startswith('race_'))
def handle_race_selection(call):
    selected_race = call.data[5:]
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    bot.send_message(call.message.chat.id, f'Вы выбрали: {selected_race}')
    bot.answer_callback_query(call.id)



bot.polling()