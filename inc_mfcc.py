import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def increase_mfcc(audio_path):
    y, sr = librosa.load(audio_path)
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    y_synthesized = librosa.feature.inverse.mfcc_to_audio(mfccs)

    return y_synthesized

def save_audio(audio, output_path, sr):
    sf.write(output_path, audio, sr)

def process_audio_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            input_audio_path = os.path.join(input_folder, filename)
            output_audio_path = os.path.join(output_folder, f"modified_{filename}")

            modified_audio = increase_mfcc(input_audio_path)
            save_audio(modified_audio, output_audio_path, sr=librosa.get_samplerate(input_audio_path))
            print(f"Processed: {filename} => Saved to: {output_audio_path}")

if __name__ == "__main__":
    input_folder_path = "C:/Users/omara/OneDrive/Desktop/Voice Signal Authentication/dataset/mohannad"
    output_folder_path = "C:/Users/omara/OneDrive/Desktop/Voice Signal Authentication/dataset/mohannad/output"

    process_audio_folder(input_folder_path, output_folder_path)
