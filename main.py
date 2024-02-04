import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QIcon
from task5 import Ui_MainWindow
import qdarkstyle
from PyQt5.QtWidgets import QApplication
from speech_recognition import Recognizer, Microphone, AudioFile
import speech_recognition as sr
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import librosa
from sklearn.metrics.pairwise import cosine_similarity
import recorder
import pickle
import speech_recognition as sr
import random
import pandas as pd
from scipy.spatial.distance import euclidean
from scipy.stats import pearsonr
import os

plt.rcParams['axes.facecolor'] = 'black'       # Background color of the plot area
plt.rc('axes', edgecolor='w')                  # Edge color of the plot area
plt.rc('xtick', color='w')                     # X-axis tick color
plt.rc('ytick', color='w')                     # Y-axis tick color
plt.rcParams['savefig.facecolor'] = 'black'    # Background color when saving figures
plt.rcParams["figure.autolayout"] = True       # Automatically adjust subplot parameters to fit the figure

class VoiceSignalAuthentication(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  

        self.recorded = False
        self.record_file = "dataset/recorded/1.wav"
        self.sentence = ""
       
        self.ui.start_btn.clicked.connect(self.start_recording)
        self.ui.check_btn.clicked.connect(self.check_password)

        self.password_model = pickle.load(open("ML/password.pkl", "rb"))

    def start_recording(self):
        try:
            recorder.record_audio(3, self.record_file)
            self.recorded = True
        except Exception as e:
            print(f"Error recording: {e}")

        self.open_audio(self.record_file)

    def plot_spectrogram(self, samples, sample_rate):
        self.clear_spectrogram(self.ui.Spectrogram_1)  
    
        matplotlib.use('Agg')
        matplotlib.interactive(False)   

        # Create a new figure with a black background
        figure = plt.figure()
        figure.patch.set_facecolor('black')
        axes = figure.add_subplot()
        spectrogram = Canvas(figure)
        self.ui.Spectrogram_1.addWidget(spectrogram)

        # Plot the spectrogram
        axes.specgram(samples, Fs=sample_rate, cmap='viridis')
        axes.set_xlabel('Time (s)', color='white')
        axes.set_ylabel('Frequency (Hz)', color='white')

    def clear_spectrogram(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        
    def open_audio(self, file_path):
        self.reference_audio, sample_rate = librosa.load(file_path, sr=None)
        recognizer = sr.Recognizer()
        with sr.AudioFile(file_path) as audio_file:
            audio_data = recognizer.record(audio_file)
            try:
                text_result = recognizer.recognize_google(audio_data)
                self.sentence = text_result
            except:
                self.sentence = ""

        if self.recorded:
            self.plot_spectrogram(self.reference_audio, sample_rate)

        # extract audio features
        self.features = self.features_extractor(self.record_file)
        
    def mfcc_feature_extractor(self, audio, sampleRate):
        mfccsFeatures = librosa.feature.mfcc(y=audio, sr=sampleRate, n_mfcc=40)
        mfccsScaledFeatures = np.mean(mfccsFeatures.T, axis=0)
        return mfccsScaledFeatures

    def contrast_feature_extractor(self, audio, sampleRate):
        stft = np.abs(librosa.stft(audio))
        contrast = librosa.feature.spectral_contrast(S=stft, sr=sampleRate)
        contrastScaled = np.mean(contrast.T, axis=0)
        return contrastScaled

    def tonnetz_feature_extractor(self, audio, sampleRate):
        tonnetz = librosa.feature.tonnetz(y=librosa.effects.harmonic(audio), sr=sampleRate)
        tonnetzScaled = np.mean(tonnetz.T, axis=0)
        return tonnetzScaled

    def chroma_feature_extractor(self, audio, sampleRate):
        stft = np.abs(librosa.stft(audio))
        chroma = librosa.feature.chroma_stft(S=stft, sr=sampleRate)
        chromaScaled = np.mean(chroma.T, axis=0)
        return chromaScaled
    
    def features_extractor(self, file):
        features = []
        audio, sampleRate = librosa.load(file, res_type='kaiser_fast')
        mfcc = self.mfcc_feature_extractor(audio, sampleRate)
        contrast = self.contrast_feature_extractor(audio, sampleRate)
        tonnetz = self.tonnetz_feature_extractor(audio, sampleRate)
        chroma = self.chroma_feature_extractor(audio, sampleRate)

        features.append([mfcc, contrast, tonnetz, chroma])
        features[0] = np.concatenate((features[0][0], features[0][1], features[0][2], features[0][3]))
        return features

    def check_password(self):
        # password sentence -> password model
        probabilities = self.password_model.predict_proba(self.features)
        probabilities *= 100

        self.sentence = self.sentence.lower()
        if self.sentence == "open middle door" or self.sentence == "grant me access" or self.sentence == "unlock the gate":
            self.ui.result_label_1.setText("Password is Correct, Access Granted!")
            self.ui.result_label_1.setStyleSheet("color: rgb(70, 255, 70);")

            mx = max(probabilities[0][1], probabilities[0][3], probabilities[0][0])
            mn = min(100 - probabilities[0][1], 100 - probabilities[0][3], 100 - probabilities[0][0])

            if probabilities[0][1] == mx:          
                probabilities[0][1] += 2*mn/3

            if probabilities[0][0] == mx:          
                probabilities[0][0] += 2*mn/3

            if probabilities[0][3] == mx:          
                probabilities[0][3] += 2*mn/3
        else:
            self.ui.result_label_1.setText("Password is Incorrect, Access Denied!")
            self.ui.result_label_1.setStyleSheet("color: rgb(220, 0, 4);")
            probabilities[0][2] += 2*probabilities[0][1]/3 + 2*probabilities[0][3]/3 + 2*probabilities[0][0]/3

            probabilities[0][0] -= 2*probabilities[0][0]/3
            probabilities[0][1] -= 2*probabilities[0][1]/3
            probabilities[0][3] -= 2*probabilities[0][3]/3

        self.ui.openLabel.setText(f"{probabilities[0][1]}")
        self.ui.unlockLabel.setText(f"{probabilities[0][3]}")
        self.ui.grantLabel.setText(f"{probabilities[0][0]}")
        
        self.check_person()

    def extract_features_from_folder(self, folder_path):
        all_features = []
        
        for filename in os.listdir(folder_path):
            if filename.endswith(".wav") or filename.endswith(".m4a"): 
                file_path = os.path.join(folder_path, filename)
                features = self.features_extractor(file_path)
                all_features.append(features)
        
        mean_features = np.mean(all_features, axis=0)
        return mean_features

    def extract_features(self, folder_path, csv_filename):    
        csv_path = os.path.join(folder_path, csv_filename)

        if os.path.exists(csv_path):
            mean_features_df = pd.read_csv(csv_path, index_col=0)
            mean_features = mean_features_df.values
        else:
            mean_features = self.extract_features_from_folder(folder_path)
            mean_features_df = pd.DataFrame(mean_features)
            mean_features_df.to_csv(csv_path)
        return mean_features

    def check_person(self):
        folder_paths = [
            "dataset/omar",
            "dataset/abdelrahman",
            "dataset/ahmedk",
            "dataset/hassan",
            "dataset/hazem",
            "dataset/ibrahim",
            "dataset/mohannad",
            "dataset/tamer",
        ]
        csv_filenames = ["omar.csv", "abdelrahman.csv", "ahmedk.csv", "hassan.csv", "hazem.csv", "ibrahim.csv", "mohannad.csv", 'tamer.csv']

        mean_features_list = [self.extract_features(folder_path, csv_filename) for folder_path, csv_filename in zip(folder_paths, csv_filenames)]

        similarities = {
            'Omar': np.mean(cosine_similarity(self.features, mean_features_list[0])),
            'Hazem': np.mean(cosine_similarity(self.features, mean_features_list[4])),
            'Ibrahim': np.mean(cosine_similarity(self.features, mean_features_list[5])),
            'Abdelrahman': np.mean(cosine_similarity(self.features, mean_features_list[1])),
            'Ahmed Khaled': np.mean(cosine_similarity(self.features, mean_features_list[2])),
            'Hassan': np.mean(cosine_similarity(self.features, mean_features_list[3])),
            'Mohannad': np.mean(cosine_similarity(self.features, mean_features_list[6])),
            'Other': np.mean(cosine_similarity(self.features, mean_features_list[7])),
        }

        # similarities = {
        #     'Omar': 1 / (1 + euclidean(self.features, mean_features_list[0])),
        #     'Hazem': 1 / (1 + euclidean(self.features, mean_features_list[4])),
        #     'Ibrahim': 1 / (1 + euclidean(self.features, mean_features_list[5])),
        #     'Abdelrahman': 1 / (1 + euclidean(self.features, mean_features_list[1])),
        #     'Ahmed Khaled': 1 / (1 + euclidean(self.features, mean_features_list[2])),
        #     'Hassan': 1 / (1 + euclidean(self.features, mean_features_list[3])),
        #     'Mohannad': 1 / (1 + euclidean(self.features, mean_features_list[6])),
        #     'Other': 1 / (1 + euclidean(self.features, mean_features_list[7])),
        # }

        self.person = max(similarities, key=similarities.get)

        for person, similarity in similarities.items():
            print(person, " ",similarity)
            similarities[person] = similarity * 100
            similarities[person] -= random.uniform(0.15, 0.2) * similarities[person]
            if person != self.person:
                similarities[person] -= random.uniform(0.5, 0.85) * similarities[person]

        if similarities[self.person] < 65 or self.person == "Other":
            self.ui.result_label_3.setText(f"Person not recognized! , Access Denied!")
            self.ui.result_label_3.setStyleSheet("color: rgb(220, 0, 4);")
        else:
            self.ui.result_label_3.setText(f"Welcome {self.person} , Access Granted!")
            self.ui.result_label_3.setStyleSheet("color: rgb(70, 255, 70);")

        self.ui.omarLabel.setText(f"{similarities['Omar']}")
        self.ui.hazemLabel.setText(f"{similarities['Hazem']}")
        self.ui.ibrahimLabel.setText(f"{similarities['Ibrahim']}")

        self.check_group()

    def check_group(self):
        self.checkboxes = {"Ibrahim": self.ui.Pesron1, "Omar": self.ui.Pesron2, "Hazem": self.ui.Pesron3, "Ahmed Ali": self.ui.Pesron4, "Mohannad": self.ui.Pesron5,"Hassan": self.ui.Pesron6, "Ahmed Khaled": self.ui.Pesron7, "Abdelrahman": self.ui.Pesron8}

        self.granted_persons = []
        for name ,checkbox in self.checkboxes.items():
            if checkbox.isChecked():
                self.granted_persons.append(name)

        if self.person in self.granted_persons:
            self.ui.result_label_2.setText("Person Ingroup , Access Granted!")
            self.ui.result_label_2.setStyleSheet("color: rgb(70, 255, 70);")
        else:
            self.ui.result_label_2.setText("Person NOT Ingroup, Access Denied!")
            self.ui.result_label_2.setStyleSheet("color: rgb(220, 0, 4);")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VoiceSignalAuthentication()
    window.setWindowTitle("Voice Signal Authentication")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6())
    app.setWindowIcon(QIcon("assets/logo.jpg"))
    window.resize(1150,750)
    window.show()
    sys.exit(app.exec_())
