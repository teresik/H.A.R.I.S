import datetime
import os
import pygame

chao_sound_folder = 'sound/chaotageszeit'
hello_sound_folder = 'sound/tageszeithello'
os.makedirs(chao_sound_folder, exist_ok=True)
os.makedirs(hello_sound_folder, exist_ok=True)

chao_filename = ''
hello_filename = ''

def get_greeting():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Доброе утро, сэр!"
    elif 12 <= current_hour < 17:
        return "Добрый день, сэр!"
    elif 17 <= current_hour < 22:
        return "Добрый вечер, сэр!"
    else:
        return "Доброй ночи, сэр!"

def get_farewell():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Хорошего утра, сэр!"
    elif 12 <= current_hour < 17:
        return "Хорошего дня, сэр!"
    elif 17 <= current_hour < 22:
        return "Хорошего вечера, сэр!"
    else:
        return "Спокойной ночи, сэр!"

def va_sprech_chao(text):
    global chao_filename
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
            chao_filename = 'morgen.wav'
    elif 12 <= current_hour < 17:
            chao_filename = 'day.wav'
    elif 17 <= current_hour < 22:
            chao_filename = 'abend.wav'
    else:
            chao_filename = 'nights.wav'

    full_path_to_file = os.path.join(chao_sound_folder, chao_filename)
    
    # Воспроизведение файла
    pygame.mixer.init()
    pygame.mixer.music.load(full_path_to_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Подождать окончания воспроизведения
        pygame.time.Clock().tick(10)

def va_sprech_hallo(text):
    global hello_filename
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
            hello_filename = 'morgen.wav'
    elif 12 <= current_hour < 17:
            hello_filename = 'tag.wav'
    elif 17 <= current_hour < 22:
            hello_filename = 'abend.wav'
    else:
            hello_filename = 'nacht.wav'

    full_path_to_file = os.path.join(hello_sound_folder, hello_filename)

    # Воспроизведение файла
    pygame.mixer.init()
    pygame.mixer.music.load(full_path_to_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Подождать окончания воспроизведения
        pygame.time.Clock().tick(10)
