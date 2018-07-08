import os
from time import time

import joblib
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import NearestCentroid
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC

from feature import load_dataset_from_h5
from utils import log_the_string


def use_decision_classify_tree(dataX, lableY):
    modelPath = 'dt.model'
    if not os.path.isfile(modelPath):
        log_the_string('use decision tree and train it save it...')
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(dataX, lableY)
        joblib.dump(clf, modelPath)
    else:
        clf = joblib.load(modelPath)
    return clf


def use_SVM(dataX, lableY):
    modelPath = 'svm.model'
    if not os.path.isfile(modelPath):
        log_the_string('use SVM and train it save it...')
        clf = LinearSVC()
        clf = clf.fit(dataX, lableY)
        joblib.dump(clf, modelPath)
    else:
        clf = joblib.load(modelPath)
    return clf


def use_SGD(dataX, lableY):
    modelPath = 'sgd.model'
    if not os.path.isfile(modelPath):
        log_the_string('use SGD and train it save it...')
        clf = SGDClassifier(loss="hinge", penalty="l2")
        clf = clf.fit(dataX, lableY)
        joblib.dump(clf, modelPath)
    else:
        clf = joblib.load(modelPath)
    return clf


def use_nearesrNeighbors(dataX, lableY):
    modelPath = 'nn.model'
    if not os.path.isfile(modelPath):
        log_the_string('use nearesrNeighbors and train it save it...')
        clf = NearestCentroid()
        clf = clf.fit(dataX, lableY)
        joblib.dump(clf, modelPath)
    else:
        clf = joblib.load(modelPath)
    return clf


def use_gaussianNB(dataX, lableY):
    modelPath = 'gnb.model'
    if not os.path.isfile(modelPath):
        log_the_string('use gaussianNB and train it save it...')
        clf = GaussianNB()
        clf = clf.fit(dataX, lableY)
        joblib.dump(clf, modelPath)
    else:
        clf = joblib.load(modelPath)
    return clf


def use_randomForest(dataX, lableY):
    modelPath = 'randomForest.model'
    if not os.path.isfile(modelPath):
        log_the_string('use randomForest and train it save it...')
        clf = RandomForestClassifier(n_estimators=10, max_depth=None,
                                     min_samples_split=2, random_state=0)
        clf = clf.fit(dataX, lableY)
        joblib.dump(clf, modelPath)
    else:
        clf = joblib.load(modelPath)
    return clf


def use_MLP(dataX, lableY):
    modelPath = 'mlp.model'
    if not os.path.isfile(modelPath):
        log_the_string('use MLP and train it save it...')
        clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                            hidden_layer_sizes=(5, 2), random_state=1)
        clf = clf.fit(dataX, lableY)
        joblib.dump(clf, modelPath)
    else:
        clf = joblib.load(modelPath)
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
    dataX, labelY = load_dataset_from_h5()  # dataX, labelY = batch_get_mfcc()
    print('load dataX shape:', dataX.shape)
    X_train, X_test, y_train, y_test = train_test_split(dataX, labelY, test_size=0.2)
    dctModel = use_decision_classify_tree(X_train, y_train)
    svmModel = use_SVM(X_train, y_train)
    sgdModel = use_SGD(X_train, y_train)
    nearModle = use_nearesrNeighbors(X_train, y_train)
    gaussianNB_Model = use_gaussianNB(X_train, y_train)
    randomForestModel = use_randomForest(X_train, y_train)
    mlpModel = use_MLP(X_train, y_train)

    dctPredict = dctModel.predict(X_test)
    svmPredict = svmModel.predict(X_test)
    sgdPredict = sgdModel.predict(X_test)
    nearPredict = nearModle.predict(X_test)
    gaussianNB_Predict = gaussianNB_Model.predict(X_test)
    randomForestPredict = randomForestModel.predict(X_test)
    mlpPredict = mlpModel.predict(X_test)

    final_vote_res = dctPredict + svmPredict + sgdPredict + nearPredict + gaussianNB_Predict + randomForestPredict + mlpPredict

    final_vote_res_0_1 = [1 if item > 3 else 0 for item in final_vote_res]

    get_evaluation_report(y_test, dctPredict)
    get_evaluation_report(y_test, svmPredict)
    get_evaluation_report(y_test,final_vote_res_0_1)
    end = time()
    log_the_string('it takes %.2f s' % (end - start))