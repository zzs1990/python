# -*- coding: utf-8 -*-
# 快速构建一个识别手写数字图片的神经网络
# 人工智能的本质是分析海量数据，从数据中抽取出潜在的底层特征

# mnist对应网络训练需要的数据集
from keras.datasets import mnist

# 将手写数字图片数据集加载到程序中
# train代表训练数据，test用于检验网络训练结果
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images.shape)



