@echo off
REM Скрипт запуска VK-бота (изолированное окружение)

set BOTDIR=%~dp0
set VENV=%BOTDIR%venv\Scripts\python.exe

if not exist "%VENV%" (
    echo [VKBot] Создание окружения...
    py -3.12 -m venv "%BOTDIR%venv"
    "%BOTDIR%venv\Scripts\pip.exe" install vkbottle -q
)

echo [VKBot] Запуск...
"%VENV%" "%BOTDIR%bot.py"

pause
