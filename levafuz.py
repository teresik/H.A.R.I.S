from fuzzywuzzy import process
from kommanden import command_sound
import os

from kommanden import play_sound
from kommanden import command_sound

import random

command_sound_folder = 'sound/commands'
os.makedirs(command_sound_folder, exist_ok=True)

SOME_THRESHOLD = 80

# Список команд с грамматическими вариациями
komtegory = {
    "Приветствие": [
        "привет", "здравствуй", "добрый день", "приветствую", "доброго времени суток", "хеллоу", "здоров"
                    ],

    "Контроль освещения": [
        "включи свет", "освети комнату", "свет включить", "зажги лампу", "лампу включи"
        "выключи свет", "потуши свет", "лампу выключи", "осветление выкл", "темнее сделай"
    ],

    "Управление музыкой": [
        "включи музыку", "музыку воспроизведи", "начни воспроизведение", "мелодию включи", "играй музыку"   
        "выключи музыку", "останови музыку", "музыку останови", "паузу нажми", "мелодию выключи"
    ],

    "Погода": [
        "какая погода", "погоду скажи", "прогноз погоды", "как на улице", "сведения о погоде"
    ],

    "Напоминания": [
        "напомни мне", "запиши напоминание", "не забыть про", "напоминание создай", "напомнить о"
    ],

    "Поиск информации": [
        "найди информацию", "поиск в интернете", "загугли это", "искать в сети", "информацию найти"
    ],
    "Время и будильник": [
        "который час", "скажи время", "текущее время", "часы покажи", "время сейчас"
        "установи будильник", "разбуди меня в", "будильник на", "подъем в", "будить в"
    ],
    "Запросы к календарю": [
        "что в планах", "покажи календарь", "мероприятия на сегодня", "мои задачи", "расписание на день"
    ],
    "Управление звонками": [
        "позвони", "сделай звонок", "набери номер", "свяжись с", "звонок на"
    ],
    "Прощание": [
        "Пока", "Прощай"
    ]
    # Добавьте здесь другие команды с их вариациями
    # ...
}


def process_command(command_text):
    command_sound()

    # Получение списка файлов и воспроизведение случайного файла
    command_files = os.listdir(command_sound_folder)
    random_file = random.choice(command_files)
    full_path_to_file = os.path.join(command_sound_folder, random_file)
    play_sound(full_path_to_file)

    # Ищем наилучшее соответствие для команды
    best_match = None
    highest_score = 0

    for category, command_variants in komtegory.items():
        match, score = process.extractOne(command_text, command_variants)
        if score > highest_score:
            highest_score = score
            best_match = category

    return best_match if highest_score >= 60 else None  # Минимальный порог точности

# Пример использования:
# print(process_command("Привет, как дела?"))  # Например, вернет "привет"
