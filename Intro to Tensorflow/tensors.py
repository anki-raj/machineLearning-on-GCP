import tensorflow as tf
#Making n-dimensional tensors
x1 = tf.constant([[2,3,4],
				[5,6,7]])
x2 = tf.stack([x1,x1])
x3 = tf.stack([x2,x2,x2,x2])
print(x3)
#Slicing of tensors
y = x1[:,1]
with tf.Session() as sess:
	print(y.eval())

