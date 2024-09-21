#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import config
import random
from random import choice
bot = telebot.TeleBot(config.token)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    username = message.from_user.username or "there"  # Fallback in case username is None
    bot.send_message(message.chat.id, f"""
    Hi {username}, I am a HelpBot😀👍 (ver1.03).
    I am here just to be here!\n----------\nCommands:\n /start Starts the bot\n /help Helps the bot\n goodbot Bot becomes friendly \n badbot Bot becomes unfriendly\n secret Bot says 1 secret about himself. (in Bottish, of course) """)

@bot.message_handler(commands=['fact'])
def fact(message):
    fact = choice(["You are currently talking with a bot.", "A bot is not a real person."])
    bot.reply_to(message, fact)


# Handle all other messages with content_type 'text'
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == 'goodbot':
        bot.send_message(message.chat.id, f"Yes, I know, {message.from_user.username or 'friend'}. I am a good one!")
    elif message.text == 'badbot':
        bot.send_message(message.chat.id, f"I am not bad ;/")
    elif message.text == 'secret':
        bot.send_message(message.chat.id, f"A_BgVY5j0av</yz2")
    elif message.text == 'info':
        bot.send_message(message.chat.id, "A helpful bot. Speaks Bottish. Responds to you.")
    elif message.text == 'photo':
        randomphoto = [
        'https://indieground.net/wp-content/uploads/2023/03/Freebie-GradientTextures-Preview-02.jpg',
        'https://images.ctfassets.net/h6goo9gw1hh6/2VwHU3zc2pQLXBRA7nxOoL/4a6608bbc21f485609aee930cb76e2e2/Gradient_Background_Example.jpg?w=750&h=750&fl=progressive&q=70&fm=jpg',
        'https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2020/02/Usign-Gradients-Featured-Image.jpg'
        ]
        bot.send_photo(message.chat.id, random.choice(randomphoto))
    
    else:
        bot.send_message(message.chat.id, f"Bot only speaks Bottish. Please take this into consideration.")


# Start polling
bot.infinity_polling()
