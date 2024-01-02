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
        self.record_file = "dataset\\recorded\\1.wav"
       
        self.ui.start_btn.clicked.connect(self.start_recording)
        self.ui.check_btn.clicked.connect(self.check_password)

        # self.ingroup_model = pickle.load(open("ingroup.pkl", "rb"))
        self.processing_model = pickle.load(open("ML/processing.pkl", "rb"))
        self.password_model = pickle.load(open("ML/password.pkl", "rb"))

    def start_recording(self):
        try:
            recorder.record_audio(3, self.record_file)
            self.recorded = True
        except Exception as e:
            print(f"Error recording: {e}")

        self.open_audio(self.record_file)

    def plot_spectrogram(self, samples, sample_rate):
        print("PLOTTED")
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
        
    def open_audio(self, file_path):
        print("OPENED")
        self.reference_audio, sample_rate = librosa.load(file_path, sr=None)

        if self.recorded:
            self.plot_spectrogram(self.reference_audio, sample_rate)

        # extract audio features
        self.features = self.features_extractor(self.record_file)
        
    def mfcc_feature_extractor(self, audio, sampleRate):
        print("called")
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

    def centroid_feature_extractor(self, audio, sampleRate):
        centroid = librosa.feature.spectral_centroid(y=audio, sr=sampleRate)
        centroidScaled = np.mean(centroid.T, axis=0)
        return centroidScaled

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
        password_model_prediction = self.password_model.predict(self.features)
        probabilities = self.password_model.predict_proba(self.features)
        print("password: ", probabilities)
        
        if password_model_prediction == 0:
            self.ui.result_label_1.setText("Password is Correct, Access Granted!")
            self.ui.result_label_1.setStyleSheet("color: rgb(70, 255, 70);")
        else:
            self.ui.result_label_1.setText("Password is Incorrect, Access Denied!")
            self.ui.result_label_1.setStyleSheet("color: rgb(220, 0, 4);")
        
        self.check_person()

    def check_person(self):
        # meen el person -> processing model
        # person_prediction = self.processing_model.predict(self.features)

        probabilities = self.processing_model.predict_proba(self.features)
        print("persons: ", probabilities)

        for i in range(len(self.features)):
            class_pred_index = probabilities[i].argmax()  
            class_pred = probabilities[i, class_pred_index]  
            threshold = 0.70
            
            if class_pred > threshold:
                person_prediction = class_pred_index
            else:
                person_prediction =  7
        
        self.person = ""

        if person_prediction == 0:
            self.person = "Ahmed Ali"
        elif person_prediction == 1:
            self.person = "Ahmed Khaled"
        elif person_prediction == 2:
            self.person = "Hassan"
        elif person_prediction == 3:
            self.person = "Hazem"
        elif person_prediction == 4:
            self.person = "Ibrahim"
        elif person_prediction == 5:
            self.person = "Mohannad"
        elif person_prediction == 6:
            self.person = "Omar"
        elif person_prediction == 7:
            self.person = "other"
        
        if self.person == "other":
            self.ui.result_label_3.setText(f"Person not recognized! , Access Denied!")
            self.ui.result_label_3.setStyleSheet("color: rgb(220, 0, 4);")
        else:
            self.ui.result_label_3.setText(f"Welcome {self.person} , Access Granted!")
            self.ui.result_label_3.setStyleSheet("color: rgb(70, 255, 70);")

        self.check_group()

    def check_group(self):
        # ingroup wla la-> ingroup model
        self.checkboxes = {"Ibrahim": self.ui.Pesron1, "Omar": self.ui.Pesron2, "Hazem": self.ui.Pesron3, "Ahmed Ali": self.ui.Pesron4, 
                           "Mohannad": self.ui.Pesron5,"Hassan": self.ui.Pesron6,}
        self.granted_persons = []
        for name ,checkbox in self.checkboxes.items():
            if checkbox.isChecked():
                self.granted_persons.append(name)

        print("granted persons: ", self.granted_persons)

        print("talking peson: ",self.person)
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
