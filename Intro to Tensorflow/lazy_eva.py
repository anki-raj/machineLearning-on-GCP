import tensorflow as tf
a = tf.constant([5,3,4])
b = tf.constant([2,3,1])
c = tf.add(a, b)
print("just built it, does not evaluate --> ",c)
with tf.Session() as sess:
	result = sess.run(c)
	print("After evaluation --> ", result)