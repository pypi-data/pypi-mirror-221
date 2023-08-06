import tensorflow as tf

from . import _tensorflow_model


class LocalCnn(_tensorflow_model.TensorflowModel):
    """
    Implementation of a class for a Locally-connected Convolutional Neural Network (LocalCNN).

    See :obj:`~easypheno.model._base_model.BaseModel` and :obj:`~easypheno.model._tensorflow_model.TensorflowModel` for more information on the attributes.
    """
    standard_encoding = 'onehot'
    possible_encodings = ['onehot']

    def define_model(self) -> tf.keras.Sequential:
        """
        Definition of a LocalCNN network.

        Architecture:

            - LocallyConnected1D, BatchNorm, Dropout, MaxPool1D, Flatten
            - N_LAYERS of (Dense + BatchNorm + Dropout)
            - Dense output layer

        Kernel size for LocallyConnectedLayer and max pooling layer may be fixed or optimized.
        Same applies for stride, number of units in the first dense layer and percentage decrease after each layer.
        """
        n_layers = self.suggest_hyperparam_to_optuna('n_layers')
        model = tf.keras.Sequential()
        act_function = tf.keras.layers.Activation(self.suggest_hyperparam_to_optuna('act_function'))
        l1_regularizer = None  # tf.keras.regularizers.L1(l1=self.suggest_hyperparam_to_optuna('l1_factor'))
        in_channels = self.width_onehot
        width = self.n_features
        model.add(tf.keras.Input(shape=(width, in_channels)))
        n_filters = 1
        kernel_size = int(2 ** self.suggest_hyperparam_to_optuna('kernel_size_exp'))
        stride = max(1, int(kernel_size * self.suggest_hyperparam_to_optuna('stride_perc_of_kernel_size')))
        model.add(tf.keras.layers.LocallyConnected1D(filters=n_filters, kernel_size=kernel_size,
                                                     strides=stride, activation=None,
                                                     kernel_regularizer=l1_regularizer))
        model.add(act_function)
        model.add(tf.keras.layers.BatchNormalization())
        p = self.suggest_hyperparam_to_optuna('dropout')
        model.add(tf.keras.layers.Dropout(rate=p, seed=42))
        kernel_size_max_pool = 2 ** 4  # self.suggest_hyperparam_to_optuna('maxpool_kernel_size_exp')
        model.add(tf.keras.layers.MaxPool1D(pool_size=kernel_size_max_pool))
        model.add(tf.keras.layers.Flatten())
        n_units = int(model.output_shape[1] * self.suggest_hyperparam_to_optuna('n_initial_units_factor'))
        perc_decrease = self.suggest_hyperparam_to_optuna('perc_decrease_per_layer')
        for layer in range(n_layers):
            model.add(tf.keras.layers.Dense(units=n_units, activation=None,
                                            kernel_regularizer=l1_regularizer))
            model.add(act_function)
            model.add(tf.keras.layers.BatchNormalization())
            model.add(tf.keras.layers.Dropout(rate=p))
            n_units = int(n_units * (1-perc_decrease))
        model.add(tf.keras.layers.Dense(units=self.n_outputs))
        return model

    def define_hyperparams_to_tune(self) -> dict:
        """
        See :obj:`~easypheno.model._base_model.BaseModel` for more information on the format.

        See TensorflowModel for more information on hyperparameters common for all tensorflow models.
        """

        if self.n_features < 20000:
            kernel_size_exp = {
                # Exponent with base 2 to get the kernel size for the convolutional layers
                'datatype': 'categorical',
                'list_of_values': [2.6, 3, 3.4, 3.6, 3.9]  # 6, 8, 10, 12, 14
            }
        else:
            kernel_size_exp = {
                # Exponent with base 2 to get the kernel size for the convolutional layers
                'datatype': 'int',
                'lower_bound': 3,
                'upper_bound': 7
            }

        return {
            'n_layers': {
                'datatype': 'int',
                'lower_bound': 1,
                'upper_bound': 3
            },
            'kernel_size_exp': kernel_size_exp,
            'maxpool_kernel_size_exp': {
                # Exponent with base 2 to get the kernel size for the maxpool layers
                'datatype': 'int',
                'lower_bound': 2,
                'upper_bound': 4
            },
            'stride_perc_of_kernel_size': {
                # Stride in relation to the kernel size
                'datatype': 'float',
                'lower_bound': 0.5,
                'upper_bound': 1,
                'step': 0.1
            },
            'n_initial_units_factor': {
                # Number of units in the linear layer after flattening in relation to the number of inputs
                'datatype': 'float',
                'lower_bound': 0.1,
                'upper_bound': 0.7,
                'step': 0.05
            },
            'perc_decrease_per_layer': {
                # Percentage decrease of the number of units per layer
                'datatype': 'float',
                'lower_bound': 0.2,
                'upper_bound': 0.5,
                'step': 0.05
            }
        }
