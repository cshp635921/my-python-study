import tensorflow as tf
import numpy as np
predictions = tf.constant([1, 2])
prediction_logits = tf.constant([[1.0, 2.0, 3.0], [0, -0.5, 1]])
loss = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=predictions, logits=prediction_logits)

def mysoftmax(sess, predictions, logits):
    q = []
    for i in range(predictions.shape[0]):
        loss = logits[i][predictions[i]]/tf.reduce_sum(prediction_logits[i])
        q.append(loss)
    print(sess.run(q))
with tf.Session() as sess:
    print(sess.run(loss))
    mysoftmax(sess, predictions, prediction_logits)



