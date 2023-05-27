import subprocess

import pandas as pd
import numpy as np
import torch
def readData(path):
    f = open(path)
    temp = []
    for line in f:
        temp.append(line.strip())

    model =[]
    for item in temp:
        t = []
        t1 = item.split(",")
        for i in t1:
            if i == "":
                continue
            t.append(float(i))
        model.append(t)
    f.close()
    return model

def cos_sim(vector_a, vector_b):
    norm1 = np.linalg.norm(vector_a,axis=-1,keepdims=True)
    norm2 = np.linalg.norm(vector_b, axis=-1, keepdims=True)
    arr1_norm = vector_a / norm1
    arr2_norm = vector_b / norm2
    cos = np.dot(arr1_norm, arr2_norm.T)
    return cos

if __name__ == '__main__':
    model = readData('model.txt')
    model = np.array(model)
    test = readData('test.txt')
    test = np.array(test)
    res = cos_sim(model,test)
    # 提取出矩阵中的非nan
    res = res[np.logical_not(np.isnan(res))]
    score = round(float(np.mean(res)),4) * 100
    with open('model.txt', 'w') as f:
        f.truncate(0)
    with open('test.txt', 'w') as f:
        f.truncate(0)
    print(score)

