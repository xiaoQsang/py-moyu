import os
from pydub import AudioSegment
from time import time
from loglt import log_the_string

def convert_wavFile(wavPath, desWavPath):
    log_the_string(wavPath)
    sound=AudioSegment.from_wav(wavPath)
    sound=sound.set_channels(1)
    sound=sound.set_frame_rate(16000)
    sound=sound.set_sample_width(2)
    out_dir= os.path.dirname(desWavPath)
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    sound.export(desWavPath,'wav')
    return 0

def transform_fomat_2_mono_16k(dataDir='music_speech'):
    dataDir= 'music_speech'
    for root, dirs, names in os.walk(dataDir):
        for name in names:
            file_path=os.path.join(root, name)
            if 'music_wav' in file_path and '.wav' in file_path:
                src=file_path
                des='Data/music/' + os.path.basename(file_path)
                convert_wavFile(src, des)
            elif 'speech_wav' in file_path and '.wav' in file_path:
                src = file_path
                des = 'Data/speech/' + os.path.basename(file_path)
                convert_wavFile(src, des)
            else:
                pass
    return 0
if __name__ == '__main__':
    start = time()
    end = time()
    all_take_str = 'it takes %.2f %'(end - start)
    print(all_take_str)
    log_the_string(all_take_str)