#coding=utf-8
import tensorflow as tf
m1 = tf.constant([[3,3]])
m2 = tf.constant([[2],[3]])
#创建一个矩阵乘法
product = tf.matmul(m1,m2)

#定义会话
#定义图
with tf.Session() as sess:
    result=sess.run(product)
    print(result)
