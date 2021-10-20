### tensorflow install

- create conda env, python 3.8
- install tensorflow-macos. Instructions from https://developer.apple.com/metal/tensorflow-plugin/

  `SYSTEM_VERSION_COMPAT=0 python -m pip install tensorflow-macos`
  `SYSTEM_VERSION_COMPAT=0 python -m pip install tensorflow-metal`

- install tensorflow addons
  `pip install tensorflow-addons`

### Download training data

- Download, unzip and put images in DIR specified in config.cfg
- http://human-pose.mpi-inf.mpg.de/

### Convert to TF 2

- see https://www.tensorflow.org/guide/migrate/upgrade
- command in /Volumes/Stoage/hourglasstensorlfow/update_to_TF2.ipynb

- manually change the batch normalization layers

example from:

```conv = tf.nn.conv2d(inputs, kernel, [1,strides,strides,1], padding='VALID', data_format='NHWC')
norm = tf.contrib.layers.batch_norm(conv, 0.9, epsilon=1e-5, activation_fn=tf.nn.relu, is_training=self.training)`
```

to:

```conv = tf.nn.conv2d(input=inputs, filters=kernel, strides=[1, strides, strides, 1], padding='VALID', data_format='NHWC')

act_layer = tf.keras.layers.Activation(tf.nn.relu)

norm = tf.keras.layers.BatchNormalization(momentum=0.9, epsilon=1e-5)

normalized = norm(act_layer(conv), training=self.training)
```
