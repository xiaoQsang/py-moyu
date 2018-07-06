import os
from time import time

import joblib
from sklearn import tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

from feature import load_dataset_from_h5
from utils import log_the_string


def use_decision_classify_tree(dataX, lableY):
    modelPath = 'dt.model'
    if not os.path.isfile(modelPath):
        log_the_string('use decision tree and train it save it...')
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(dataX, lableY)
        joblib.dump(clf, 'dt.model')
    else:
        clf = joblib.load(modelPath)
    return clf


def use_SVM(dataX, lableY):
    log_the_string('use SVM and train it save it...')
    clf = LinearSVC()
    clf = clf.fit(dataX, lableY)
    joblib.dump(clf, 'svm.model')
    return clf


def get_evaluation_report(groundTruth, predictResult):
    acc = accuracy_score(groundTruth, predictResult)
    pre = precision_score(groundTruth, predictResult)
    rec = recall_score(groundTruth, predictResult)
    f1 = f1_score(groundTruth, predictResult)
    log_the_string('acc:%.2f,pre:%.2f,rec:%.2f,f1:%.2f' % (acc, pre, rec, f1))
    return acc, pre, rec, f1


if __name__ == '__main__':
    start = time()
    dataX, labelY = load_dataset_from_h5()
    print('load dataX shape:', dataX.shape)
    X_train, X_test, y_train, y_test = train_test_split(dataX, labelY, test_size=0.2)
    dctModel = use_decision_classify_tree(X_train, y_train)
    svmModel = use_SVM(X_train, y_train)
    dctPredict = dctModel.predict(X_test)
    svmPredict = svmModel.predict(X_test)
    get_evaluation_report(y_test, dctPredict)
    get_evaluation_report(y_test, svmPredict)
    end = time()
    log_the_string('it takes %.2f s' % (end - start))