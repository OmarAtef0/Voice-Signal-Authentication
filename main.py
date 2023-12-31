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
import os

plt.rcParams['axes.facecolor'] = 'black'       # Background color of the plot area
plt.rc('axes', edgecolor='w')                  # Edge color of the plot area
plt.rc('xtick', color='w')                     # X-axis tick color
plt.rc('ytick', color='w')                     # Y-axis tick color
plt.rcParams['savefig.facecolor'] = 'black'    # Background color when saving figures
plt.rcParams["figure.autolayout"] = True       # Automatically adjust subplot parameters to fit the figure

class PreCalculate:
    def process_audio_data(self, label, individuals):
        data_dict = {}
        for i in individuals:
            files = os.listdir(f"dataset/{label}/{i}")
            for file in files:
                print(file)
                samples, sample_rate = librosa.load(file, sr=None)
                fft_result = np.fft.fft(samples)
                frequency = np.fft.fftfreq(len(fft_result), d=1/sample_rate)
                
                positive_frequency = frequency[frequency >= 0]
                f_amplitude = np.abs(fft_result[frequency >= 0])
                phase = np.angle(fft_result[frequency >= 0])

                data_dict[i] = {
                    'samples': samples,
                    'sample_rate': sample_rate,
                    'fft_result': fft_result,
                    'frequency': frequency,
                    'positive_frequencies': positive_frequency,
                    'f_amplitude': f_amplitude,
                    'phase': phase
                }
                
        return data_dict

    def prefind_fft(self):
        individuals = ["omar"]

        return self.process_audio_data("open middle door", individuals), self.process_audio_data("unlock the gate", individuals), self.process_audio_data("grant me access", individuals)

class VoiceSignalAuthentication(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  

        # pre_calculator = PreCalculate()
        # self.open_dict, self.unlock_dict, self.grant_dict = pre_calculator.prefind_fft()
        # print(self.open_dict[1])
        # print("CALCULATED")

        # Initialize SpeechRecognition components
        # self.recognizer = Recognizer()
        # self.microphone = Microphone()

        self.is_recording = False 
        self.recorded = False
        self.record_file = "dataset\\recorded\\1.wav"

        self.input_audio_data = {}
       
        self.ui.start_btn.clicked.connect(self.start_recording)

    def start_recording(self):
        self.is_recording = True

        try:
            recorder.record_audio(3, self.record_file)
            self.recorded = True
        except Exception as e:
            print(f"Error recording: {e}")

        self.open_audio(self.record_file)
        # self.process_audio()
    
    def process_audio(self):
        print("PROCESSING")
        recognizer = Recognizer()

        with AudioFile(self.record_file) as audio_file:
            audio_data = recognizer.record(audio_file, duration=5)  
            try:
                spoken_sentence = recognizer.recognize_google(audio_data)
                print("spoken_sentence: ",spoken_sentence)
            except sr.UnknownValueError:
                print("Speech not recognized. Please try again.")
            except sr.RequestError as e:
                print(f"Speech recognition service request failed; {e}")

        sentence_correct = self.sentence_check(spoken_sentence)
        print("sentence check: ",sentence_correct)
        if sentence_correct:
            self.check_person(spoken_sentence)

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

    # def sentence_check(self, spoken_sentence):
    #     valid_sentences = ["open middle door", "unlock the gate", "grant me access"]
    #     return any(sentence in spoken_sentence for sentence in valid_sentences)
    
    def sentence_check(self):
        pass  
        
    def open_audio(self, file_path):
        print("OPENED")
        self.reference_audio, sample_rate = librosa.load(file_path, sr=None)

        if self.recorded:
            self.plot_spectrogram(self.reference_audio, sample_rate)

        self.check_person()
        
    def check_person(self):
        folder_path = 'dataset\\mode_1_data'
        files = os.listdir(folder_path)
        similarity_percentages = {}

        # frequency amplitudes | spectrogram 

        for file in files:
            self.current_audio, sr_current = librosa.load(os.path.join(folder_path, file))
            min_length = min(len(self.reference_audio), len(self.current_audio))
            
            self.reference_audio = self.reference_audio[:min_length]
            self.current_audio = self.current_audio[:min_length]

            ref_stft_result = librosa.stft(self.reference_audio)
            self.ref_f_amplitude = np.abs(ref_stft_result)
            self.ref_spectrogram = np.abs(librosa.stft(self.reference_audio))

            stft_result = librosa.stft(self.current_audio)
            self.f_amplitude = np.abs(stft_result)
            self.spectrogram = np.abs(librosa.stft(self.current_audio))
            
            correlation_matrix = np.corrcoef(self.ref_f_amplitude, self.f_amplitude)
            absolute_correlation = np.abs(correlation_matrix)
            similarity_percentage = np.mean(absolute_correlation) * 100

            print(f"{self.record_file} and {file}: {similarity_percentage:.2f}%")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VoiceSignalAuthentication()
    window.setWindowTitle("Voice Signal Authentication")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6())
    app.setWindowIcon(QIcon("assets/logo.jpg"))
    window.resize(1150,750)
    window.show()
    sys.exit(app.exec_())
