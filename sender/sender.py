from telegram import Bot


class Sender:

    def __init__(
            self,
            telegramBotToken,
            telegramChannelId
    ):
        self.telegramBotToken = telegramBotToken
        self.telegramChannelId = telegramChannelId
        self.bot = Bot(self.telegramBotToken)

    def send(self, message):
        self.bot.send_message(
            chat_id=self.telegramChannelId,
            text=message
        )
