import numpy as np
import pandas as pd
import math
import pickle
import os

def minMaxNormalizer(data: list or np.ndarray):
  min_value = np.min(data)
  max_value = np.max(data)
  data_normalized = (data - min_value) / (max_value - min_value)
  return data_normalized

def trainTestSplitter(X, y, test_percent):
  total_data = len(X)
  train_percent = 1 - test_percent
  train_max_index = math.ceil(total_data * train_percent)
  X_train = X[:train_max_index]
  y_train = y[:train_max_index]
  X_test = X[train_max_index:]
  y_test = y[train_max_index:]

  return (np.array(X_train), np.array(X_test), np.array(y_train), np.array(y_test))

def basicTrainTestSplitter(data, test_percent):
  total_data = len(data)
  train_percent = 1 - test_percent
  train_max_index = math.ceil(total_data * train_percent)
  train = data[:train_max_index]
  test = data[train_max_index:]

  return (np.array(train), np.array(test))

def serializeSklearnModel(model, model_type, name, folder_path):
  model_folder = os.path.join(folder_path, model_type)

  if (not os.path.exists(model_folder)):
    os.mkdir(model_folder)
  
  file_path = os.path.join(model_folder, f'{name}.pkl')
  with open(file_path, 'wb') as file:
    pickle.dump(model, file)
    
# def plot_pred(datas: list, colors: list, dataLabels: list, linestyles=['dashed', 'solid'], axisLabels=[], title='', showLegend=False, savePath=''):
#     if (len(datas) != len(colors) != len(dataLabels) != len(linestyles) != len(axisLabels)):
#         raise ValueError("All arrays must be the same length")
    
#     fig, ax = pyplot.subplots()
    
#     for i in range(len(datas)):
#         data = datas[i]
#         dataLabel = dataLabels[i]
#         linestyle = linestyles[i]
#         color = colors[i]
        
#         ax.plot(data, label=dataLabel, color=color, linestyle=linestyle)
        
#     if (len(axisLabels) > 0):
#         ax.set_ylabel(axisLabels[0])
#         ax.set_xlabel(axisLabels[1])
    
#     if (showLegend):
#         ax.legend()

#     if (len(title) > 0):
#         ax.set_title(title)
        
#     if (len(savePath) > 0):
#         pyplot.savefig(savePath)

#     pyplot.show()
    
