import numpy as np
import matplotlib.pyplot as plt
import librosa.display

def plot_fft(ax0, ax1, samples, sample_rate, title='Frequency Spectrum'):
    fft_result = np.fft.fft(samples)
    frequencies = np.fft.fftfreq(len(fft_result), d=1/sample_rate)
    
    positive_frequencies = frequencies[frequencies >= 0]
    amplitude = np.abs(fft_result[frequencies >= 0])
    phase = np.angle(fft_result[frequencies >= 0])

    ax0.set_title(title)
    ax0.plot(positive_frequencies, amplitude)
    ax0.set_xlabel('Frequency (Hz)')
    ax0.set_ylabel('Amplitude')

    ax1.set_title("Phase")
    ax1.plot(positive_frequencies[0:100], phase[0:100])
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('Radian')

def plot_time_domain(ax, samples, sample_rate, title='Time Domain Plot'):
    time = np.arange(0, len(samples)) / sample_rate

    ax.set_title(title)
    ax.plot(time, samples)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')

def plot_spectrogram(ax, samples, sample_rate, title='Spectrogram'):
    _, _, Sxx, _ = plt.specgram(samples, Fs=sample_rate, cmap='viridis')

    ax.set_title(title)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Frequency (Hz)')


def process_mp3(file_path):
    samples, sample_rate = librosa.load(file_path, sr=None)

    fig, axes = plt.subplots(4, 1, figsize=(10, 10))

    plot_time_domain(axes[0], samples, sample_rate, title='Time Domain Plot')

    plot_fft(axes[1], axes[2], samples, sample_rate, title='Frequency Spectrum')

    plot_spectrogram(axes[3], samples, sample_rate, title='Spectrogram')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    mp3_file_path = 'dataset/open middle door/1.mp3'  
    process_mp3(mp3_file_path)
