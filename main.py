import telebot

# Replace 'TOKEN' with your bot token
bot_token = '6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc'

# Replace 'GROUP_ID' with the ID of the group where the bot will save the chats
log_group_id = '-1001832126466'

# Create a SingleInstanceBot instance
bot = telebot.TeleBot(bot_token)
bot = telebot.SingleInstanceBot(bot)

# Register a message handler for all incoming messages in any group
@bot.message_handler(func=lambda message: True)
def save_chat(message):
    chat_id = message.chat.id

    if message.text:
        chat_message = f"{message.from_user.username}: {message.text}"
        bot.send_message(log_group_id, chat_message)
    elif message.photo:
        # Forward the first photo in the message
        photo = message.photo[-1]
        bot.send_photo(log_group_id, photo.file_id)
    elif message.video:
        # Forward the video
        bot.send_video(log_group_id, message.video.file_id)
    elif message.document:
        # Forward the document
        bot.send_document(log_group_id, message.document.file_id)
    elif message.sticker:
        # Forward the sticker
        bot.send_sticker(log_group_id, message.sticker.file_id)

# Start the bot
bot.polling()
