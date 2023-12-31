import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
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
            samples, sample_rate = librosa.load(f"dataset/{label}/{i}.mp3", sr=None)
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
        individuals = [1, 2, 3, 4, 5, 6, 7, 8]

        return self.process_audio_data("open middle door", individuals), self.process_audio_data("unlock the gate", individuals), self.process_audio_data("grant me access", individuals)

class VoiceSignalAuthentication(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  

        pre_calculator = PreCalculate()
        self.open_dict, self.unlock_dict, self.grant_dict = pre_calculator.prefind_fft()
        print(self.open_dict[1])

        print("CALCULATED")

        # Initialize SpeechRecognition components
        self.recognizer = Recognizer()
        self.microphone = Microphone()

        self.is_recording = False 
        self.recorded = False
        self.file_path = "dataset\\recorded\\1.wav"

        self.input_audio_data = {}
       
        self.ui.start_btn.clicked.connect(self.start_recording)

    def start_recording(self):
        self.is_recording = True

        try:
            recorder.record_audio(5, self.file_path)
            self.recorded = True
        except Exception as e:
            print(f"Error recording: {e}")

        self.open_audio(self.file_path)
        self.process_audio()
    
    def process_audio(self):
        print("PROCESSING")
        recognizer = Recognizer()

        with AudioFile(self.file_path) as audio_file:
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
        
    def open_audio(self, file_path):
        print("OPENED")
        samples, sample_rate = librosa.load(file_path, sr=None)

        if self.recorded:
            self.plot_spectrogram(samples, sample_rate)
            
        fft_result = np.fft.fft(samples)
        frequency = np.fft.fftfreq(len(fft_result), d=1/sample_rate)
        
        positive_frequency = frequency[frequency >= 0]
        f_amplitude = np.abs(fft_result[frequency >= 0])
        phase = np.angle(fft_result[frequency >= 0])

        self.input_audio_data = {
            'samples': samples,
            'sample_rate': sample_rate,
            'fft_result': fft_result,
            'frequency': frequency,
            'positive_frequencies': positive_frequency,
            'f_amplitude': f_amplitude,
            'phase': phase
        }

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
        
        audio1 = self.input_audio_data
        # loop over the 10 random audios
        audio2 = {0}
        

        #COMPARE BETWEEN 2 AUDIOS

        # 'samples': samples,
        # 'sample_rate': sample_rate,
        # 'fft_result': fft_result,
        # 'frequency': frequency,
        # 'positive_frequencies': positive_frequency,
        # 'amplitude': amplitude,
        # 'phase': phase
        

    def check_person(self, spoken_sentence):
        for i in range(1,11):
            audio1 = self.input_audio_data

            if spoken_sentence == "open middle door":
                audio2 = self.open_dict[i]
            elif spoken_sentence == "unlock the gate":
                audio2 = self.unlock_dict[i]
            elif spoken_sentence == "grant me access":
                audio2 = self.grant_dict[i]    

            #COMPARE BETWEEN 2 AUDIOS

            # 'samples': samples,
            # 'sample_rate': sample_rate,
            # 'fft_result': fft_result,
            # 'frequency': frequency,
            # 'positive_frequencies': positive_frequency,
            # 'amplitude': amplitude,
            # 'phase': phase

            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VoiceSignalAuthentication()
    window.setWindowTitle("Voice Signal Authentication")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6())
    # app.setWindowIcon(QIcon("assets/logo.jpg"))
    window.resize(1450,950)
    window.show()
    sys.exit(app.exec_())
