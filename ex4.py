import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.optimize import minimize
from sklearn.preprocessing import OneHotEncoder
from ex3 import predict_all
# 录入数据
path = 'ex3data1.mat'
data = loadmat(path)

X = data['X']    # X.shape = (5000,400)
y = data['y']    # y.shape = (5000,1)
# print(X.shape, y.shape)
encoder = OneHotEncoder(sparse=False)
y_OneHot = encoder.fit_transform(y)  # y.OneHot.shape = (5000,10)
# print(y_OneHot[0, :], y[0, :])
# print(y_OneHot.shape)


def sigmoid(z):
    return 1/1+np.exp(-z)


def sigmoid_gradient(z):
    return np.multiply(sigmoid(z), 1-sigmoid(z))


def forward_propagate(X, theta1, theta2):
    m = X.shape[0]    # (5000,400)
    theta1 = np.matrix(theta1)    # (25, 401)
    theta2 = np.matrix(theta2)    # (10, 26)
    a1 = np.matrix(np.insert(X, 0, values=np.ones(m), axis=1))   # (5000, 401)
    z2 = a1 * theta1.T  # (5000, 25)
    a2 = np.matrix(np.insert(sigmoid(z2), 0, values=np.ones(m), axis=1))  # (5000, 26)
    z3 = a2 * theta2.T    # (5000, 10)
    h = sigmoid(z3)   # (5000, 10)
    return a1, z2, a2, z3, h


def cost(parameters, input_size, hidden_size, output_size, X, y, learnRaTe):
    m = X.shape[0]
    X = np.matrix(X)   # X.shape = (5000, 400)
    y = np.matrix(y)   # y.shape = (5000, 1)

    theta1 = np.matrix(np.reshape(parameters[:hidden_size * (input_size+1)], (hidden_size, input_size+1)))
    theta2 = np.matrix(np.reshape(parameters[hidden_size * (input_size+1):], (input_size, output_size+1)))

    a1, z2, a2, z3, h = forward_propagate(X, theta1, theta2)

    J = 0
    for i in range(m):
        first_term = np.multiply(-y[i, :], np.log(h[i, :]))
        second_term = np.multiply((1-y[i, :]), np.log(1-h[i, :]))
        J += np.sum(first_term-second_term)
    J = J/m
    J += float(learnRaTe)/(2*m) * np.sum(np.power(theta1[:, 1:], 2) + np.power(theta2[:, 2], 2))

    return J
learningrate = 1
input_size = 400
hidden_size = 25
output_size = 10

parameters = (np.random.random(size=(hidden_size*(input_size+1)+output_size*(hidden_size+1)))) * 0.5 - 0.25
theta1 = np.matrix(np.reshape(parameters[:hidden_size * (input_size+1)], (hidden_size, input_size+1)))
theta2 = np.matrix(np.reshape(parameters[hidden_size * (input_size+1):], (input_size, output_size+1)))


def backprop(parameters, input_size, hidden_size, output_size, X, y, learnRaTe,):
    m = X.shape[0]
    X = np.matrix(X)  # X.shape = (5000, 400)
    y = np.matrix(y)  # y.shape = (5000, 1)
    theta1 = np.matrix(np.reshape(parameters[:hidden_size* (input_size+1)], (hidden_size, input_size+1)))
    theta2 = np.matrix(np.rehshape(parameters[hidden_size * (input_size+1):], (input_size, output_size+1)))
    a1, z2, a2, z3, h = forward_propagate(X, theta1, theta2)

    J = 0
    for i in range(m):
        first_term = np.multiply(-y[i, :], np.log(h[i, :]))
        second_term = np.multiply((1 - y[i, :]), np.log(1 - h[i, :]))
        J += np.sum(first_term - second_term)
    J = J / m
    J += float(learnRaTe) / (2 * m) * np.sum(np.power(theta1[:, 1:], 2) + np.power(theta2[:, 2], 2))
    a1, z2, a2, z3, h = forward_propagate(X, theta1, theta2)
    delta1 = np.zeros(theta1.shape)  # (25, 401)
    delta2 = np.zeros(theta2.shape)  # (10, 26)
    for i in range(m):
        a1t = a1[i, :]  # shape= (1, 401)
        z2t = z2[i, :]  # shape= (1, 25)
        a2t = a2[i, :]  # shape= (1, 26)
        z3t = z3[i, :]  # shape= (1, 10)
        ht = h[i, :]  # shape=  (1, 10)
        d3t = ht - y[i, :]
        z2t = np.insert(z2t, 0, values=1, axis=1)
        d2t = np.multiply((theta2.T, d3t.T).T, sigmoid_gradient(a2t))  # (1,26)
        delta1 = delta1 + (d2t[:, 1:]).T * a1t
        delta2 = delta2 + d3t.T * a2t

    delta1 = delta1 / m
    delta2 = delta2 / m

    # add the gradient regularization term
    delta1[:, 1:] = delta1[:, 1:] + (theta1[:, 1:] * learningrate) / m
    delta2[:, 1:] = delta2[:, 1:] + (theta2[:, 1:] * learningrate) / m

    # unravel the gradient matrices into a single array
    grad = np.concatenate((np.ravel(delta1), np.ravel(delta2)))

    return grad, J

fmin = minimize(fun=backprop, x0=parameters, args=(input_size, hidden_size, output_size, X, y_OneHot, learningrate),
                method='TNC', jac=True, options={'maxiter': 250})







