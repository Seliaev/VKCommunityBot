"""Диагностика VK токена и Long Poll"""
import asyncio
from vkbottle import API
from vkbottle.bot import Bot

VK_TOKEN = "vk1.a.6gY8ez5dWB3GjAi8YbI5gB0oMj2ENicg_Wy42TGRm2t-QQKIfXd-HaiosmlAdqb7RVIt1qJql6Pm-0UbdRRUodfseQQa-KrakO-WWsB-UPYA9PyUy1YWUF6nzu6S7t3XFWV8xQxtWWyQGiP5pWJowiuTYyBf7KFiZIyykskbcoweKUcG6xCPw14-ntn2w3I9WS36f_mkX7xD06OXe8mzLg"
GROUP_ID = 238191003


async def diagnose():
    api = API(token=VK_TOKEN)

    print("=" * 50)
    print("1. Проверка токена (groups.getById)...")
    try:
        resp = await api.groups.get_by_id(group_id=GROUP_ID)
        g = resp.groups[0]
        print(f"   ✅ Группа: {g.name} | id={g.id} | is_admin={g.is_admin}")
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")

    print("\n2. Проверка Long Poll сервера (groups.getLongPollServer)...")
    try:
        lp = await api.groups.get_long_poll_server(group_id=GROUP_ID)
        print(f"   ✅ Long Poll: server={lp.server[:40]}...")
        print(f"   key={lp.key[:20]}... ts={lp.ts}")
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")
        print("   → Скорее всего токен не имеет прав 'messages' или 'manage'")

    print("\n3. Проверка настроек Long Poll (groups.getLongPollSettings)...")
    try:
        settings = await api.groups.get_long_poll_settings(group_id=GROUP_ID)
        print(f"   enabled={settings.is_enabled}")
        print(f"   message_new={settings.events.message_new}")
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")

    print("=" * 50)


asyncio.run(diagnose())
