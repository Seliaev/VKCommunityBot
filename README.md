# 💬 VK CommunityBot — Бот для сообщества ВКонтакте

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![vkbottle](https://img.shields.io/badge/vkbottle-4.x-0077FF?style=flat-square&logo=vk&logoColor=white)](https://github.com/vkbottle/vkbottle)
[![VK API](https://img.shields.io/badge/VK%20API-5.199-0077FF?style=flat-square&logo=vk&logoColor=white)](https://dev.vk.com)

Демонстрационный бот для сообщества ВКонтакте. Автоответы, интерактивная клавиатура, каталог услуг и контакты — всё через Long Poll API.

🌐 **Демо-сообщество:** [vk.com/club238191003](https://vk.com/club238191003)

---

## ✨ Возможности

- ⌨️ **Клавиатура** — кастомная Reply-клавиатура с кнопками навигации
- 📋 **Каталог** — список услуг/товаров с описаниями
- 📞 **Контакты** — автоответ с контактной информацией
- 🔄 **Автоответы** — реакция на ключевые слова в сообщениях
- 📊 **Long Poll** — стабильная работа через VK Long Poll API

## 🛠 Стек

| Компонент | Технология |
|-----------|------------|
| Язык | Python 3.10+ |
| Фреймворк | vkbottle 4.x |
| API | VK API 5.199 |
| Transport | Long Poll |
| Деплой | VPS / любой хостинг |

## 📁 Структура проекта

```
vkbot/
├── bot.py              # Точка входа, запуск Long Poll
├── config.py           # Токен группы ВКонтакте
├── handlers/
│   ├── menu.py         # Главное меню, клавиатура
│   ├── catalog.py      # Каталог услуг
│   └── contacts.py     # Контакты
├── diagnose.py         # Диагностика подключения к VK API
└── requirements.txt
```

## 🚀 Запуск

```bash
git clone https://github.com/Seliaev/VKCommunityBot.git
cd VKCommunityBot
pip install -r requirements.txt
```

Создайте файл `.env` или отредактируйте `config.py`:

```python
VK_TOKEN = "токен_группы_вк"  # Управление → Работа с API
GROUP_ID = 123456789           # ID вашей группы ВКонтакте
```

```bash
python bot.py
```

## 💬 Команды / Кнопки

| Кнопка | Действие |
|--------|----------|
| 📋 Каталог | Список услуг |
| 📞 Контакты | Контактная информация |
| ❓ Помощь | Справка |

## 📸 Демонстрация

Напишите в сообщество: [vk.com/club238191003](https://vk.com/club238191003)

---

> Разработано [Denis Seliaev](https://github.com/Seliaev) · [Заказать похожий проект](https://kwork.ru/user/seliaev)
