#!/usr/bin/env python
# ******************************************************************************
# Copyright 2020 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************
"""
MobileNet model definition for ImageNet classification.

MobileNet V1 is a general architecture and can be used for multiple use cases.

This specific version includes parameter options to generate a mobilenet version
compatible for Akida with:
    - overall architecture compatible with Akida (conv stride 2 replaced with
     max pool),
    - options to quantize weights and activations,
    - different initialization options.
"""

from keras import Model, regularizers
from keras.layers import Input, Dropout, Rescaling

from .imagenet_utils import obtain_input_shape
from ..layer_blocks import conv_block, separable_conv_block, dense_block
from ..utils import fetch_file, get_params_by_version
from ..model_io import load_model, get_model_path


def mobilenet_imagenet(input_shape=None,
                       alpha=1.0,
                       dropout=1e-3,
                       include_top=True,
                       pooling=None,
                       classes=1000,
                       use_stride2=True,
                       input_scaling=(128, -1)):
    """Instantiates the MobileNet architecture.

    Args:
        input_shape (tuple, optional): shape tuple. Defaults to None.
        alpha (float, optional): controls the width of the model.
            Defaults to 1.0.

            * If `alpha` < 1.0, proportionally decreases the number of filters
              in each layer.
            * If `alpha` > 1.0, proportionally increases the number of filters
              in each layer.
            * If `alpha` = 1, default number of filters from the paper are used
              at each layer.
        dropout (float, optional): dropout rate. Defaults to 1e-3.
        include_top (bool, optional): whether to include the fully-connected
            layer at the top of the model. Defaults to True.
        pooling (str, optional): optional pooling mode for feature extraction
            when `include_top` is `False`.
            Defaults to None.

            * `None` means that the output of the model will be the 4D tensor
              output of the last convolutional block.
            * `avg` means that global average pooling will be applied to the
              output of the last convolutional block, and thus the output of the
              model will be a 2D tensor.
        classes (int, optional): optional number of classes to classify images
            into, only to be specified if `include_top` is `True`. Defaults to 1000.
        use_stride2 (bool, optional): replace max pooling operations by stride 2
            convolutions in layers separable 2, 4, 6 and 12. Defaults to True.
        input_scaling (tuple, optional): scale factor and offset to apply to
            inputs. Defaults to (128, -1). Note that following Akida convention,
            the scale factor is an integer used as a divider.

    Returns:
        keras.Model: a Keras model for MobileNet/ImageNet.

    Raises:
        ValueError: in case of invalid input shape.
    """
    # Model version management
    fused, post_relu_gap, relu_activation = get_params_by_version(relu_v2='ReLU7.5')

    # Define weight regularization, will apply to the first convolutional layer
    # and to all pointwise weights of separable convolutional layers.
    weight_regularizer = regularizers.l2(4e-5)

    # Define stride 2 or max pooling
    if use_stride2:
        sep_conv_pooling = None
        strides = 2
    else:
        sep_conv_pooling = 'max'
        strides = 1

    # Determine proper input shape and default size.
    if input_shape is None:
        default_size = 224
    else:
        rows = input_shape[0]
        cols = input_shape[1]

        if rows == cols and rows in [128, 160, 192, 224]:
            default_size = rows
        else:
            default_size = 224

    input_shape = obtain_input_shape(input_shape,
                                     default_size=default_size,
                                     min_size=32,
                                     include_top=include_top)

    rows = input_shape[0]
    cols = input_shape[1]

    img_input = Input(shape=input_shape, name="input")

    if input_scaling is None:
        x = img_input
    else:
        scale, offset = input_scaling
        x = Rescaling(1. / scale, offset, name="rescaling")(img_input)

    x = conv_block(x,
                   filters=int(32 * alpha),
                   name='conv_0',
                   kernel_size=(3, 3),
                   padding='same',
                   use_bias=False,
                   strides=2,
                   add_batchnorm=True,
                   relu_activation=relu_activation,
                   kernel_regularizer=weight_regularizer)

    x = separable_conv_block(x,
                             filters=int(64 * alpha),
                             name='separable_1',
                             kernel_size=(3, 3),
                             padding='same',
                             use_bias=False,
                             add_batchnorm=True,
                             relu_activation=relu_activation,
                             fused=fused,
                             pointwise_regularizer=weight_regularizer)

    x = separable_conv_block(x,
                             filters=int(128 * alpha),
                             name='separable_2',
                             kernel_size=(3, 3),
                             padding='same',
                             pooling=sep_conv_pooling,
                             strides=strides,
                             use_bias=False,
                             add_batchnorm=True,
                             relu_activation=relu_activation,
                             fused=fused,
                             pointwise_regularizer=weight_regularizer)

    x = separable_conv_block(x,
                             filters=int(128 * alpha),
                             name='separable_3',
                             kernel_size=(3, 3),
                             padding='same',
                             use_bias=False,
                             add_batchnorm=True,
                             relu_activation=relu_activation,
                             fused=fused,
                             pointwise_regularizer=weight_regularizer)

    x = separable_conv_block(x,
                             filters=int(256 * alpha),
                             name='separable_4',
                             kernel_size=(3, 3),
                             padding='same',
                             pooling=sep_conv_pooling,
                             strides=strides,
                             use_bias=False,
                             add_batchnorm=True,
                             relu_activation=relu_activation,
                             fused=fused,
                             pointwise_regularizer=weight_regularizer)

    x = separable_conv_block(x,
                             filters=int(256 * alpha),
                             name='separable_5',
                             kernel_size=(3, 3),
                             padding='same',
                             use_bias=False,
                             add_batchnorm=True,
                             relu_activation=relu_activation,
                             fused=fused,
                             pointwise_regularizer=weight_regularizer)

    x = separable_conv_block(x,
                             filters=int(512 * alpha),
                             name='separable_6',
                             kernel_size=(3, 3),
                             padding='same',
                             pooling=sep_conv_pooling,
                             strides=strides,
                             use_bias=False,
                             add_batchnorm=True,
                             relu_activation=relu_activation,
                             fused=fused,
                             pointwise_regularizer=weight_regularizer)

    x = separable_conv_block(x,
                             filters=int(512 * alpha),
                             name='separable_7',
                             kernel_size=(3, 3),
                             padding='same',
                             use_bias=False,
                             add_batchnorm=True,
                             relu_activation=relu_activation,
                             fused=fused,
                             pointwise_regularizer=weight_regularizer)

    x = separable_conv_block(x,
                             filters=int(512 * alpha),
                             name='separable_8',
                             kernel_size=(3, 3),
                             padding='same',
                             use_bias=False,
                             add_batchnorm=True,
                             relu_activation=relu_activation,
                             fused=fused,
                             pointwise_regularizer=weight_regularizer)

    x = separable_conv_block(x,
                             filters=int(512 * alpha),
                             name='separable_9',
                             kernel_size=(3, 3),
                             padding='same',
                             use_bias=False,
                             add_batchnorm=True,
                             relu_activation=relu_activation,
                             fused=fused,
                             pointwise_regularizer=weight_regularizer)

    x = separable_conv_block(x,
                             filters=int(512 * alpha),
                             name='separable_10',
                             kernel_size=(3, 3),
                             padding='same',
                             use_bias=False,
                             add_batchnorm=True,
                             relu_activation=relu_activation,
                             fused=fused,
                             pointwise_regularizer=weight_regularizer)

    x = separable_conv_block(x,
                             filters=int(512 * alpha),
                             name='separable_11',
                             kernel_size=(3, 3),
                             padding='same',
                             use_bias=False,
                             add_batchnorm=True,
                             relu_activation=relu_activation,
                             fused=fused,
                             pointwise_regularizer=weight_regularizer)

    x = separable_conv_block(x,
                             filters=int(1024 * alpha),
                             name='separable_12',
                             kernel_size=(3, 3),
                             padding='same',
                             pooling=sep_conv_pooling,
                             strides=strides,
                             use_bias=False,
                             add_batchnorm=True,
                             relu_activation=relu_activation,
                             fused=fused,
                             pointwise_regularizer=weight_regularizer)

    # Last separable layer with global pooling
    layer_pooling = 'global_avg' if include_top or pooling == 'avg' else None
    x = separable_conv_block(x,
                             filters=int(1024 * alpha),
                             name='separable_13',
                             kernel_size=(3, 3),
                             padding='same',
                             pooling=layer_pooling,
                             use_bias=False,
                             add_batchnorm=True,
                             relu_activation=relu_activation,
                             fused=fused,
                             post_relu_gap=post_relu_gap,
                             pointwise_regularizer=weight_regularizer)

    if include_top:
        x = Dropout(dropout, name='dropout')(x)
        x = dense_block(x,
                        units=classes,
                        name='classifier',
                        use_bias=False,
                        add_batchnorm=False,
                        relu_activation=False,
                        kernel_regularizer=weight_regularizer)

    # Create model.
    return Model(img_input, x, name='mobilenet_%0.2f_%s_%s' % (alpha, rows, classes))


