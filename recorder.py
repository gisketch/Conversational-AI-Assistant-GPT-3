import pyaudio
import wave
import keyboard

def record_audio(audio, r, sr):
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    print("Recording...")
    frames = []
    while True:
        # Read raw microphone data
        data = stream.read(1024)
        frames.append(data)
        if keyboard.is_pressed("e"):
            print("Done recording\n\n")
            break

    stream.stop_stream()
    stream.close()
    # audio.terminate()

    sound_file = wave.open("./temp/myrecording.wav", "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()

    r = sr.Recognizer()
    tempsound = sr.AudioFile("./temp/myrecording.wav")

    try:
        with tempsound as source:
            transcribed = r.record(source)
            return r.recognize_google(transcribed)
    except Exception as e:
        print(e)
        return "<Inaudible voice from human...>"