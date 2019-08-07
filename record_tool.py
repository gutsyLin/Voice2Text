import pyaudio

from keyboard_det import is_enter_press

def record_pcm1600():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_LIMIT = 60
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print('* recording')
    
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_LIMIT)):
            data = stream.read(CHUNK)
            frames.append(data)
            if is_enter_press():
                break
    
    print('* done recording')
    stream.stop_stream()
    stream.close()
    p.terminate()

    return b''.join(frames)

if __name__ == '__main__':
    record_pcm1600()
