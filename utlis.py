import time
from matplotlib import pyplot as plt
from scipy.io . wavfile import read as wavread

def log_the_string(comment):
    logFile = 'log.txt'
    logTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    with open(logFile, 'a')as lf:
        lf.write(logTime + '\t' + comment + '\n')
    return 0

def plot_wav(wavPath):
    sample_rate, audio_data = wavread(wavPath)
    plt.plot(audio_data)
    plt.show()
    return 0

def plot_function():
    x = list(range(10))
    y = [2 * x_item * x_item + 5 for x_item in x]
    plt.plot(x, y, 'r*')
    plt.show()
    return 0

if __name__ == '__main__':
    log_the_string('hello')

if __name__ == '__main__':
    log_the_string('hello')