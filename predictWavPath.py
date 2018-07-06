from feature import get_mfcc
import joblib
def use_clf_predict_wav_type(wavPath):
    mfcc_feat = get_mfcc(wavPath)
    clf = joblib.load('dt.model')
    res = clf.predict(mfcc_feat)
    res = list(res)
    if res.count(1) > res.count(0):
        type_wav = 'speech'
    else:
        type_wav = 'music'

    return type_wav

if __name__ == '__main__':
    use_clf_predict_wav_type(r'Data\speech\amal.wav')