# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:39:48 2021

@author: 資源教室
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 22:01:54 2021

@author: 資源教室
"""

import tensorflow.compat.v1 as tf #降階為1.0版本
import numpy as np
tf.disable_v2_behavior()
#matrix 
                                     # m1   m2
matrix1=tf.constant([[3,3],[2,2]])   # 3 3  2 
matrix2=tf.constant([[2],[2]])#        2 2  2

product=tf.matmul(matrix1,matrix2)
#counter
counter=tf.Variable(0,name='counter')
one=tf.constant(1)
new_value=tf.add(counter,one)
update=tf.assign(counter,new_value)

#另類變數呼叫
input1=tf.placeholder(tf.float32)
input2=tf.placeholder(tf.float32)
result2=tf.add(input1,input2)

init=tf.initialize_all_variables()#這步很重要有變數(var)就要init

with tf.Session() as sess:
    result=sess.run(product)
    sess.run(init)
    print(sess.run(result2,feed_dict={input1:[7.],input2:[2.]}))#run時再給值
    print(result)
    for _ in range(3):
        sess.run(update)#可以想成函式呼叫
        print(sess.run(counter))
       
        
    