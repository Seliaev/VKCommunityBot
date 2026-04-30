"""Echo-хендлер: отвечает на любое неизвестное сообщение"""
from vkbottle.bot import Bot, Message
from handlers.common import MAIN_MENU


def register(bot: Bot):

    @bot.on.message()
    async def handle_echo(message: Message):
        text = message.text or ""
        await message.answer(
            f"🤖 Вы написали: «{text}»\n\n"
            "Я пока не понимаю эту команду.\n"
            "Используйте кнопки меню 👇",
            keyboard=MAIN_MENU
        )
