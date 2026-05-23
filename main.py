from faster_whisper import WhisperModel
from commands import open_spotify, open_brave
from voice import speak

import sounddevice as sd
from scipy.io.wavfile import write

duration = 5
samplerate = 44100

while True:
    print("Escuchando...")
    speak("Escuchando...")

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype='int16'
    )

    sd.wait()

    write("audio.wav", samplerate, audio)

    print("Procesando...")

    model = WhisperModel("base", device="cpu")

    segments, info = model.transcribe("audio.wav", language="es")

    texto_completo = ""

    for segment in segments:
        texto_completo += segment.text

    texto_completo = texto_completo.lower()

    print("Dijiste:", texto_completo)

    if "spotify" in texto_completo:
        speak("Abriendo Spotify")
        open_spotify()

    elif "navegador" in texto_completo:
        speak("Abriendo Brave")
        open_brave()
    elif "apagate" in texto_completo:
        speak("Esta bien señor, me retiro...")
        break
    else:
        speak("No entendí el comando")