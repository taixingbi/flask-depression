
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import glob
from keras.models import load_model

cnn_model = load_model('../depression.h5')

# cnn_model = load_model('/home/ubuntu/ml-kaden-data-analysis-test2/model/depression.h5')

class cnnDepression:
    def __init__(self):
        print("cnn init...")
        self.THRESHOLD_ROC= 0.64

        self.sample= 125
        self.Nfeatures= 513
        # self.cnn_model = cnn_model
        self.cnn_model = load_model('../depression.h5')

    def threshold(self):
        print("threshold...")        
        return self.THRESHOLD_ROC

    def predict(self, X):
        print("predict...")
        y_probs = self.cnn_model.predict(X)
        y_probs= [ round(float(_[1]),4) for _ in y_probs]
        return y_probs

    def data_propcessing(self, spectrogram):
        print("data_propcessing...")
        spectrogram = spectrogram / np.linalg.norm(spectrogram)
        print(spectrogram.shape) # (513, 821)
        spectrogram= spectrogram.transpose()
        spectrogram= spectrogram[: -int(spectrogram.shape[0]%125) ]
        print(spectrogram.shape) 
        NSamples= int(spectrogram.shape[0]/125)
        X= spectrogram.reshape( NSamples, self.sample, self.Nfeatures, 1 )    # (25, 125, 513, 1)
        print(X.shape)
        return X

    def pipeline(self, filename):
        print("pipeline...")
        Fs, x = wavfile.read(filename)
        spectrogram, freqs, bins, im = plt.specgram(x, NFFT=1024, Fs=Fs) 
        X= self.data_propcessing(spectrogram)
        depress= self.predict(X)
        print(depress)
        return depress
    
if __name__ == '__main__':

    filename= 'data/163_1613840232_1m_noSilence.wav'
    cnnDepression().pipeline(filename)

    print("done")