def mobilenet_imagenet_pretrained(alpha=1.0):
    """
    Helper method to retrieve a `mobilenet_imagenet` model that was trained on
    ImageNet dataset.

    Args:
        alpha (float): width of the model.

    Returns:
        keras.Model: a Keras Model instance.

    """
    if alpha == 1.0:
        model_name_v1 = 'mobilenet_imagenet_224_iq8_wq4_aq4.h5'
        file_hash_v1 = '4e63ea329b3f2f773a0b9d6fef4e449639fda89d17e48bb7132b6ad86585c867'
        model_name_v2 = 'mobilenet_imagenet_224_alpha_1_i8_w4_a4.h5'
        file_hash_v2 = 'da329c8b6836c141a7b836875dbcabd36d8efd5b90d9719f50e2d4facea4868a'
    elif alpha == 0.5:
        model_name_v1 = 'mobilenet_imagenet_224_alpha_50_iq8_wq4_aq4.h5'
        file_hash_v1 = '6a5c51cb1a5ae022f2c025affb4022842078dbbb970fb07fdc9fd9e0eb1acd2f'
        model_name_v2 = 'mobilenet_imagenet_224_alpha_0.5_i8_w4_a4.h5'
        file_hash_v2 = 'c7277a7850c777a39c90023a7c509696bc7a2cb61590d3c88841f1ee3bc14003'
    elif alpha == 0.25:
        model_name_v1 = 'mobilenet_imagenet_224_alpha_25_iq8_wq4_aq4.h5'
        file_hash_v1 = '35ad51e662ed04b68978865ccb1c16bf024fa013146488b2a9c18c80d1efab29'
        model_name_v2 = 'mobilenet_imagenet_224_alpha_0.25_i8_w4_a4.h5'
        file_hash_v2 = '29eb66a023fa808735e66f3716e3a8d6429a5d9621e6ed875de4fc8104682a14'
    else:
        raise ValueError(
            f"Requested model with alpha={alpha} is not available.")

    model_path, model_name, file_hash = get_model_path("mobilenet", model_name_v1, file_hash_v1,
                                                       model_name_v2, file_hash_v2)
    model_path = fetch_file(model_path,
                            fname=model_name,
                            file_hash=file_hash,
                            cache_subdir='models')
    return load_model(model_path)
