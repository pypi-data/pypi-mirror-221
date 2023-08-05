# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Finetuning component task-level defaults."""

from dataclasses import dataclass
from azureml.acft.image.components.finetune.defaults.hf_trainer_defaults import (
    HFTrainerDefaults,
)


@dataclass
class MultiClassClassificationDefaults(HFTrainerDefaults):
    """
    This class contain trainer defaults specific to multiclass classification models.

    Note: This class is not meant to be used directly.
    Provide the defaults name consistently with the Hugging Face Trainer class.
    """

    _num_train_epochs: int = 15
    _lr_scheduler_type: str = "cosine"
    _metric_for_best_model: str = "accuracy"


@dataclass
class MultiLabelClassificationDefaults(HFTrainerDefaults):
    """
    This class contain trainer defaults specific to multilabel classification models.

    Note: This class is not meant to be used directly.
    Provide the defaults name consistently with the Hugging Face Trainer class.
    """

    _num_train_epochs: int = 15
    _lr_scheduler_type: str = "cosine"
    _metric_for_best_model: str = "iou"


@dataclass
class ObjectDetectionDefaults(HFTrainerDefaults):
    """
    This class contain trainer defaults specific to object detection models.

    Note: This class is not meant to be used directly.
    Provide the defaults name consistently with the Hugging Face Trainer class.
    """

    # todo: updated defaults for object detection after benchmarking
    _per_device_train_batch_size: int = 4
    _per_device_eval_batch_size: int = 4
    _learning_rate: float = 5e-4


@dataclass
class InstanceSegmentationDefaults(HFTrainerDefaults):
    """
    This class contain trainer defaults specific to instance segmentation models.

    Note: This class is not meant to be used directly.
    Provide the defaults name consistently with the Hugging Face Trainer class.
    """

    # todo: updated defaults for instance segmentation after benchmarking
    _per_device_train_batch_size: int = 4
    _per_device_eval_batch_size: int = 4
    _learning_rate: float = 5e-4


@dataclass
class MultiObjectTrackingDefaults(HFTrainerDefaults):
    """
    This class contain trainer defaults specific to multi-object tracking models.

    Note: This class is not meant to be used directly.
    Provide the defaults name consistently with the Hugging Face Trainer class.
    """

    # todo: updated defaults for object detection after benchmarking
    _per_device_train_batch_size: int = 1
    _per_device_eval_batch_size: int = 1
    _learning_rate: float = 1e-4
