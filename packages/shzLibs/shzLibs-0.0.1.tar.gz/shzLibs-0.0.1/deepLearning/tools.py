from numpy import ndarray

def calc_neurons_1(X_train: ndarray):
    neurons = round((X_train.shape[1] * 2/3) + 1)
    return neurons