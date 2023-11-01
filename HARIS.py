from pvporcupine import create as create_porcupine
from pvrecorder import PvRecorder

import config
from fuzzywuzzy import fuzz

import kommanden
from kommanden import command_actions
from kommanden import command_sound

from time_utils import get_greeting, get_farewell
from time_utils import va_sprech_chao, va_sprech_hallo

import levafuz

import sounddevice as sd
import numpy as np

from govor import va_speak
from config import va_listen

import os
import pygame

import random
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="fuzzywuzzy")

command_sound_folder = 'sound/commands'
os.makedirs(command_sound_folder, exist_ok=True)

# Инициализация Porcupine и Vosk
porcupine = create_porcupine(
    access_key="4X9zKzThgV0uBeZc1LrkKBtjXE6AvNXnfdX3itvyOxv0Ny3XYX8xaw==",
    keyword_paths=["Model_Haris.ppn"]
)
recorder = PvRecorder(device_index=1, frame_length=porcupine.frame_length)

def play_sound(file_path): # Воспроизведение файла
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Подождать окончания воспроизведения
        pygame.time.Clock().tick(10)

def process_recognized_text(text):
    category = levafuz.process_command(text)
    if category:
        kommanden.execute(category)
    else:
        print("Команда не распознана.")

def record_command(duration=5, samplerate=16000):
    """ Записывает аудио в течение заданного времени (в секундах) """
    print("Запись команды...")
    myrecording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float64')
    sd.wait()  # Ждем окончания записи
    print("Запись завершена.")
    text = byte_data.decode(myrecording, 'utf-8')

    return text

def record_until_silence(threshold=0.02, silence_duration=1, sample_rate=16000):
    buffer = []
    silent_frames = 0
    silence_frames = int(silence_duration * sample_rate)

    def callback(indata, frames, time, status):
        nonlocal silent_frames
        if np.abs(indata).mean() < threshold:
            silent_frames += 1
            if silent_frames > silence_frames:
                raise sd.CallbackStop
        else:
            silent_frames = 0
        buffer.append(indata.copy())

    with sd.InputStream(callback=callback, samplerate=sample_rate, channels=1):
        try:
            sd.sleep(int(10 * 1000))  # 10 секундный тайм-аут
        except sd.CallbackStop:
            pass

    return np.concatenate(buffer, axis=0)

def handle_command(command_text):

    # Получение списка файлов в директории 'sound/command'
    command_files = os.listdir(command_sound_folder)
    # Выбор случайного файла
    random_file = random.choice(command_files)
    full_path_to_file = os.path.join(command_sound_folder, random_file)
    play_sound(full_path_to_file)

    # Используем levafuz для определения команды
    recognized_command = levafuz.process_command(command_text)
    if recognized_command in command_actions:
        command_actions[recognized_command]()
    else:
        print("Команда не распознана.")

listening_enabled = True  # По умолчанию прослушивание выключено

def main():
    print("H.A.R.I.S (v1.0) начал свою работу ...")
    recorder.start()

    try:
        while True:
            pcm = recorder.read()
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print(get_greeting())
                farewell_message = get_farewell()  # Получаем приветственное сообщение
                va_sprech_hallo(farewell_message)
                va_listen(process_recognized_text)
                if keyword_detected:  # Предположим, что это условие проверяет обнаружение ключевого слова
                    audio = record_until_silence()
                    # Теперь у вас есть запись команды, которую можно отправить на обработку


    except KeyboardInterrupt:
        print("\nЗавершение работы H.A.R.I.S ...")
        print(get_farewell())
        farewell_message = get_farewell()  # Получаем прощальное сообщение
        va_sprech_chao(farewell_message)

    finally:
        recorder.stop()

if __name__ == "__main__":
    main()
