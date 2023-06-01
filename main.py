import telebot

# Replace 'TOKEN' with your bot token
bot_token = '6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc'

# Replace 'CHAT_LOG_ID' with the ID of the chat where you want to forward the messages
chat_log_id = '-1001832126466'

# Create a TeleBot instance
bot = telebot.TeleBot(bot_token)

# Register a message handler for forwarding messages
@bot.message_handler(func=lambda message: True)
def forward_message(message):
    # Forward the message to the specified chat log
    bot.forward_message(chat_log_id, message.chat.id, message.message_id)

# Start the bot
bot.polling()
