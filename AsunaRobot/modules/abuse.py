import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from AsunaRobot import dispatcher
from AsunaRobot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "Bruh.",
    "Bahasa tu baik ke? ",
    "I came to know that some shops were selling your boobs for 69$
    "The world would have been so smooth if your dad had just pulled out",
    "And the truth is, you're a fucking cunt",
    "What else can you do other than spreading your legs?",
    "Jaa na Gandu",
    "2000000$ for tell abuse",
    "You sucks",
    "Bahasa baik sikit."
    "Bitches be trippin'",
    "Please fuck off bitch, and get a life",
    "hm",
    "eh",
    ":/",
    "I'm a good bot, do not abuse.",
)


@run_async
def dark(bot: Bot, update: Update):
    bot.sendChatAction(
        update.effective_chat.id, "typing"
    )  # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
        message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
        message.reply_text(random.choice(SFW_STRINGS))


__help__ = """
- /dark  🤬.
"""

__mod_name__ = "Abuse"

DARK_HANDLER = DisableAbleCommandHandler("dark", dark)

dispatcher.add_handler(DARK_HANDLER)
