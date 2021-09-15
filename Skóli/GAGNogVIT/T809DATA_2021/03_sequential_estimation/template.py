from numpy.core.fromnumeric import mean
from numpy.core.numeric import identity
from tools import scatter_3d_data, bar_per_axis

import matplotlib.pyplot as plt
import numpy as np


def gen_data(
    n: int,
    k: int,
    mean: np.ndarray,
    var: float
) -> np.ndarray:
    I_k = np.identity(k)
    cov = I_k * np.power(var, 2)
    gen = np.random.multivariate_normal(mean, cov, n)
    return gen


def scatter_3d_data(data: np.ndarray):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:, 0], data[:, 1], data[:, 2])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


def bar_per_axis(data: np.ndarray):
    for i in range(data.shape[1]):
        plt.subplot(1, data.shape[1], i+1)
        plt.hist(data[:, i], 100)
        plt.title(f'Dimension {i+1}')
    plt.show()


def update_sequence_mean(
    mu: np.ndarray,
    x: np.ndarray,
    n: int
) -> np.ndarray:
    update = mu + (1/n) * (x-mu)
    return update


def _plot_sequence_estimate():
    data = gen_data(100, 3, [0, 0, 0], 1)
    estim = [np.array([0, 0, 0])]
    for i in range(data.shape[0]):
        estim.append(update_sequence_mean(estim[i], data[i], i+1))

    plt.plot([e[0] for e in estim], label='First dimension')
    plt.plot([e[1] for e in estim], label='Second dimension')
    plt.plot([e[2] for e in estim], label='Third dimension')
    plt.legend(loc='upper center')
    plt.xlabel('n')
    plt.ylabel('Mean')
    plt.savefig('1_5_1.png')
    plt.show()


def _square_error(y, y_hat):
    return np.mean(np.power((y-y_hat), 2), 0)


def _plot_mean_square_error():
    data = gen_data(100, 3, np.array([0, 0, 0]), 1)
    estim = [np.array([0, 0, 0])]
    err_arr = []
    for i in range(data.shape[0]):
        estim.append(update_sequence_mean(estim[i], data[i], i+1))
        err_arr.append(_square_error([0, 0, 0], estim[i+1]))
    plt.plot(range(data.shape[0]), err_arr)
    plt.xlabel('n')
    plt.ylabel('Squared error')
    plt.savefig('1_6_1.png')
    plt.show()


# Naive solution to the independent question.

def gen_changing_data(
    n: int,
    k: int,
    start_mean: np.ndarray,
    end_mean: np.ndarray,
    var: float
) -> np.ndarray:
    # remove this if you don't go for the independent section
    #start_mean = [0,1,-1]
    #end_mean = [1,-1,0]
    I_k = np.identity(k)
    cov = I_k * np.power(var, 2)
    data = []
    mean = start_mean
    difference = np.divide(end_mean-start_mean, n)
    for i in range(n):
        datagen = np.random.multivariate_normal(mean, cov)
        data.append(datagen)
        mean = mean+difference
    return np.array(data)


def _plot_changing_sequence_estimate():
    # remove this if you don't go for the independent section
    data = gen_changing_data(500, 3, np.array(
        [0, 1, -1]), np.array([1, -1, 0]), 1)
    esti = [np.array([0, 1, -1])]
    for i in range(data.shape[0]):

        esti.append(update_sequence_mean(esti[i], data[i], i+1))

    plt.plot([e[0] for e in esti], label='First dimension')
    plt.plot([e[1] for e in esti], label='Second dimension')
    plt.plot([e[2] for e in esti], label='Third dimension')
    plt.legend(loc='upper center')
    plt.xlabel('n')
    plt.ylabel('Mean')
    plt.savefig('bonus_1.png')
    plt.show()


def _bonus_2():
    data = gen_changing_data(500, 3, np.array(
        [0, 1, -1]), np.array([1, -1, 0]), 1)
    estim = [np.array([0, 1, -1])]
    err_arr = []
    for i in range(data.shape[0]):
        estim.append(update_sequence_mean(estim[i], data[i], i+1))
        err_arr.append(_square_error([0, 0, 0], estim[i+1]))
    plt.plot(range(data.shape[0]), err_arr)
    plt.xlabel('n')
    plt.ylabel('Mean squared error')
    plt.savefig('bonus_2.png')
    plt.show()


def main():
    #print(gen_data(2, 3, np.array([0,1,-1]), 1.3))
    #print(update_sequence_mean(3, np.array([0,1,-1]),1.3))
    # _plot_sequence_estimate()
    #data = gen_data(300,3,[0,0,0],1)
    # scatter_3d_data(data)
    # bar_per_axis(data)
    _plot_sequence_estimate()
    _plot_mean_square_error()
    _plot_changing_sequence_estimate()
    _bonus_2()


main()
