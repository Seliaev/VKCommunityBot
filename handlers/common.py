"""Хендлеры: /start, помощь, меню"""
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text

MAIN_MENU = (
    Keyboard(one_time=False)
    .add(Text("📦 Каталог"), color=KeyboardButtonColor.PRIMARY)
    .add(Text("🛒 Корзина"), color=KeyboardButtonColor.SECONDARY)
    .row()
    .add(Text("📞 Контакты"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("❓ Помощь"), color=KeyboardButtonColor.SECONDARY)
    .get_json()
)

WELCOME = (
    "👋 Добро пожаловать!\n\n"
    "Я бот сообщества Portfolio. Помогу вам:\n"
    "• 📦 Просмотреть каталог\n"
    "• 🛒 Оформить заказ\n"
    "• 📞 Связаться с нами\n\n"
    "Выберите действие 👇"
)

HELP_TEXT = (
    "❓ <b>Помощь</b>\n\n"
    "Доступные команды:\n"
    "📦 Каталог — посмотреть товары\n"
    "🛒 Корзина — ваши товары\n"
    "📞 Контакты — связаться с нами\n\n"
    "По любым вопросам пишите нам!"
)

CONTACTS_TEXT = (
    "📞 <b>Контакты</b>\n\n"
    "🌐 Сайт: https://example.com\n"
    "📧 Email: info@example.com\n"
    "📱 Телефон: +7 (999) 123-45-67\n\n"
    "Работаем ежедневно 9:00–21:00 🕗"
)

CATALOG_TEXT = (
    "📦 <b>Каталог товаров</b>\n\n"
    "🔋 Смартфоны — от 15 000 ₽\n"
    "💻 Ноутбуки — от 35 000 ₽\n"
    "🎧 Наушники — от 2 000 ₽\n"
    "📱 Аксессуары — от 500 ₽\n\n"
    "Для заказа — пишите нам напрямую или звоните! 📞"
)


def register(bot: Bot):

    @bot.on.message(text=["начать", "старт", "start", "привет", "привет!"])
    async def handle_start(message: Message):
        await message.answer(WELCOME, keyboard=MAIN_MENU)

    @bot.on.message(text=["помощь", "help", "❓ помощь"])
    async def handle_help(message: Message):
        await message.answer(HELP_TEXT, keyboard=MAIN_MENU)

    @bot.on.message(text=["📞 контакты", "контакты", "contact"])
    async def handle_contacts(message: Message):
        await message.answer(CONTACTS_TEXT, keyboard=MAIN_MENU)

    @bot.on.message(text=["📦 каталог", "каталог", "catalog"])
    async def handle_catalog(message: Message):
        await message.answer(CATALOG_TEXT, keyboard=MAIN_MENU)

    @bot.on.message(text=["🛒 корзина", "корзина", "cart"])
    async def handle_cart(message: Message):
        await message.answer(
            "🛒 Ваша корзина пуста.\n\n"
            "Перейдите в 📦 Каталог чтобы выбрать товары!",
            keyboard=MAIN_MENU
        )
