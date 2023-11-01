import sounddevice as sd
import queue
from vosk import Model, KaldiRecognizer
import time
import sys
from kommanden import help_sound


model = Model("small_model")
samplerate = 16000
device = 1

def va_listen(callback):
    q = queue.Queue()

    def q_callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
                           channels=1, callback=q_callback):
        rec = KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(rec.Result())

def listen_with_timeout(duration, process_audio_function):
    start_time = time.time()
    while time.time() - start_time < duration:
        result = process_audio_function()  # функция для обработки аудио и распознавания команд
        if result:  # Если команда распознана, выходим из функции
            return result
    return None  # Возвращаем None, если время истекло, и никаких команд не было распознано