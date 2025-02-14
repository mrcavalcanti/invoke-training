import typing

from pydantic import BaseModel


class ImageTransformConfig(BaseModel):
    # The resolution for input images. All of the images in the dataset will be resized to this (square) resolution.
    resolution: int = 512

    # If True, input images will be center-cropped to resolution.
    # If False, input images will be randomly cropped to resolution.
    center_crop: bool = False

    # Whether random flip augmentations should be applied to input images.
    random_flip: bool = False


class ImageCaptionDataLoaderConfig(BaseModel):
    # The name of a Hugging Face dataset.
    # One of dataset_name and dataset_dir should be set (dataset_name takes precedence).
    # See also: dataset_config_name.
    dataset_name: typing.Optional[str] = None

    # The directory to load a dataset from. The dataset is expected to be in
    # Hugging Face imagefolder format (https://huggingface.co/docs/datasets/v2.4.0/en/image_load#imagefolder).
    # One of 'dataset_name' and 'dataset_dir' should be set ('dataset_name' takes precedence).
    dataset_dir: typing.Optional[str] = None

    # The Hugging Face dataset config name. Leave as None if there's only one config.
    # This parameter is only used if dataset_name is set.
    dataset_config_name: typing.Optional[str] = None

    # The Hugging Face cache directory to use for dataset downloads.
    # If None, the default value will be used (usually '~/.cache/huggingface/datasets').
    hf_cache_dir: typing.Optional[str] = None

    # The name of the dataset column that contains image paths.
    image_column: str = "image"

    # The name of the dataset column that contains captions.
    caption_column: str = "text"

    # Number of subprocesses to use for data loading. 0 means that the data will be loaded in the main process.
    dataloader_num_workers: int = 0

    image_transforms: ImageTransformConfig = ImageTransformConfig()


class DreamBoothDataLoaderConfig(BaseModel):
    # The caption to use for all examples in the instance_dataset. Typically has the following form:
    # "a [instance identifier] [class noun]".
    instance_prompt: str

    # The directory to load instance images from.
    instance_data_dir: str

    # The caption to use for all examples in the class_dataset. Typically has the following form: "a [class noun]".
    class_prompt: typing.Optional[str] = None

    # The directory to load class images from.
    class_data_dir: typing.Optional[str] = None

    # The loss weight applied to class dataset examples. Instance dataset examples have an implicit loss weight of 1.0.
    class_data_loss_weight: float = 1.0

    # The image file extensions to include in the dataset.
    # If None, then the following file extensions will be loaded: [".png", ".jpg", ".jpeg"].
    image_file_extensions: typing.Optional[list[str]] = None

    # The image transforms to apply to all instance and class dataset images.
    image_transforms: ImageTransformConfig = ImageTransformConfig()

    # Number of subprocesses to use for data loading. 0 means that the data will be loaded in the main process.
    dataloader_num_workers: int = 0
