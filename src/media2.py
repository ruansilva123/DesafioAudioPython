import wave
import numpy as np
import matplotlib.pyplot as plt


def current_spectogram(wave_file):

    with wave.open(wave_file, 'r') as wav:
        frame_rate = wav.getframerate()
        num_frames = wav.getnframes()

        raw_data = wav.readframes(num_frames)

        audio_data = np.frombuffer(raw_data, dtype=np.int16)

        plt.specgram(audio_data, NFFT=1024, Fs= frame_rate, noverlap=512)
        plt.title('Espectrograma')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Frequência (Hz)')
        plt.colorbar(label='Intensidade (dB)')
        plt.show()


def alter_spectogram(wave_file, output_file, cutoff_freq = [], bandwidth = 100):
    
    with wave.open(wave_file, 'r') as wav:
        num_channels = wav.getnchannels()
        sample_width = wav.getsampwidth()
        frame_rate = wav.getframerate()
        num_frames = wav.getnframes()

        raw_data = wav.readframes(num_frames)

        audio_data = np.frombuffer(raw_data, dtype=np.int16)

        plt.specgram(audio_data, NFFT=1024, Fs= frame_rate, noverlap=512)
        plt.title('Espectrograma')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Frequência (Hz)')
        plt.colorbar(label='Intensidade (dB)')
        plt.show()

        freq_data = np.fft.fft(audio_data)

        freqs = np.fft.fftfreq(len(audio_data), d=1/frame_rate)

        for notch_freq in cutoff_freq:
            freq_data[np.abs(freqs - notch_freq) ] # finalizar

        filtered_audio_data = np.fft.ifft(freq_data)

        filtered_audio_data = np.real(filtered_audio_data).astype(np.int16)

        with wave.open(output_file, 'wb') as output_wav:
            output_wav.setnchannels(num_channels)
            output_wav.setsampwidth(sample_width)
            output_wav.setframerate(frame_rate)
            output_wav.writeframes(filtered_audio_data.tobytes())

    with wave.open(output_file, 'r') as wav:
        frame_rate = wav.getframerate()
        num_frames = wav.getnframes()

        raw_data = wav.readframes(num_frames)

        audio_data = np.frombuffer(raw_data, dtype=np.int16)

        plt.specgram(audio_data, NFFT=1024, Fs= frame_rate, noverlap=512)
        plt.title('Espectrograma')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Frequência (Hz)')
        plt.colorbar(label='Intensidade (dB)')
        plt.show()


if __name__ == "__main__":

    ...
    # current_spectogram('Audio_Longo.wav')

    # alter_spectogram('Audio_Longo.wav', 'output2.wav', [], )