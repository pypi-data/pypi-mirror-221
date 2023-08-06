import telegram

TELEGRAM_TOKEN = '6046676015:AAE0mU59JvPklD6Abuqwp_HSVFwHFyRyZtc'
TELEGRAM_CHAT_ID = '-846401867'

def send_notification_telegram():
    # Set up the Telegram Bot
    bot = telegram.Bot(token=TELEGRAM_TOKEN)

    try:
        # Send a test message to the specified chat ID
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text='This is a test message from the setup.py script.')
        print("Test message sent successfully via Telegram!")
    except telegram.error.TelegramError as e:
        print(f"Error sending the test message via Telegram: {e}")

if __name__ == "__main__":
    send_notification_telegram()
