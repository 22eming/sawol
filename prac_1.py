import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def identity_function(x):
    return x

def init_network():
    network = {}
    network['W1'] = np.array([[.1, .3, .5], [.2, .4, .6]])
    network['B1'] = np.array([.1, .2, .3])
    network['W2'] = np.array([[.1,.4], [.2,.5],[.3,.6]])
    network['B2'] = np.array([.1,.2])
    network['W3'] = np.array([[.1,.3],[.2,.4]])
    network['B3'] = np.array([.1,.2])

    return network

def forword(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['B1'], network['B2'], network['B3']

    a1 = x@W1 + b1
    z1 = sigmoid(a1)
    a2 = z1@W2 + b2
    z2 = sigmoid(a2)
    a3 = z2@W3 + b3
    y = identity_function(a3)

    return y

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

network = init_network()
x = np.array([1., .5])
y = forword(network, x)
print(y)