#!/usr/bin/env python
# ******************************************************************************
# Copyright 2021 Brainchip Holdings Ltd.
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
This model is an adaptation of the `akidanet_imagenet` model for edge
applications. It is based on AkidaNet with top layers replaced by a quantized
spike extractor and a classification layer.
"""

from keras import Model
from keras.layers import Reshape

from cnn2snn import quantize_layer, get_akida_version, AkidaVersion

from ..layer_blocks import separable_conv_block, dense_block
from ..utils import fetch_file, get_params_by_version
from ..model_io import load_model, get_model_path


def akidanet_edge_imagenet(base_model, classes, base_layer="classifier"):
    """Instantiates an AkidaNet-edge architecture.

    Args:
        base_model (str/keras.Model): an akidanet_imagenet base model.
        classes (int): the number of classes for the edge classifier.
        base_layer (str, optional): the last base layer. Defaults to "classifier".

    Returns:
        keras.Model: a Keras Model instance.
    """
    if isinstance(base_model, str):
        base_model = load_model(base_model)

    is_v1 = get_akida_version() == AkidaVersion.v1
    try:
        # Identify the base model classifier
        base_classifier = base_model.get_layer(base_layer)
        if is_v1:
            # remember the classifier weight bitwidth
            wq = base_classifier.quantizer.bitwidth
    except Exception as e:
        raise ValueError("The base model is not a quantized AkidaNet/Imagenet model") from e

    # Model version management
    fused, _, _ = get_params_by_version()

    # Recreate a model with all layers up to the classifier
    x = base_classifier.input
    x = Reshape((1, 1, x.shape[-1]))(x)
    # Add the new end layer with kernel_size (3, 3) instead of (1, 1) for
    # hardware compatibility reasons
    # Because it will be quantized to 1 bit, the ReLU max_value should be set to 1
    x = separable_conv_block(x,
                             filters=2048,
                             kernel_size=(3, 3),
                             padding='same',
                             use_bias=False,
                             add_batchnorm=True,
                             name='spike_generator',
                             fused=fused,
                             relu_activation='ReLU1')

    # Then add the Akida edge learning layer that will be dropped after
    x = dense_block(x,
                    classes,
                    name="classification_layer",
                    relu_activation=False,
                    add_batchnorm=False,
                    use_bias=False)
    x = Reshape((classes,), name="reshape_3")(x)

    # Create model
    model = Model(inputs=base_model.input,
                  outputs=x,
                  name=f"{base_model.name}_edge")

    # When targeting Akida V1, edge layers can be quantized and tuned which is not the case for V2
    # (float head training is required).
    if is_v1:
        # Quantize edge layers
        model = quantize_layer(model, 'spike_generator', wq)
        model = quantize_layer(model, 'spike_generator/relu', 1)
        # NOTE: quantization set to 2 here, to be as close as
        # possible to the Akida native layer that will replace this one,
        # with binary weights.
        model = quantize_layer(model, 'classification_layer', 2)

    return model


def akidanet_edge_imagenet_pretrained():
    """ Helper method to retrieve a `akidanet_edge_imagenet` model that was
    trained on ImageNet dataset.

    Returns:
        keras.Model: a Keras Model instance.

    """
    model_name_v1 = 'akidanet_imagenet_224_alpha_50_edge_iq8_wq4_aq4.h5'
    file_hash_v1 = '71ffc3acb09e5682e479505f6b288bd2736311ce46d3974bdf7b2c02916e52a8'
    model_path, model_name, file_hash = get_model_path("akidanet_edge", model_name_v1, file_hash_v1)
    model_path = fetch_file(model_path,
                            fname=model_name,
                            file_hash=file_hash,
                            cache_subdir='models')
    return load_model(model_path)


def akidanet_faceidentification_edge_pretrained():
    """
    Helper method to retrieve an `akidanet_edge_imagenet` model that was trained
    on CASIA Webface dataset and that performs face identification.

    Returns:
        keras.Model: a Keras Model instance.

    """
    model_name_v1 = 'akidanet_faceidentification_edge_iq8_wq4_aq4.h5'
    file_hash_v1 = '61838682cc88cec6dc9a347f1a301bfa9e94fbcbc7a52a273789259de07d3104'
    model_name_v2 = 'akidanet_faceidentification_edge_i8_w4_a4.h5'
    file_hash_v2 = '2b0fed9bb88674ebba2925cdd76c26232c418d43b7e05b8ba8121861fcc49137'
    model_path, model_name, file_hash = get_model_path("akidanet_edge", model_name_v1, file_hash_v1,
                                                       model_name_v2, file_hash_v2)
    model_path = fetch_file(model_path,
                            fname=model_name,
                            file_hash=file_hash,
                            cache_subdir='models')
    return load_model(model_path)
