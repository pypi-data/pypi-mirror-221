import tensorflow as tf


def tfrecordWrite(writer, srcData, srcLabel):
    example = tf.train.Example(features=tf.train.Features(feature={
        "data": tf.train.Feature(bytes_list=tf.train.BytesList(value=[srcData.astype("float64").tobytes()])),
        "label": tf.train.Feature(bytes_list=tf.train.BytesList(value=[srcLabel.astype("int8").tobytes()])),
    }))
    writer.write(example.SerializeToString())


def tfrecordRead(example, size_window, size_feature, size_label):
    features = tf.io.parse_single_example(example, features={
        'data': tf.io.FixedLenFeature([], tf.string),
        'label': tf.io.FixedLenFeature([], tf.string)
    })
    data = tf.io.decode_raw(features["data"], tf.float64)
    data = tf.reshape(data, shape=(size_window, size_feature))
    label = tf.io.decode_raw(features["label"], tf.int8)
    label = tf.reshape(label, shape=(size_label,))
    
    return data, label

