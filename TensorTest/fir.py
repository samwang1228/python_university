# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 22:01:54 2021

@author: 資源教室
"""

import tensorflow.compat.v1 as tf #降階為1.0版本
import numpy as np
tf.disable_v2_behavior()
#產生100個 0~1之間的數
sess=tf.Session()
x_data=np.random.rand(100).astype(np.float32)#astype()修改資料型別
y_data=x_data*0.1+0.3
#print(y_data)
Weight=tf.Variable(tf.random_uniform([1],-1.0,1.0))

#[n]->shape of n n維
biases=tf.Variable(tf.zeros([1]))


y=Weight*x_data+biases #直線方程式AX+B

loss=tf.reduce_mean(tf.square(y-y_data))
optimizer=tf.train.GradientDescentOptimizer(0.5)
train=optimizer.minimize(loss)

init=tf.initialize_all_variables()
#print(sess.run(Weight))

#所有關於圖變量的賦值和計算都要通過tf.Session的run來進行
sess.run(init)

for step in range(201):
    sess.run(train)
    if step%20==0:
        print(step,sess.run(Weight),sess.run(biases))