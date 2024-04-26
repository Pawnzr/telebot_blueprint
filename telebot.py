import telebot

# Thay thế 'YOUR_TOKEN' bằng token của bot Telegram của bạn
bot = telebot.TeleBot('YOUR_TOKEN')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Xin chào! Đây là bot tính toán đơn giản. Gửi bất kỳ phép tính nào dưới dạng `/sum 3,1` để tính tổng.")


bot.polling()
