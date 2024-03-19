# -*- coding:UTF-8 -*-
from matplotlib.font_manager import FontProperties
from smote import preprocess_data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import argparse


def sigmoid(inX):
    # 设置一个阈值，超过这个值后就按饱和处理
    threshold = 20.0
    # 将输入限制在 [-threshold, threshold] 范围内
    inX_clipped = np.clip(inX, -threshold, threshold)
    # 计算 sigmoid 函数
    return 1.0 / (1.0 + np.exp(-inX_clipped))


def gradAscent(dataMatIn, classLabels):
    dataMatrix = np.mat(dataMatIn)
    labelMat = np.mat(classLabels).transpose()
    m, n = np.shape(dataMatrix)
    alpha = 0.01
    maxCycles = 500
    weights = np.ones((n, 1))
    weights_array = np.array([])
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)
        error = labelMat - h
        weights = weights + alpha * dataMatrix.transpose() * error
        weights_array = np.append(weights_array, weights)
    weights_array = weights_array.reshape(maxCycles, n)
    return weights.getA(), weights_array


def stocGradAscent1(dataMatrix, classLabels, batchSize=32, numIter=150, lambda_reg=0.01):
    m, n = np.shape(dataMatrix)
    weights = np.ones(n)   # 初始化权重，确保是n维的
    weights_array = np.array([])
    eps = 1e-6  # 避免除零错误的小值

    for j in range(numIter):
        dataIndex = list(range(m))
        np.random.shuffle(dataIndex)  # 随机打乱数据样本的顺序
        for k in range(0, m, batchSize):
            batchIndex = dataIndex[k:min(k + batchSize, m)]  # 选取一个小批量样本
            dataBatch = dataMatrix[batchIndex]
            labelBatch = classLabels[batchIndex]
            h = sigmoid(np.dot(dataBatch, weights))  # 确保点积得到正确的维度
            error = labelBatch - h  # 计算误差
            gradient = np.dot(error, dataBatch) / batchSize  # 计算梯度，取小批量样本的平均值
            alpha = 4 / (1.0 + j + k) + 0.01  # 降低alpha的大小，每次迭代减小
            weights = weights + alpha * (gradient - lambda_reg * weights) / (
                np.sqrt(np.sum(np.square(gradient))) + eps)  # 更新回归系数，添加L2正则化项和AdaGrad算法
            weights_array = np.append(
                weights_array, weights, axis=0)  # 添加回归系数到数组中
    weights_array = weights_array.reshape(
        numIter * ((m + batchSize - 1) // batchSize), n)  # 改变维度
    return weights, weights_array


def plotWeights(weights_array1, weights_array2):
    # 将fig画布分隔成3行2列,不共享x轴和y轴,fig画布的大小为(20,10)
    fig, axs = plt.subplots(nrows=3, ncols=2, sharex=False,
                            sharey=False, figsize=(20, 10))
    x1 = np.arange(0, len(weights_array1), 1)

    # 绘制w0与迭代次数的关系
    axs[0][0].plot(x1, weights_array1[:, 0])
    axs[0][0].set_title('改进的随机梯度上升算法：回归系数与迭代次数关系')
    axs[0][0].set_ylabel('W0')

    # 绘制w1与迭代次数的关系
    axs[1][0].plot(x1, weights_array1[:, 1])
    axs[1][0].set_ylabel('W1')

    # 绘制w2与迭代次数的关系
    axs[2][0].plot(x1, weights_array1[:, 2])
    axs[2][0].set_xlabel('迭代次数')
    axs[2][0].set_ylabel('W2')

    x2 = np.arange(0, len(weights_array2), 1)

    # 绘制w0与迭代次数的关系
    axs[0][1].plot(x2, weights_array2[:, 0])
    axs[0][1].set_title('梯度上升算法：回归系数与迭代次数关系')
    axs[0][1].set_ylabel('W0')

    # 绘制w1与迭代次数的关系
    axs[1][1].plot(x2, weights_array2[:, 1])
    axs[1][1].set_ylabel('W1')

    # 绘制w2与迭代次数的关系
    axs[2][1].plot(x2, weights_array2[:, 2])
    axs[2][1].set_xlabel('迭代次数')
    axs[2][1].set_ylabel('W2')

    plt.show()


def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0


def colicTest(x_train, y_train, x_test, y_test):
    trainWeights,_ = stocGradAscent1(np.array(x_train), y_train)  # 使用改进的随机上升梯度训练
    errorCount = 0
    numTestVec = len(x_test)
    
    for i in range(numTestVec):
        if int(classifyVector(np.array(x_test[i]), trainWeights)) != int(y_test[i]):
            errorCount += 1
    
    errorRate = (float(errorCount) / numTestVec) * 100  # 错误率计算
    print("测试集错误率为: %.2f%%" % errorRate)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='PyTorch churn prediction training')
    parser.add_argument('--file_path', type=str, default='C:/Users/xyj/Desktop/电商流失预测/毕设代码/input/internet_service_churn.csv',
                        help='training dataset ')
    args = parser.parse_args()

    x_train, y_train, x_test, y_test = preprocess_data(
        file_path=args.file_path, test_size=0.15, random_state=42)
    colicTest(x_train, y_train, x_test, y_test)
    
    # weights1, weights_array1 = stocGradAscent1(np.array(x), y)
    # weights2, weights_array2 = gradAscent(x, y)
    # plotWeights(weights_array1, weights_array2)
