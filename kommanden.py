from time_utils import get_greeting, get_farewell
from govor import va_speak
import os
import pygame
import random
import webbrowser

hello_sound_folder = 'sound/hello'
chao_sound_folder = 'sound/chao'
command_sound_folder = 'sound/commands'
os.makedirs(command_sound_folder, exist_ok=True)
os.makedirs(chao_sound_folder, exist_ok=True)
os.makedirs(hello_sound_folder, exist_ok=True)

def greet():
    return get_greeting()

def remind():
    va_speak("Что вам напомнить, сэр?")

def farewell():
    return get_farewell()

def execute(category):
    if category == "Приветствие":

        hello_sound()

        print("Привет! Чем могу помочь?")

    elif category == "Контроль освещения":
        pass

    elif category == "Управление музыкой":
        url = "https://open.spotify.com/"

        webbrowser.open_new(url)
        chrome_path = 'D:\Projects\VEGA\programs'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open(url)

    elif category == "Прощание":
        print("Прощание")

        chao_sound()


# Добавьте здесь другие функции для обработки команд

def play_sound(file_path): # Воспроизведение файла
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Подождать окончания воспроизведения
        pygame.time.Clock().tick(10)

def command_sound():
    # Получение списка файлов в директории 'sound/hello'
    command_files = os.listdir(command_sound_folder)
    # Выбор случайного файла
    random_file = random.choice(command_files)
    full_path_to_file = os.path.join(command_sound_folder, random_file)
    play_sound(full_path_to_file)

def hello_sound():
    # Получение списка файлов в директории 'sound/hello'
    hello_files = os.listdir(hello_sound_folder)
    # Выбор случайного файла
    random_file = random.choice(hello_files)
    full_path_to_file = os.path.join(hello_sound_folder, random_file)
    play_sound(full_path_to_file)

def chao_sound():
    # Получение списка файлов в директории 'sound/hello'
    chao_files = os.listdir(chao_sound_folder)
    # Выбор случайного файла
    random_file = random.choice(chao_files)
    full_path_to_file = os.path.join(chao_sound_folder, random_file)
    play_sound(full_path_to_file)

command_actions = {
    "Приветствие": greet,
    "Контроль освещения": remind,
    "Прощание": farewell,
    # Другие команды и соответствующие им функции
}