import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

duration = 5
samplerate = 44100

print("Escuchando...")

audio = sd.rec(int(duration * samplerate), samplerate = samplerate, channels = 1, dtype = 'int16')
sd.wait()

write("audio.wav", samplerate, audio)

print("Procesando...")

model = WhisperModel("base", device = "cpu")
segments, info = model.transcribe("audio.wav", language="es")

for segment in segments:
    print(segment.text)