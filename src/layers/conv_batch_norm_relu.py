import tensorflow as tf


class ConvBatchNormRelu(tf.keras.layers.Layer):
    def __init__(
        self,
        filters: int,
        kernel_size: int,
        strides: int = 1,
        padding: str = "same",
        activation: str = None,
        kernel_initializer: str = "glorot_uniform",
        name: str = "",
        momentum: float = 0.9,
        trainable: bool = False,
        epsilon: float = 1e-5,
    ):
        super(ConvBatchNormRelu, self).__init__(name=name)
        # Define Layers
        self.conv = tf.keras.layers.Conv2D(
            filters=filters,
            kernel_size=kernel_size,
            strides=strides,
            padding=padding,
            name=f"Conv2D",
            activation=activation,
            kernel_initializer=kernel_initializer,
        )
        self.batch_norm = tf.keras.layers.BatchNormalization(
            axis=-1,
            momentum=momentum,
            epsilon=epsilon,
            trainable=trainable,
            name=f"BatchNorm",
        )
        self.relu = tf.keras.layers.ReLU(
            name=f"ReLU",
        )

    def call(self, inputs: tf.Tensor, training: bool = False):
        x = self.conv(inputs)
        x = self.batch_norm(x, training=training)
        x = self.relu(x)
        return x