import librosa
import numpy as np

N_FFT = 1024
K_HOP = 256

def read_audio_spectum(filename):
    x, fs = librosa.load(filename) #x=audiodata, fs=samplerate
    R = np.abs(librosa.stft(x, n_fft=N_FFT, hop_length=K_HOP, win_length=N_FFT, center=True))
    print(fs)
    return R, fs
file="inputs/lemons.mp3"
read_audio_spectum(file)