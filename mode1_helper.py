import librosa
import numpy as np
import os
import matplotlib.pyplot as plt

def calculate_similarity_percentage(correlation_matrix):
    # Use the absolute correlation values
    absolute_correlation = np.abs(correlation_matrix)

    # Calculate the average similarity percentage
    similarity_percentage = np.mean(absolute_correlation) * 100

    return similarity_percentage

def main():
    # Replace 'audio1.wav' and 'audio2.wav' with your file paths
    folder_path = 'dataset\\test'

    # List all files in the folder
    files = os.listdir(folder_path)

    # Select the first two .wav files
    file_path1 = os.path.join(folder_path, files[0])
    file_path2 = os.path.join(folder_path, files[1])

    # Load audio files
    audio1, sr1 = librosa.load(file_path1)
    audio2, sr2 = librosa.load(file_path2)

    # Ensure both audio signals have the same length
    min_length = min(len(audio1), len(audio2))
    audio1 = audio1[:min_length]
    audio2 = audio2[:min_length]

    # Compute 2D correlation
    correlation_matrix = np.corrcoef(audio1, audio2)

    # Calculate and print similarity percentage
    similarity_percentage = calculate_similarity_percentage(correlation_matrix)
    print(f"Similarity Percentage: {similarity_percentage:.2f}%")

    # Plot the two audio signals
    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(audio1)
    plt.title('Audio 1')

    plt.subplot(3, 1, 2)
    plt.plot(audio2)
    plt.title('Audio 2')

    plt.subplot(3, 1, 3)
    plt.imshow(correlation_matrix, cmap='viridis', aspect='auto')
    plt.title('Correlation Matrix')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
