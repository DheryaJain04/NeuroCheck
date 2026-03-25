import numpy as np
import pyaudio as pya

def run_bnt_test():
    FORMAT = pya.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    THRESHOLD = 500

    p = pya.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True, output=True,
                    frames_per_buffer=CHUNK)

    print("* Recording... Speak now *")

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        frames.append(stream.read(CHUNK))

    print("* Recording complete *")

    stream.stop_stream()
    stream.close()
    p.terminate()

    audio_data = np.frombuffer(frames[0], dtype=np.int16)
    for i in range(1, len(frames)):
        audio_data = np.append(audio_data, np.frombuffer(frames[i], dtype=np.int16))

    energy = np.abs(audio_data)
    score = np.sum(energy> THRESHOLD)

    score = int(score/1000)
    return score