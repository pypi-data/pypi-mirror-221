"""
Imports models.
"""

from .dvs.model_convtiny_gesture import (convtiny_dvs_gesture,
                                         convtiny_gesture_pretrained)
from .dvs.model_convtiny_handy import (convtiny_dvs_handy,
                                       convtiny_handy_samsung_pretrained)
from .imagenet.model_mobilenet import (mobilenet_imagenet,
                                       mobilenet_imagenet_pretrained)
from .imagenet.model_akidanet import (
    akidanet_imagenet, akidanet_imagenet_pretrained, akidanet_faceidentification_pretrained,
    akidanet_plantvillage_pretrained, akidanet_vww_pretrained)
from .imagenet.model_akidanet_edge import (
    akidanet_edge_imagenet, akidanet_edge_imagenet_pretrained,
    akidanet_faceidentification_edge_pretrained)
from .imagenet.model_akidanet18 import akidanet18_imagenet, akidanet18_imagenet_pretrained
from .kws.model_ds_cnn import ds_cnn_kws, ds_cnn_kws_pretrained
from .modelnet40.model_pointnet_plus import (pointnet_plus_modelnet40,
                                             pointnet_plus_modelnet40_pretrained
                                             )
from .utk_face.model_vgg import vgg_utk_face, vgg_utk_face_pretrained
from .detection.model_yolo import (yolo_base, yolo_widerface_pretrained,
                                   yolo_voc_pretrained)
from .centernet.model_centernet import centernet_base, centernet_voc_pretrained
from .mnist.model_gxnor import gxnor_mnist, gxnor_mnist_pretrained
from .transformers.model_vit import (
    vit_imagenet, vit_ti16, bc_vit_ti16, bc_vit_ti16_imagenet_pretrained, vit_s16, vit_s32, vit_b16,
    vit_b32, vit_l16, vit_l32)
from .transformers.model_deit import (
    deit_imagenet, deit_ti16, bc_deit_ti16, bc_deit_dist_ti16_imagenet_pretrained,
    deit_s16, deit_b16)
from .portrait128.model_akida_unet import akida_unet_portrait128, akida_unet_portrait128_pretrained

from .extract import extract_samples
from .gamma_constraint import add_gamma_constraint
from .utils import fetch_file, get_params_by_version
from .unfuse_sepconv_layers import unfuse_sepconv2d
