import pvporcupine
import pyaudio

porcupine = pvporcupine.create(
    keywords=['jarvis']
)

pa = pyaudio.PyAudio()

audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

while True:

    pcm = audio_stream.read(porcupine.frame_length)

    pcm = memoryview(pcm).cast('h')

    keyword_index = porcupine.process(pcm)

    if keyword_index >= 0:
        print("Wake word detected")