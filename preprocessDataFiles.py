import os
from pydub import AudioSegment

def convert_wavFile(wavPath, desWavPath):
    sound=AudioSegment.from_wav(wavPath)
    sound=sound.set_channels(1)
    sound=sound.set_frame_rate(16000)
    sound=sound.set_set_sample_width(2)
    out_dir= os.path.dirname(desWavPath)
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    sound.export(desWavPath,'wav')
    return 0
    sound.export(desWavPath,'wav')
def transform_fomat_2_mono_16k():
    dataDir= 'music_speech'
    for root, dirs, names in os.walk(dataDir):
        for name in names:
            file_path=os.path.join(root,name)
            if 'music_wav' in file_path and '.wav' in file_path:
                src=file_path
                des='Data/music/'+os.path.basename(file_path)

            elif 'speech_wav' in file_path and '.wav' in file_path:
                src = file_path
                des = 'Data/music/' + os.path.basename(file_path)
            else:
                pass
    return 0

transform_fomat_2_mono_16k()