import numpy as np
import collections
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from numpy.lib.function_base import append
from tools import load_iris, split_train_test, plot_points


def remove_one(points: np.ndarray, i: int):
    return np.concatenate((points[0:i], points[i+1:]))


def euclidian_distance(x: np.ndarray, y: np.ndarray) -> float:
    dist = np.linalg.norm(x - y)
    return dist


def euclidian_distances(x: np.ndarray, points: np.ndarray) -> np.ndarray:
    dists = []
    for i in range(len(points)):
        dists.append(euclidian_distance(x, points[i]))
    return dists


def k_nearest(x: np.ndarray, points: np.ndarray, k: int):
    distances = euclidian_distances(x, points)
    order = np.argsort(distances)
    return order[:k]


def vote(targets, classes):
    TelVect = []
    for i in range(len(classes)):
        counter = 0
        for j in range(len(targets)):
            if targets[j] == classes[i]:
                counter += 1
        TelVect.append(counter)
    MaxVal = TelVect.index(max(TelVect))
    Common = classes[MaxVal]
    return Common


def knn(
    x: np.ndarray,
    points: np.ndarray,
    point_targets: np.ndarray,
    classes: list,
    k: int
) -> np.ndarray:
    nearest = k_nearest(x, points, k)
    # SKILAR INDEX Á "K" CLOSEST POINTS
    voting = vote(point_targets[nearest], classes)
    return voting


def knn_predict(
    points: np.ndarray,
    point_targets: np.ndarray,
    classes: list,
    k: int
) -> np.ndarray:
    arr = []
    for i in range(len(point_targets)):
        temp_pts = remove_one(points, i)
        temp_trg = remove_one(point_targets, i)
        arr.append(knn(points[i], temp_pts, temp_trg, classes, k))
    return np.array(arr)


def knn_accuracy(
    points: np.ndarray,
    point_targets: np.ndarray,
    classes: list,
    k: int
) -> float:
    pred = knn_predict(points, point_targets, classes, k)
    return accuracy_score(point_targets, pred)


def knn_confusion_matrix(
    points: np.ndarray,
    point_targets: np.ndarray,
    classes: list,
    k: int
) -> np.ndarray:
    n = len(classes)
    M = np.zeros((n, n))

    guess = knn_predict(points, point_targets, classes, k)
    for i in range(len(point_targets)):
        j = point_targets[i]
        k = guess[i]
        M[k][j] += 1
    return M


def best_k(
    points: np.ndarray,
    point_targets: np.ndarray,
    classes: list,
) -> int:
    accuracy = 0
    best_accuracy = 0
    for i in range(len(points)-1):
        accuracy = knn_accuracy(points, point_targets, classes, i)
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = i
    return best_k


def knn_plot_points(
    points: np.ndarray,
    point_targets: np.ndarray,
    classes: list,
    k: int
):
    colors = ['yellow', 'purple', 'blue']
    prediction = knn_predict(points, point_targets, classes, k)
    for i in range(points.shape[0]):
        [x, y] = points[i, :2]
        if point_targets[i] == prediction[i]:
            edgestring = 'green'
        else:
            edgestring = 'red'
        plt.scatter(x, y, c=colors[point_targets[i]], edgecolors=edgestring,
                    linewidths=2)
    plt.title('Yellow=0, Purple=1, Blue=2')
    fig1 = plt.gcf()
    plt.ylabel("Sepal width")
    plt.xlabel("Sepal length")
    plt.show()
    fig1.savefig("2_5_1.png")


def weighted_vote(
    targets: np.ndarray,
    distances: np.ndarray,
    classes: list
) -> int:
    '''
    Given a list of nearest targets, vote for the most
    popular
    '''
    # Remove if you don't go for independent section
    ...


def wknn(
    x: np.ndarray,
    points: np.ndarray,
    point_targets: np.ndarray,
    classes: list,
    k: int
) -> np.ndarray:
    '''
    Combine k_nearest and vote
    '''
    # Remove if you don't go for independent section
    ...


def wknn_predict(
    points: np.ndarray,
    point_targets: np.ndarray,
    classes: list,
    k: int
) -> np.ndarray:
    # Remove if you don't go for independent section
    ...


def compare_knns(
    points: np.ndarray,
    targets: np.ndarray,
    classes: list
):
    # Remove if you don't go for independent section
    ...


d, t, classes = load_iris()
knn_plot_points(d, t, classes, 3)
