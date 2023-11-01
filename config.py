import sounddevice as sd
import queue
from vosk import Model, KaldiRecognizer

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