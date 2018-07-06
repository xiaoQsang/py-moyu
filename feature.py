import os
from time import time

import h5py
import numpy
from python_speech_features import mfcc
from scipy.io.wavfile import read as wavread
from python_speech_features import delta
from python_speech_features import logfbank

from utils import log_the_string


def get_mfcc(wavFilePath):
    log_the_string('now is processing %s...' % wavFilePath)
    sampleRate, audioData = wavread(wavFilePath)
    audioData = numpy.array([item / 2 ** 15 for item in audioData])
    mfcc_feat = mfcc(audioData, sampleRate)
    return mfcc_feat


def batch_get_mfcc(data_dir='Data'):
    dataX = []
    labelY = []
    for root, dirs, names in os.walk(data_dir):
        for name in names:
            wav_path = os.path.join(root, name)
            if r'\music' in wav_path:
                label = 0
            elif r'\speech' in wav_path:
                label = 1
            feat = get_mfcc(wav_path)
            dataX.append(feat)
            label_num = feat.shape[0]
            labelY.extend([label] * label_num)
    dataX = numpy.concatenate(dataX)
    return dataX, labelY


def save_dataset_2_h5(dataX, labelY, dataset_path='dataset.h5'):
    log_the_string('now is saving to h5')
    dataset_file = h5py.File(dataset_path, 'w')
    dataset_file.create_dataset('dataX', data=dataX)
    dataset_file.create_dataset('labelY', data=labelY)
    dataset_file.close()
    return 0


def load_dataset_from_h5(dataset_path='dataset.h5'):
    log_the_string('now is loading from h5')
    dataset_file = h5py.File(dataset_path, 'r')
    dataX = dataset_file['dataX'][:]
    labelY = dataset_file['labelY'][:]
    return dataX, labelY


if __name__ == '__main__':
    start = time()
    dataX, labelY = batch_get_mfcc()
    save_dataset_2_h5(dataX, labelY)
    dataX, labelY = load_dataset_from_h5()
    end = time()
    log_the_string('it takes %.2f s' % (end - start))