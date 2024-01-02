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

def remove_silence_and_noise(input_audio_path, output_folder, subsegment_duration=5000):
    audio = AudioSegment.from_file(input_audio_path)

    # Normalize the audio to enhance the volume
    audio = normalize(audio)

    # Split audio based on silence
    segments = split_on_silence(audio, silence_thresh=-50)

    for i, segment in enumerate(segments):
        # Normalize each segment individually
        segment = normalize(segment)

        # Calculate the number of subsegments
        num_subsegments = len(segment) // subsegment_duration

        for j in range(num_subsegments):
            # Extract subsegment of 5 seconds
            subsegment_start = j * subsegment_duration
            subsegment_end = (j + 1) * subsegment_duration
            subsegment = segment[subsegment_start:subsegment_end]

            # Save the subsegment as a separate audio file
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


input_audio_path = "ML/new audios/tamer/tamer2.m4a"
output_folder = "ML/new audios/tamer"

remove_silence_and_noise(input_audio_path, output_folder)

