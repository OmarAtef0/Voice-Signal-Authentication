import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from speech_recognition import Recognizer, Microphone, AudioFile
import speech_recognition as sr
from scipy.io import wavfile
import librosa
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.effects import normalize
from pydub import AudioSegment

def cut_mp3(input_path, output_path, duration_minutes=10):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(input_path)

    # Set the desired duration in milliseconds
    duration_milliseconds = duration_minutes * 60 * 1000

    # Cut the audio to the specified duration
    cut_audio = audio[duration_milliseconds:duration_milliseconds*2]

    # Export the cut audio to a new MP3 file
    cut_audio.export(output_path, format="mp3")


def remove_silence_and_noise(input_audio_path, output_folder, subsegment_duration=5000):
    audio = AudioSegment.from_file(input_audio_path)
    audio = normalize(audio)
    segments = split_on_silence(audio, silence_thresh=-50)

    for i, segment in enumerate(segments):
        segment = normalize(segment)
        num_subsegments = len(segment) // subsegment_duration

        for j in range(num_subsegments):
            subsegment_start = j * subsegment_duration
            subsegment_end = (j + 1) * subsegment_duration
            subsegment = segment[subsegment_start:subsegment_end]

            output_path = os.path.join(output_folder, f"segment_{i + 1}_subsegment_{j + 1}.wav")
            subsegment.export(output_path, format="wav")

            recognizer = Recognizer()

            with AudioFile(output_path) as audio_file:
                audio_data = recognizer.record(audio_file, duration=5)  
                try:
                    spoken_sentence = recognizer.recognize_google(audio_data)
                    print(f"segment_{i + 1}_subsegment_{j + 1}.wav: {spoken_sentence}")
                except sr.UnknownValueError:
                    print("Speech not recognized. Please try again.")


input_audio_path = "output_cut.mp3"
output_folder = "C:/Users/omara/OneDrive/Desktop/second option/dataset/tamer"

input_path = "DSP-Lec6.mp3"
output_path = "output_cut.mp3"

# cut_mp3(input_path, output_path, duration_minutes=10)

remove_silence_and_noise(input_audio_path, output_folder)

