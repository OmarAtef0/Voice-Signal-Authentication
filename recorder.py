import sounddevice as sd
import wavio as wv

def record_audio(duration, filename):
  print("RECORDING")
  fs = 44100
  recording = sd.rec(duration * fs, samplerate=fs, channels=2)
  sd.wait()
  wv.write(filename, recording, fs, sampwidth=2)

