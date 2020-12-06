from typing import List, Optional, Union, Literal
from dataclasses import dataclass, field


@dataclass
class JointDescriptionConfig:
    column_format: str
    index_format: str
    visibility_format: str
    names: List[str]


@dataclass
class DatasetDescriptionConfig:
    image_column: str
    train_test_column: str
    n_joints: int
    joints: JointDescriptionConfig


@dataclass
class DatasetConfig:
    images_folder: str
    summary_file: str
    description: DatasetDescriptionConfig


COLOR_MODE = Union[
    Literal["RGB"],
    Literal["BGR"],
    Literal["RGBA"],
    Literal["BGRA"],
    Literal["GRAYSCALE"],
]
NORMALIZATION_MODE = Union[
    Literal["by255"],
    Literal["MinMax"],
    Literal["normal"],
]


@dataclass
class DataAugmentationConfig:
    rotation: Optional[int] = None


@dataclass
class DataConfig:
    mode: COLOR_MODE
    input_size: int
    output_size: int
    shuffle: bool = False
    normalization: Optional[NORMALIZATION_MODE] = None
    augmentation: Optional[DataAugmentationConfig] = None


@dataclass
class LogConfig:
    log_folder: str


@dataclass
class CheckpointsConfig:
    filepath: str


@dataclass
class ModelConfig:
    name: str
    stages: int
    latent_features: int
    downsamplings: int
    logs: Optional[LogConfig] = None
    checkpoints: Optional[CheckpointsConfig] = None


@dataclass
class LearningRateConfig:
    value: float
    decay: Optional[bool] = False
    decay_step: Optional[int] = None
    decay_value: Optional[float] = None


OPTIMIZERS_TYPES = Union[
    Literal["RMSprop"],
    Literal["Adagrad"],
    Literal["Adam"],
    Literal["Adamax"],
    Literal["SGD"],
]


@dataclass
class OptimizerConfig:
    type: OPTIMIZERS_TYPES
    params: Optional[dict] = field(default_factory=dict)


LOSSES_TYPES = Union[
    Literal["binary_crossentropy"],
]


@dataclass
class LossConfig:
    type: LOSSES_TYPES


METRICS_TYPES = Union[
    Literal["MeanAmountCorrectKeypointsMetric"],
    Literal["LastAmountCorrectKeypointsMetric"],
    Literal["FullAmountCorrectKeypointsMetric"],
    Literal["MeanSquaredError"],
    Literal["MeanAbsoluteError"],
    Literal["MeanAbsolutePercentageError"],
]


@dataclass
class MetricConfig:
    type: METRICS_TYPES
    params: dict = field(default_factory=dict)


@dataclass
class TrainConfig:
    intermediate_supervision: bool
    validation_ratio: float
    epochs: int
    epoch_size: int
    batch_size: int
    learning_rate: LearningRateConfig

    optimizer: OptimizerConfig = OptimizerConfig(type="RMSprop")
    loss: LossConfig = LossConfig(type="binary_crossentropy")
    metrics: Optional[List[MetricConfig]] = None


@dataclass
class HourglassConfig:
    version: str
    dataset: DatasetConfig
    data: DataConfig
    model: ModelConfig
    train: TrainConfig