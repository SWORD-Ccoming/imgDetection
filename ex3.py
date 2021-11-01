import numpy as np                                                         # 录入numpy数据库并将其命名为np
import matplotlib.pyplot as plt
from scipy.io import loadmat                                               # 录入loadmat函数用于读取数据集
from scipy.optimize import minimize

path = 'ex3data1.mat'
data = loadmat(path)
# print(data['X'].shape, data['y'].shape)


def sigmoid(z):                                                             # sigmoid函数
    return 1/(1+np.exp(-z))


def cost(theta, X, y, learnrate):                                           # 代价函数
    y = np.matrix(y)
    X = np.matrix(X)
    theta = np.matrix(theta)
    first = np.multiply(-y, np.log(sigmoid(X*theta.T)))
    second = np.multiply((1-y), np.log(1-sigmoid(X*theta.T)))
    reg = learnrate/(2*len(X))*np.sum(np.power(theta[:, 1:theta.shape[1]], 2))
    return np.sum(first-second)/len(X) + reg


def gradient(theta, X, y, learnrate):                                       # 梯度函数但只需要grad
    X = np.matrix(X)
    y = np.matrix(y)
    theta = np.matrix(theta)
    error = sigmoid(X*theta.T) - y      # (5000,0)的列向量, X为（5000，400）的矩阵，在matlab中一张图等于400个特征值的行向量
    grad = ((X.T*error)/len(X)).T + ((learnrate/len(X))*theta)   # theta.shape = （0, 400）   grad.shape = （0， 400）
    grad[0, 0] = np.sum(np.multiply(error, X[:, 0]))/len(X)
    return np.array(grad).ravel()


def one_vs_all(X, y, numbers_labels, learn_rate):
    rows = X.shape[0]
    parameters = X.shape[1]

    all_theta = np.zeros((numbers_labels, parameters+1))
    X = parameters.insert(X, 0, values=np.ones(rows), axis=1)

    for i in range(1, numbers_labels+1):
        theta = np.zeros(parameters+1)
        y_i = np.array([1 if label == i else 0 for label in y])
        y_i = np.reshape(y_i, (rows, 1))

        fmin = minimize(x0=theta, args=(X, y_i, learn_rate), jac=gradient, fun=cost, method='TNC')
        all_theta[i-1, :] = fmin.x
    return all_theta


def predict_all(X, all_theta):
    rows = X.shape[0]
    parameters = X.shape[1]
    X = np.insert(X, 0, values=np.ones(rows), axis=1)
    numbers_labels = all_theta.shape[0]
    all_theta = np.matrix(all_theta)
    X = np.matrix(X)
    h = sigmoid(X*all_theta.T)
    # X.shape= (5000, 401) all_theta.shape = (10, 401)
    # 即可推得 h.shape = （X*all_theta.T）.shape=(5000,10)
    h_argmax = np.argmax(h, axis=1)
    h_argmax = h_argmax + 1   # 因为矩阵是从零开始进行引索，故需要对其加1方便对其进行运算
    return h_argmax


all_theta = one_vs_all(data['X'], data['y'], 10, 1)
y_predict = predict_all(data['X'], all_theta)
correct = [1 if a == b else 0 for (a, b) in zip(y_predict, data['y'])]
accuracy = (sum(map(int, correct))) / float(len(correct))
print('accuracy={0}%'.format(accuracy*100))




