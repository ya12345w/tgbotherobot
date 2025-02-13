import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7758387247:AAEF-7dFTkHCYZ4esD2zduaLXC61Zcbw1qk"

bot = telebot.TeleBot(TOKEN)

class Hero:
    def __str__(self):
        return f"{self.Name}"
    def __init__(self, name , damage, health, magic_list, speed, energy, mana, krit, classes):
        self.Name=name
        self.Damage=damage
        self.Health=health
        self.Magic_list=magic_list
        self.Speed=speed
        self.Energy=energy
        self.Mana=mana
        self.Krit=krit
        self.Classes=classes
    def wait(self):
        return "герой ждет ваш ход"
    def evade(self):
        return random.randint(0, 100) <= self.Speed
    def atack(self, h1, h2):
        krit_chanse = 1
        if random.randint(0.100) <= self.Krit:
            krit_chanse = 2
        atack_count = h1.dammage * krit_chanse
        h2.health = h2.health - atack_count
        return f"{h1.name} атаковал {h2.name} на {atack_count}"


    class Hero_classes:
        def __init__(self): #закончи с классами здесь
            pass


rases = [
    Hero("Человек", 100, 2000, [], 50, 100, 100, 20, []),
    Hero("Орк",150, 2000, [], 30, 100, 100, 30, []),
    Hero("Эльф", 100, 1600, [], 75, 100, 100, 20, []),
    Hero("Голем", 100, 2500, [], 20, 100, 100, 15, []),
    Hero("Демон", 200,1000, [], 50, 100, 150, 20, [])
]

commands = [
    "start",
    "help",
    "choise_race",
    "choise_class",
    "show_info",
]

classes = [

]

magics = [

]

true1 = False

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

def generate_race_buttons(races=rases):
    markup = InlineKeyboardMarkup()
    for race in races:
        markup.add(InlineKeyboardButton(text=race.Name, callback_data=f'race_{race.Name}'))
    return markup
def generate_class_buttons():
    markup = InlineKeyboardMarkup()
    for class1 in classes

@bot.message_handler(commands=commands[2])
def send_welcome(message):
    bot.send_message(message.chat.id, "Выберите свою расу:", reply_markup=generate_race_buttons())

@bot.callback_query_handler(func=lambda call: call.data.startswith('race_'))
def handle_race_selection(call):
    global selected_race, true1
    selected_race = call.data[5:]
    true1 = True
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    bot.send_message(call.message.chat.id, f'Вы выбрали: {selected_race}')
    bot.answer_callback_query(call.id)

@bot.message_handler(commands=commands[3])
def class_choise(message):
    if true1 == True:
        bot.send_message(message.chat.id, f"Выберите класс для {selected_race}", )




bot.polling()