import tensorflow as tf
from typing import List


def getWriter(file_path, is_zip: bool = True):
    if bool:
        return tf.io.TFRecordWriter(
            file_path,
            tf.io.TFRecordOptions(compression_type="GZIP")
        )
    else:
        return tf.io.TFRecordWriter(
            file_path,
        )

def tfrecordWrite(writer, srcData, srcLabel):
    example = tf.train.Example(features=tf.train.Features(feature={
        "data": tf.train.Feature(bytes_list=tf.train.BytesList(value=[srcData.astype("float32").tobytes()])),
        "label": tf.train.Feature(bytes_list=tf.train.BytesList(value=[srcLabel.astype("float32").tobytes()])),
    }))
    writer.write(example.SerializeToString())


def tfrecordRead(data_src, size_window, size_feature, size_label):
    features = tf.io.parse_single_example(data_src, features={
        'data': tf.io.FixedLenFeature([], tf.string),
        'label': tf.io.FixedLenFeature([], tf.string)
    })
    data = tf.io.decode_raw(features["data"], tf.float32)
    data = tf.reshape(data, shape=(size_window, size_feature))
    label = tf.io.decode_raw(features["label"], tf.float32)
    label = tf.reshape(label, shape=(size_label,))
    
    return data, label

def getTFRecordDataset(
        files: List[str], window: int, feature: int, label: int,
        suffle: int = None, batch: int = 1024, is_zip: bool = True
        ):
    if is_zip:
        tfds = tf.data.TFRecordDataset(files, "GZIP")
    else:
        tfds = tf.data.TFRecordDataset(files)
    tfds = tfds.map(lambda data_src: tfrecordRead(data_src, window, feature, label))
    if suffle is not None:
        tfds = tfds.shuffle(suffle)
    tfds = tfds.batch(batch)

    return tfds
