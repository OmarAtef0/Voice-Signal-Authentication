import os
import sounddevice as sd
import speech_recognition as sr
import wavio
import numpy as np
import librosa
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
# from pyAudioAnalysis import audioBasicIO, audioFeatureExtraction

class VoiceRecognitionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.dataset_features = self.get_reference_features()
        self.audio_filename = "recorded_audio.wav"

    def init_ui(self):
        self.setWindowTitle('Voice Recognition App')

        self.label = QLabel('Recognition Result Will Appear Here', self)

        self.record_button = QPushButton('Record Audio', self)
        self.record_button.clicked.connect(self.start_recording)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.record_button)

        self.setLayout(layout)

    def start_listening(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print('Listening...')
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

        try:
            recognized_text = recognizer.recognize_google(audio)
            self.label.setText(f'Recognized Speech: {recognized_text}')

            # Save the recorded audio as a WAV file
            self.save_audio_to_wav(audio)

            # Extract features from the recorded audio
            user_features = self.extract_audio_features(self.audio_filename)

            # Display information about the extracted features (for demonstration purposes)
            if user_features:
                print("User Features:")
                for feature_name, feature_value in user_features.items():
                    print(f"{feature_name}: {feature_value.shape}")

                # Compare features with the reference features (your features)
                similarity_score = self.compare_features_with_reference(user_features)

                print(f"Cosine Similarity Score: {similarity_score}")

                # You can add logic here to determine access based on the similarity score

        except sr.UnknownValueError:
            self.label.setText('Speech Recognition could not understand audio')
        except sr.RequestError as e:
            self.label.setText(f'Speech Recognition request failed; {e}')

    def start_recording(self):
        duration = 5  # Set the recording duration in seconds
        recording = sd.rec(int(duration * 44100), samplerate=44100, channels=1, dtype='int16')
        sd.wait()

        # Save the recorded audio as a WAV file
        self.save_audio_to_wav(recording)

        print(f"Audio recorded and saved to {os.path.abspath(self.audio_filename)}")

        # Extract features from the recorded audio
        user_features = self.extract_audio_features(self.audio_filename)

        # Compare features with stored features
        similarity_scores = self.compare_features_with_dataset(user_features)

        # Update UI label based on the comparison result
        self.update_ui_label(similarity_scores)

    def save_audio_to_wav(self, audio_data):
        wavio.write(self.audio_filename, audio_data, 44100, sampwidth=3)

    def extract_audio_features(self, file_path):
        # Extract MFCC features from the recorded audio
        audio_signal, sampling_rate = librosa.load(file_path, sr=None)
        _, mfccs = audioFeatureExtraction.stFeatureExtraction(audio_signal, sampling_rate,
                                                               0.050 * sampling_rate, 0.025 * sampling_rate)
        return mfccs

    def save_audio_to_wav(self, audio_data):
        sample_rate = audio_data.sample_rate
        audio_array = audio_data.get_wav_data()

        wavio.write(self.audio_filename, audio_array, sample_rate, sampwidth=3)

        print(f"Audio saved to {os.path.abspath(self.audio_filename)}")

    def extract_audio_features(self, file_path):
        try:
            # Load the audio file
            audio_signal, sampling_rate = librosa.load(file_path, sr=None)

            # Chroma feature
            chroma = librosa.feature.chroma_stft(audio_signal, sr=sampling_rate)

            # Zero Crossing Rate
            zero_crossing_rate = librosa.feature.zero_crossing_rate(audio_signal)

            # Spectrogram
            spectrogram = np.abs(librosa.stft(audio_signal))

            # Spectral Contrast
            spectral_contrast = librosa.feature.spectral_contrast(audio_signal, sr=sampling_rate)

            # MFCCs (Mel-frequency cepstral coefficients)
            mfccs = librosa.feature.mfcc(audio_signal, sr=sampling_rate, n_mfcc=13)

            return {
                'chroma': chroma,
                'zero_crossing_rate': zero_crossing_rate,
                'spectrogram': spectrogram,
                'spectral_contrast': spectral_contrast,
                'mfccs': mfccs
            }

        except Exception as e:
            print(f"Error processing audio file: {e}")
            return None

    def compare_features_with_reference(self, user_features):
        # This function calculates the cosine similarity between user features and reference features (your features)
        # You can customize this function based on your specific needs and access control logic

        # Placeholder for reference features (your features)
        reference_features = self.get_reference_features()

        if reference_features is None:
            return None  # Handle the case where reference features are not available

        # Calculate cosine similarity
        similarity_score = self.cosine_similarity(user_features, reference_features)

        return similarity_score

    def get_reference_features(self):
        # Placeholder for reference features (your features)
        # You need to implement the logic to load or retrieve your reference features
        # from your database or any other storage mechanism
        # Example: Load the features from a file or database
                # Load audio files from the dataset folder
        # Extract features (e.g., MFCCs) from each audio file
        # Store the extracted features along with speaker labels
        dataset_features = {}  # Use a dictionary to store features by speaker label
        dataset_folder = 'dataset/open middle door/omar'

        for speaker_folder in os.listdir(dataset_folder):
            speaker_path = os.path.join(dataset_folder, speaker_folder)
            if os.path.isdir(speaker_path):
                for audio_file in os.listdir(speaker_path):
                    if audio_file.endswith('.wav'):
                        audio_path = os.path.join(speaker_path, audio_file)
                        features = self.extract_audio_features(audio_path)

                        # Store the features along with the speaker label
                        dataset_features.setdefault(speaker_folder, []).append(features)

        return dataset_features
  
    def compare_features_with_dataset(self, user_features):
        # Compare the features of the recorded audio with the stored features using cosine similarity
        similarity_scores = {}
        for speaker_label, speaker_features in self.dataset_features.items():
            avg_similarity_score = 0
            for stored_features in speaker_features:
                similarity_score = self.cosine_similarity(user_features, stored_features)
                avg_similarity_score += similarity_score

            # Calculate average similarity score for each speaker
            avg_similarity_score /= len(speaker_features)
            similarity_scores[speaker_label] = avg_similarity_score

        return similarity_scores

    @staticmethod
    def cosine_similarity(self, feature_vector1, feature_vector2):
        # This function calculates cosine similarity between two feature vectors
        # It's a simple example; you may need to customize it based on your requirements

        # Flatten the feature vectors
        flat_vector1 = feature_vector1['chroma'].flatten()
        flat_vector2 = feature_vector2['chroma'].flatten()

        # Calculate cosine similarity
        dot_product = np.dot(flat_vector1, flat_vector2)
        norm_vector1 = np.linalg.norm(flat_vector1)
        norm_vector2 = np.linalg.norm(flat_vector2)

        similarity_score = dot_product / (norm_vector1 * norm_vector2)

        return similarity_score
   
    def update_ui_label(self, similarity_scores):
        # Update the UI label based on the comparison result
        max_similarity_score = max(similarity_scores.values())
        best_matching_speaker = max(similarity_scores, key=similarity_scores.get)

        if max_similarity_score > 0.7:  # Adjust the threshold based on experimentation
            self.label.setText(f"Approved: Speaker {best_matching_speaker}")
        else:
            self.label.setText("Denied: No matching speaker found")
            

if __name__ == '__main__':
    app = QApplication([])
    window = VoiceRecognitionApp()
    window.show()
    app.exec_()
