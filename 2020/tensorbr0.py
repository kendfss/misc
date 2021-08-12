# activate tensorflow
# python (activating python shell)
from m3ta import show, pop
# import tensorflow as tf
# import tensorflow.compat.v1 as tf
# hello = tf.constant('Hello, Tensorflow!')
# sess = tf.Session()
# print(sess.run(hello))
import tensorflow as tf # Assuming TF 2.0 is installed
a = tf.constant([[1, 2],[3, 4]])
b = tf.matmul(a, a)
print(b)
# tf.Tensor( [[ 7 10] [15 22]], shape=(2, 2), dtype=int32)
print(type(b.numpy()))
# <class 'numpy.ndarray'>
