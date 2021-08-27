#from _typeshed import Self
from typing import Union, ValuesView
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.shape_base import split
from sklearn.tree import DecisionTreeClassifier, plot_tree

from tools import load_iris, split_train_test


def prior(targets: np.ndarray, classes: list) -> np.ndarray:
    bin = np.zeros(len(classes))
    for i in classes:
        for j in targets:
            if i == j:
                bin[i] += 1/len(targets)
    return bin


def split_data(
    features: np.ndarray,
    targets: np.ndarray,
    split_feature_index: int,
    theta: float
) -> Union[tuple, tuple]:

    features_1 = []
    targets_1 = []

    features_2 = []
    targets_2 = []

    for i in range(len(features)):
        if features[i][split_feature_index] < theta:
            features_1.append(features[i])
            targets_1.append(targets[i])
        else:
            features_2.append(features[i])
            targets_2.append(targets[i])

    return (np.array(features_1), np.array(targets_1)), (np.array(features_2), np.array(targets_2))


def gini_impurity(targets: np.ndarray, classes: list) -> float:
    dogs = prior(targets, classes)
    return 0.5*(1-np.sum(np.power(dogs, 2)))


def weighted_impurity(
    t1: np.ndarray,
    t2: np.ndarray,
    classes: list
) -> float:
    g1 = gini_impurity(t1, classes)
    g2 = gini_impurity(t2, classes)
    n = t1.shape[0] + t2.shape[0]
    N1 = len(t1)
    N2 = len(t2)

    return ((N1*g1)+(N2*g2))/n


def total_gini_impurity(
    features: np.ndarray,
    targets: np.ndarray,
    classes: list,
    split_feature_index: int,
    theta: float
) -> float:
    (f_1, t_1), (f_2, t_2) = split_data(
        features, targets, split_feature_index, theta)
    return weighted_impurity(t_1, t_2, classes)


def brute_best_split(
    features: np.ndarray,
    targets: np.ndarray,
    classes: list,
    num_tries: int
) -> Union[float, int, float]:
    best_gini, best_dim, best_theta = float("inf"), None, None
    # iterate feature dimensions
    for i in range(features.shape[1]):
        # create the thresholds
        thetas = np.linspace(np.min(features[:, i]), np.max(
            features[:, i]), num_tries+2)[1:-1]

        # iterate thresholds
        for theta in thetas:
            total_gini = total_gini_impurity(
                features, targets, classes, i, theta)
            if total_gini < best_gini:
                best_gini = total_gini
                best_dim = i
                best_theta = theta

    return best_gini, best_dim, best_theta


class IrisTreeTrainer:
    def __init__(
        self,
        features: np.ndarray,
        targets: np.ndarray,
        classes: list = [0, 1, 2],
        train_ratio: float = 0.8
    ):
        (self.train_features, self.train_targets),\
            (self.test_features, self.test_targets) =\
            split_train_test(features, targets, train_ratio)

        self.classes = classes
        self.tree = DecisionTreeClassifier()

    def train(self):
        return self.tree.fit(self.train_features, self.train_targets)

    def accuracy(self):
        predict = self.tree.predict(self.test_features)
        return accuracy_score(self.test_targets, predict)

    def plot(self):
        plot_tree(self.tree)
        fig1 = plt.gcf()
        plt.show()
        fig1.savefig("2_3_1.png")

    def plot_progress(self):
        s = []
        n = []
        for i in range(1, len(self.train_features-1)):
            self.tree.fit(self.train_features[:i], self.train_targets[:i])
            y_prediction = self.tree.predict(self.test_features)
            score = accuracy_score(self.test_targets, y_prediction)
            s.append(score)
            n.append(i)
        fig2 = plt.gcf()
        plt.plot(n, s)
        plt.ylabel("Accuracy")
        plt.xlabel("Number of samples")
        plt.show()
        fig2.savefig("bonus_1.png")

    def guess(self):
        pred = self.tree.predict(self.test_features)
        return pred

    def confusion_matrix(self):
        n = len(self.classes)
        M = np.zeros((n, n))

        guess = self.guess()
        for i in range(len(self.test_targets)):
            j = self.test_targets[i]
            k = guess[i]
            M[j][k] += 1
        return M
