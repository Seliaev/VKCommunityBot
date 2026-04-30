"""
VK Community Bot — бот для сообщества ВКонтакте
club238191003 | Long Poll API v5.199
"""
import asyncio
import sys
import logging
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text

from config import VK_TOKEN

# ── Исправление WinError 64 / aiohttp на Windows ──────────
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

bot = Bot(token=VK_TOKEN)

# ──────────────────────── Клавиатура ────────────────────────

MAIN_MENU = (
    Keyboard(one_time=False)
    .add(Text("📦 Каталог"), color=KeyboardButtonColor.PRIMARY)
    .add(Text("🛒 Корзина"), color=KeyboardButtonColor.SECONDARY)
    .row()
    .add(Text("📞 Контакты"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("❓ Помощь"), color=KeyboardButtonColor.SECONDARY)
    .get_json()
)

# ──────────────────────── Тексты ────────────────────────────

WELCOME = (
    "👋 Добро пожаловать!\n\n"
    "Я бот сообщества Portfolio. Помогу вам:\n"
    "• 📦 Просмотреть каталог\n"
    "• 🛒 Оформить заказ\n"
    "• 📞 Связаться с нами\n\n"
    "Выберите действие 👇"
)

HELP_TEXT = (
    "❓ Помощь\n\n"
    "Доступные команды:\n"
    "📦 Каталог — посмотреть товары\n"
    "🛒 Корзина — ваши товары\n"
    "📞 Контакты — связаться с нами\n\n"
    "По любым вопросам пишите нам!"
)

CONTACTS_TEXT = (
    "📞 Контакты\n\n"
    "🌐 Сайт: https://example.com\n"
    "📧 Email: info@example.com\n"
    "📱 Телефон: +7 (999) 123-45-67\n\n"
    "Работаем ежедневно 9:00–21:00 🕗"
)

CATALOG_TEXT = (
    "📦 Каталог товаров\n\n"
    "📱 Смартфоны — от 15 000 ₽\n"
    "💻 Ноутбуки — от 35 000 ₽\n"
    "🎧 Наушники — от 2 000 ₽\n"
    "🔌 Аксессуары — от 500 ₽\n\n"
    "Для заказа — пишите нам напрямую или звоните! 📞"
)

CART_TEXT = (
    "🛒 Ваша корзина пуста.\n\n"
    "Перейдите в 📦 Каталог чтобы выбрать товары!"
)

# ──────────────────────── Хендлеры ──────────────────────────

@bot.on.message()
async def handle_message(message: Message):
    text = (message.text or "").strip().lower()
    logger.info(f"Получено сообщение: '{text}' от {message.from_id}")

    if text in ("начать", "старт", "start", "привет", "привет!", "hi", "hello", "/start"):
        await message.answer(WELCOME, keyboard=MAIN_MENU)

    elif text in ("📦 каталог", "каталог", "catalog"):
        await message.answer(CATALOG_TEXT, keyboard=MAIN_MENU)

    elif text in ("🛒 корзина", "корзина", "cart"):
        await message.answer(CART_TEXT, keyboard=MAIN_MENU)

    elif text in ("📞 контакты", "контакты", "contact", "contacts"):
        await message.answer(CONTACTS_TEXT, keyboard=MAIN_MENU)

    elif text in ("❓ помощь", "помощь", "help", "/help"):
        await message.answer(HELP_TEXT, keyboard=MAIN_MENU)

    else:
        await message.answer(
            f"Вы написали: «{message.text}»\n\n"
            "Используйте кнопки меню 👇",
            keyboard=MAIN_MENU
        )


# ──────────────────────── Запуск ────────────────────────────

if __name__ == "__main__":
    logger.info("VK-бот запущен! Long Poll...")
    bot.run_forever()
