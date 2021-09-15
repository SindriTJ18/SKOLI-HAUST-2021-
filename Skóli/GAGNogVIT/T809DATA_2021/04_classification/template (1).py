from pandas.core import frame
from tools import load_iris, split_train_test
from sklearn.metrics import accuracy_score, balanced_accuracy_score

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal
import pandas as pd


def mean_of_class(
    features: np.ndarray,
    targets: np.ndarray,
    selected_class: int
) -> np.ndarray:
    out_arr = []
    frame = pd.DataFrame(features)
    frame[4] = targets
    temp = frame[frame[4] == selected_class]
    for i in range(temp.shape[1]-1):
        out_arr.append(temp[i].mean())
    return np.array(out_arr)


def covar_of_class(
    features: np.ndarray,
    targets: np.ndarray,
    selected_class: int
) -> np.ndarray:
    out_arr = np.array
    frame = pd.DataFrame(features)
    frame[4] = targets
    temp = frame[frame[4] == selected_class]
    temp = temp.drop(4, axis=1)

    return out_arr(temp.cov())


def likelihood_of_class(
    feature: np.ndarray,
    class_mean: np.ndarray,
    class_covar: np.ndarray
) -> float:
    temp = multivariate_normal(class_mean, class_covar)
    return temp.pdf(feature)


def maximum_likelihood(
    train_features: np.ndarray,
    train_targets: np.ndarray,
    test_features: np.ndarray,
    classes: list
) -> np.ndarray:
    means, covs = [], []
    for class_label in classes:
        means.append(mean_of_class(train_features, train_targets, class_label))
        covs.append(covar_of_class(train_features, train_targets, class_label))
    likelihoods = []
    for i in range(test_features.shape[0]):
        temp = []
        for j in range(len(classes)):
            temp.append(likelihood_of_class(
                test_features[i], means[j], covs[j]))
        likelihoods.append(temp)

    return np.array(likelihoods)


def predict(likelihoods: np.ndarray):
    return_arr = np.zeros(likelihoods.shape[0])
    for i in range(likelihoods.shape[0]):
        return_arr[i] = np.argmax(likelihoods[i])

    return np.array(return_arr)


def maximum_aposteriori(
    train_features: np.ndarray,
    train_targets: np.ndarray,
    test_features: np.ndarray,
    classes: list
) -> np.ndarray:
    df_train = pd.DataFrame(train_features)
    df_train[4] = train_targets
    a_dict = {}
    for i in classes:
        a_dict[i] = df_train[df_train[4] == i].shape[0] / df_train.shape[0]
    likelihood = pd.DataFrame(maximum_likelihood(
        train_features, train_targets, test_features, classes))
    for i in a_dict:
        likelihood[i] = likelihood[i] * a_dict[i]
    likelihood = np.array(likelihood)
    return likelihood


def confusion_matrix(classes, pred, test_targets):
    confusion_m = [[0]*len(classes) for x in range(len(classes))]
    for p in range(len(test_targets)):
        confusion_m[int(pred[p])][test_targets[p]] += 1
    return np.array(confusion_m)


def diffBetweenMLEAndMAP(train_features, train_targets, test_features, test_targets, classes):
    arr1 = maximum_likelihood(
        train_features, train_targets, test_features, classes)
    arr2 = maximum_aposteriori(
        train_features, train_targets, test_features, classes)
    predictionMLE = predict(arr1)
    predictionMAP = predict(arr2)
    acc1 = accuracy_score(test_targets, predictionMLE)
    acc2 = accuracy_score(test_targets, predictionMAP)
    print("MLE")
    print(acc1)
    print(confusion_matrix(classes, predictionMLE, test_targets))

    print("MAP")
    print(acc2)
    print(confusion_matrix(classes, predictionMAP, test_targets))


def main():
    features, targets, classes = load_iris()
    (train_features, train_targets), (test_features, test_targets)\
        = split_train_test(features, targets, train_ratio=0.6)
    #print(mean_of_class(train_features, train_targets, 0))
    #print(covar_of_class(train_features, train_targets, 0))
    class_mean = mean_of_class(train_features, train_targets, 0)
    class_cov = covar_of_class(train_features, train_targets, 0)
    #print(likelihood_of_class(test_features[0, :], class_mean, class_cov))
    #likelihoods = maximum_likelihood(train_features, train_targets, test_features, classes)
    # print(predict(likelihoods))
    diffBetweenMLEAndMAP(train_features, train_targets,
                         test_features, test_targets, classes)


main()
