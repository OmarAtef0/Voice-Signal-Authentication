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
    # Replace 'record.wav' with the name of your reference audio
    reference_audio_name = 'record.wav'
    
    # Replace 'dataset\\test' with the path to your audio files
    folder_path = 'dataset\\test'

    # List all files in the folder
    files = os.listdir(folder_path)

    # Find the index of the reference audio
    record_index = files.index(reference_audio_name)
    
    # Remove the reference audio from the list
    del files[record_index]

    # Load the reference audio
    reference_audio, sr_reference = librosa.load(os.path.join(folder_path, reference_audio_name))

    # Initialize a dictionary to store similarity percentages
    similarity_percentages = {}

    # Iterate over the remaining audios
    for file in files:
        # Load the current audio
        current_audio, sr_current = librosa.load(os.path.join(folder_path, file))

        # Ensure both audio signals have the same length
        min_length = min(len(reference_audio), len(current_audio))
        reference_audio = reference_audio[:min_length]
        current_audio = current_audio[:min_length]

        # Compute 2D correlation
        correlation_matrix = np.corrcoef(reference_audio, current_audio)

        # Calculate similarity percentage
        similarity_percentage = calculate_similarity_percentage(correlation_matrix)
        
        # Print similarity percentage
        print(f"Similarity Percentage between {reference_audio_name} and {file}: {similarity_percentage:.2f}%")

        # Plot the two audio signals and the correlation matrix
        plt.figure(figsize=(10, 6))

        plt.subplot(3, 1, 1)
        plt.plot(reference_audio)
        plt.title(f'{reference_audio_name}')

        plt.subplot(3, 1, 2)
        plt.plot(current_audio)
        plt.title(f'{file}')

        plt.subplot(3, 1, 3)
        plt.imshow(correlation_matrix, cmap='viridis', aspect='auto')
        plt.title('Correlation Matrix')

        plt.tight_layout()
        plt.show()

        # Store the similarity percentage in the dictionary
        similarity_percentages[file] = similarity_percentage

    # Print the similarity percentages for all comparisons
    print("\nSimilarity Percentages:")
    for file, similarity_percentage in similarity_percentages.items():
        print(f"{file}: {similarity_percentage:.2f}%")

if __name__ == "__main__":
    main()
