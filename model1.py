import librosa
import numpy as np
import os
import matplotlib.pyplot as plt

def calculate_similarity_percentage(correlation_matrix):
    absolute_correlation = np.abs(correlation_matrix)
    
    similarity_percentage = np.mean(absolute_correlation) * 100

    return similarity_percentage

def main():
    reference_audio_name = 'dataset\open middle door\omar\omar_open_middle_door_1.wav'
    reference_audio, sr_reference = librosa.load(reference_audio_name)

    ref_stft_result = librosa.stft(reference_audio)
    ref_f_amplitude = np.abs(ref_stft_result)

    # ref_chroma = librosa.feature.chroma_stft(y=reference_audio, sr=sr_reference)
    # ref_zero_crossing_rate = librosa.feature.zero_crossing_rate(reference_audio)
    ref_spectrogram = np.abs(librosa.stft(reference_audio))
    # ref_spectral_contrast = librosa.feature.spectral_contrast(y=reference_audio, sr=sr_reference)
    # ref_mfccs = librosa.feature.mfcc(y=reference_audio, sr=sr_reference, n_mfcc=13)

    folder_path = 'dataset\\mode_1_data'
    files = os.listdir(folder_path)
    similarity_percentages = {}

    # frequency amplitudes | spectrogram 

    for file in files:
        current_audio, sr_current = librosa.load(os.path.join(folder_path, file))
        min_length = min(len(reference_audio), len(current_audio))

        reference_audio = reference_audio[:min_length]
        current_audio = current_audio[:min_length]

        stft_result = librosa.stft(current_audio)
        f_amplitude = np.abs(stft_result)

        # chroma = librosa.feature.chroma_stft(y=current_audio, sr=sr_current)
        # zero_crossing_rate = librosa.feature.zero_crossing_rate(current_audio)
        spectrogram = np.abs(librosa.stft(current_audio))
        # spectral_contrast = librosa.feature.spectral_contrast(y=current_audio, sr=sr_current)
        # mfccs = librosa.feature.mfcc(y=current_audio, sr=sr_current, n_mfcc=13)
        
        correlation_matrix = np.corrcoef(ref_spectrogram, spectrogram)

        similarity_percentage = calculate_similarity_percentage(correlation_matrix)
        print(f"{reference_audio_name} and {file}: {similarity_percentage:.2f}%")

        # plt.figure(figsize=(10, 6))

        # plt.subplot(3, 1, 1)
        # plt.plot(reference_audio)
        # plt.title(f'{reference_audio_name}')

        # plt.subplot(3, 1, 2)
        # plt.plot(current_audio)
        # plt.title(f'{file}')

        # plt.subplot(3, 1, 3)
        # plt.imshow(correlation_matrix, cmap='viridis', aspect='auto')
        # plt.title('Correlation Matrix')

        # plt.tight_layout()
        # plt.show()

        similarity_percentages[file] = similarity_percentage

if __name__ == "__main__":
    main()
