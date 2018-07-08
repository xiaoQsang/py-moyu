# py-moyu
happy moyu everyday

1. use preprocessDataFiles.py convert the need files and to the standard format
2. use featureExtraction.py extract audio features such as mfcc from python_speech_feaures instead of the librosa which met many problem for installing all data of mfcc feature and lable are saved into dataset.h5
3. use classificationModels.py build sklearn model, here used the decision tree and SVM model, train it use train set and saved the trained model. then get dt.model and svm.model
4. use predictWavType.py predict a given wav file which is speech or music. 0 is music and 1 is speech.
5. use web.py and index.html in templates do a demo on web. user upload an auido file then get the answer of music or speech.