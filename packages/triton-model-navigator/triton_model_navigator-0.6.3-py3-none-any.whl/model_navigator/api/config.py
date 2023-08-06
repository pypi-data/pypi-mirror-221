# Copyright (c) 2021-2023, NVIDIA CORPORATION. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Definition of enums and classes representing configuration for Model Navigator."""
import abc
from dataclasses import dataclass
from enum import Enum
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Protocol,
    Sequence,
    Tuple,
    Type,
    Union,
    runtime_checkable,
)

import numpy

from model_navigator.core.constants import (
    DEFAULT_MAX_WORKSPACE_SIZE,
    DEFAULT_MIN_SEGMENT_SIZE,
    DEFAULT_ONNX_OPSET,
    DEFAULT_PROFILING_THROUGHPUT_CUTOFF_THRESHOLD,
)
from model_navigator.core.logger import LOGGER
from model_navigator.exceptions import ModelNavigatorConfigurationError
from model_navigator.frameworks import Framework
from model_navigator.utils.common import DataObject

Sample = Dict[str, numpy.ndarray]

VerifyFunction = Callable[[Iterable[Sample], Iterable[Sample]], bool]


class DeviceKind(Enum):
    """Supported types of devices.

    Args:
        CPU (str): Select CPU device.
        GPU (str): Select GPU with CUDA support.
    """

    CPU = "cpu"
    CUDA = "cuda"


@runtime_checkable
class SizedIterable(Protocol):
    """Protocol representing sized iterable. Used by dataloader."""

    def __iter__(self) -> Iterator:
        """Magic method __iter__.

        Returns:
            Iterator to next item.
        """
        ...

    def __len__(self) -> int:
        """Magic method __len__.

        Returns:
            Length of size iterable.
        """
        ...


SizedDataLoader = Union[SizedIterable, Sequence]


class Format(Enum):
    """All model formats supported by Model Navigator 'optimize' function.

    Args:
        PYTHON (str): Format indicating any model defined in Python.
        TORCH (str): Format indicating PyTorch model.
        TENSORFLOW (str): Format indicating TensorFlow model.
        JAX (str): Format indicating JAX model.
        TORCHSCRIPT (str): Format indicating TorchScript model.
        TF_SAVEDMODEL (str): Format indicating TensorFlow SavedModel.
        TF_TRT (str): Format indicating TensorFlow TensorRT model.
        TORCH_TRT (str): Format indicating PyTorch TensorRT model.
        ONNX (str): Format indicating ONNX model.
        TENSORRT (str): Format indicating TensorRT model.
    """

    PYTHON = "python"
    TORCH = "torch"
    TENSORFLOW = "tensorflow"
    JAX = "jax"
    TORCHSCRIPT = "torchscript"
    TF_SAVEDMODEL = "tf-savedmodel"
    TF_TRT = "tf-trt"
    TORCH_TRT = "torch-trt"
    ONNX = "onnx"
    TENSORRT = "trt"


class JitType(Enum):
    """TorchScript export parameter.

    Used for selecting the type of TorchScript export.

    Args:
        TRACE (str): Use tracing during export.
        SCRIPT (str): Use scripting during export.
    """

    SCRIPT = "script"
    TRACE = "trace"


class TensorRTPrecision(Enum):
    """Precisions supported during TensorRT conversions.

    Args:
        INT8 (str): 8-bit integer precision.
        FP16 (str): 16-bit floating point precision.
        FP32 (str): 32-bit floating point precision.
    """

    INT8 = "int8"
    FP16 = "fp16"
    FP32 = "fp32"


class TensorRTPrecisionMode(Enum):
    """Precision modes for TensorRT conversions.

    Args:
        HIERARCHY (str): Use TensorRT precision hierarchy starting from highest to lowest.
        SINGLE (str): Use single precision.
        MIXED (str): Use mixed precision.
    """

    HIERARCHY = "hierarchy"
    SINGLE = "single"
    MIXED = "mixed"


class TensorType(Enum):
    """All model formats supported by Model Navigator 'optimize' function."""

    NUMPY = "numpy"
    TORCH = "torch"
    TENSORFLOW = "tensorflow"
    JAX = "jax"


class TensorRTCompatibilityLevel(Enum):
    """Compatibility level for TensorRT.

    Args:
        AMPERE_PLUS (str): Support AMPERE plus architecture
    """

    AMPERE_PLUS = "ampere_plus"


@dataclass
class ShapeTuple(DataObject):
    """Represents a set of shapes for a single binding in a profile.

    Each element of the tuple represents a shape for a single dimension of the binding.

    Args:
        min (Tuple[int]): The minimum shape that the profile will support.
        opt (Tuple[int]): The shape for which TensorRT will optimize the engine.
        max (Tuple[int]): The maximum shape that the profile will support.
    """

    min: Tuple[int, ...]
    opt: Tuple[int, ...]
    max: Tuple[int, ...]

    def __str__(self):
        """String representation."""
        return f"(min={self.min}, opt={self.opt}, max={self.max})"

    def __repr__(self):
        """Representation."""
        return type(self).__name__ + self.__str__()

    def __iter__(self):
        """Iterate over shapes."""
        yield from [self.min, self.opt, self.max]


@dataclass
class OptimizationProfile(DataObject):
    """Optimization profile configuration.

    For each batch size profiler will run measurements in windows of fixed number of queries.
    Batch sizes are profiled in the ascending order.

    Profiler will run multiple trials and will stop when the measurements
    are stable (within `stability_percentage` from the mean) within three consecutive windows.
    If the measurements are not stable after `max_trials` trials, the profiler will stop with an error.
    Profiler will also stop profiling when the throughput does not increase at least by `throughput_cutoff_threshold`.


    Args:
        max_batch_size: Maximal batch size used during conversion and profiling. None mean automatic search is enabled.
        batch_sizes : List of batch sizes to profile. None mean automatic search is enabled.
        window_size: Number of requests to measure in each window.
        stability_percentage: Allowed percentage of variation from the mean in three consecutive windows.
        max_trials: Maximum number of window trials.
        throughput_cutoff_threshold: Minimum throughput increase to continue profiling.
        dataloader: Optional dataloader for profiling. Use only 1 sample.
    """

    max_batch_size: Optional[int] = None
    batch_sizes: Optional[List[Union[int, None]]] = None
    window_size: Optional[int] = 50
    stability_percentage: float = 10.0
    max_trials: int = 10
    throughput_cutoff_threshold: float = DEFAULT_PROFILING_THROUGHPUT_CUTOFF_THRESHOLD
    dataloader: Optional[SizedDataLoader] = None

    def to_dict(self, filter_fields: Optional[List[str]] = None, parse: bool = False) -> Dict:
        """Serialize to a dictionary.

        Append `dataloader` field to filtered fields during dump.

        Args:
            filter_fields (Optional[List[str]], optional): List of fields to filter out.
                Defaults to None.
            parse (bool, optional): If True recursively parse field values to jsonable representation.
                Defaults to False.

        Returns:
            Dict: Data serialized to a dictionary.
        """
        if not filter_fields:
            filter_fields = []

        filter_fields += ["dataloader"]
        return super().to_dict(filter_fields=filter_fields, parse=parse)

    @classmethod
    def from_dict(cls, optimization_profile_dict: Mapping) -> "OptimizationProfile":
        """Instantiate OptimizationProfile class from a dictionary.

        Args:
            optimization_profile_dict (Mapping): Data dictionary.

        Returns:
            OptimizationProfile
        """
        return cls(
            max_batch_size=optimization_profile_dict.get("max_batch_size"),
            batch_sizes=optimization_profile_dict.get("batch_sizes"),
            window_size=optimization_profile_dict.get("window_size"),
            stability_percentage=optimization_profile_dict.get("stability_percentage", 10.0),
            max_trials=optimization_profile_dict.get("max_trials", 10),
            throughput_cutoff_threshold=optimization_profile_dict.get("throughput_cutoff_threshold", -2),
        )


class TensorRTProfile(Dict[str, ShapeTuple]):
    """Single optimization profile that can be used to build an engine.

    More specifically, it is an ``Dict[str, ShapeTuple]`` which maps binding
    names to a set of min/opt/max shapes.
    """

    def add(self, name, min, opt, max):
        """A convenience function to add shapes for a single binding.

        Args:
            name (str): The name of the binding.
            min (Tuple[int]): The minimum shape that the profile will support.
            opt (Tuple[int]): The shape for which TensorRT will optimize the engine.
            max (Tuple[int]): The maximum shape that the profile will support.

        Returns:
            Profile:
                self, which allows this function to be easily chained to add multiple bindings,
                e.g., TensorRTProfile().add(...).add(...)
        """
        self[name] = ShapeTuple(min, opt, max)
        return self

    @classmethod
    def from_dict(cls, profile_dict: Dict[str, Dict[str, Tuple[int, ...]]]):
        """Create a TensorRTProfile from a dictionary.

        Args:
            profile_dict (Dict[str, Dict[str, Tuple[int, ...]]]):
                A dictionary mapping binding names to a dictionary containing ``min``, ``opt``, and
                ``max`` keys.

        Returns:
            TensorRTProfile:
                A TensorRTProfile object.
        """
        return cls({name: ShapeTuple(**shapes) for name, shapes in profile_dict.items()})

    def __getitem__(self, key):
        """Retrieves the shapes registered for a given input name.

        Returns:
            ShapeTuple:
                    A named tuple including ``min``, ``opt``, and ``max`` members for the shapes
                    corresponding to the input.
        """
        if key not in self:
            LOGGER.error(f"Binding: {key} does not have shapes set in this profile")
        return super().__getitem__(key)

    def __repr__(self):
        """Representation."""
        ret = "TensorRTProfile()"
        for name, (min, opt, max) in self.items():
            ret += f".add('{name}', min={min}, opt={opt}, max={max})"
        return ret

    def __str__(self):
        """String representation."""
        elems = []
        for name, (min, opt, max) in self.items():
            elems.append(f"{name} [min={min}, opt={opt}, max={max}]")

        sep = ",\n "
        return "{" + sep.join(elems) + "}"


SERIALIZED_FORMATS = (
    Format.TORCHSCRIPT,
    Format.TF_SAVEDMODEL,
    Format.TF_TRT,
    Format.TORCH_TRT,
    Format.ONNX,
    Format.TENSORRT,
)

SOURCE_FORMATS = (
    Format.TORCH,
    Format.TENSORFLOW,
    Format.JAX,
)

INPUT_FORMATS = {
    Framework.NONE: Format.PYTHON,
    Framework.JAX: Format.JAX,
    Framework.TORCH: Format.TORCH,
    Framework.TENSORFLOW: Format.TENSORFLOW,
    Framework.ONNX: Format.ONNX,
}

EXPORT_FORMATS = {
    Framework.NONE: [],
    Framework.JAX: [Format.TF_SAVEDMODEL],
    Framework.TENSORFLOW: [Format.TF_SAVEDMODEL],
    Framework.TORCH: [Format.TORCHSCRIPT, Format.ONNX],
    Framework.ONNX: [Format.ONNX],
}

DEFAULT_NONE_FRAMEWORK_TARGET_FORMATS = (Format.PYTHON,)

DEFAULT_JAX_TARGET_FORMATS = (
    Format.TF_SAVEDMODEL,
    Format.ONNX,
    Format.TENSORRT,
    Format.TF_TRT,
)

DEFAULT_TENSORFLOW_TARGET_FORMATS = (
    Format.TF_SAVEDMODEL,
    Format.TF_TRT,
    Format.ONNX,
    Format.TENSORRT,
)

DEFAULT_TORCH_TARGET_FORMATS = (
    Format.TORCHSCRIPT,
    Format.ONNX,
    Format.TORCH_TRT,
    Format.TENSORRT,
)

DEFAULT_ONNX_TARGET_FORMATS = (
    Format.ONNX,
    Format.TENSORRT,
)

DEFAULT_TARGET_FORMATS = {
    Framework.NONE: DEFAULT_NONE_FRAMEWORK_TARGET_FORMATS,
    Framework.JAX: DEFAULT_JAX_TARGET_FORMATS,
    Framework.TENSORFLOW: DEFAULT_TENSORFLOW_TARGET_FORMATS,
    Framework.TORCH: DEFAULT_TORCH_TARGET_FORMATS,
    Framework.ONNX: DEFAULT_ONNX_TARGET_FORMATS,
}


AVAILABLE_JAX_TARGET_FORMATS = (Format.JAX,) + DEFAULT_JAX_TARGET_FORMATS

AVAILABLE_TENSORFLOW_TARGET_FORMATS = (Format.TENSORFLOW,) + DEFAULT_TENSORFLOW_TARGET_FORMATS

AVAILABLE_TORCH_TARGET_FORMATS = (Format.TORCH,) + DEFAULT_TORCH_TARGET_FORMATS

AVAILABLE_ONNX_TARGET_FORMATS = DEFAULT_ONNX_TARGET_FORMATS

AVAILABLE_NONE_FRAMEWORK_TARGET_FORMATS = (Format.PYTHON,)

AVAILABLE_TARGET_FORMATS = {
    Framework.NONE: AVAILABLE_NONE_FRAMEWORK_TARGET_FORMATS,
    Framework.JAX: AVAILABLE_JAX_TARGET_FORMATS,
    Framework.TENSORFLOW: AVAILABLE_TENSORFLOW_TARGET_FORMATS,
    Framework.TORCH: AVAILABLE_TORCH_TARGET_FORMATS,
    Framework.ONNX: AVAILABLE_ONNX_TARGET_FORMATS,
}

DEFAULT_TENSORRT_PRECISION = (TensorRTPrecision.FP32, TensorRTPrecision.FP16)
DEFAULT_TENSORRT_PRECISION_MODE = TensorRTPrecisionMode.HIERARCHY


class CustomConfig(abc.ABC):
    """Base class used for custom configs. Input for Model Navigator `optimize` method."""

    @classmethod
    @abc.abstractmethod
    def name(cls) -> str:
        """Name of the CustomConfig."""
        raise NotImplementedError()

    def defaults(self) -> None:
        """Update parameters to defaults."""
        return None

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> "CustomConfig":
        """Instantiate CustomConfig from a dictionary."""
        return cls(**config_dict)


class CustomConfigForFormat(DataObject, CustomConfig):
    """Abstract base class used for custom configs representing particular format."""

    @property
    @abc.abstractmethod
    def format(self) -> Format:
        """Format represented by CustomConfig."""
        raise NotImplementedError()


@dataclass
class TensorFlowConfig(CustomConfigForFormat):
    """TensorFlow custom config used for SavedModel export.

    Args:
        jit_compile: Enable or Disable jit_compile flag for tf.function wrapper for Jax infer function.
        enable_xla: Enable or Disable enable_xla flag for jax2tf converter.

    """

    jit_compile: Tuple[Optional[bool], ...] = (None,)
    enable_xla: Tuple[Optional[bool], ...] = (None,)

    @property
    def format(self) -> Format:
        """Returns Format.TF_SAVEDMODEL.

        Returns:
            Format.TF_SAVEDMODEL
        """
        return Format.TF_SAVEDMODEL

    @classmethod
    def name(cls) -> str:
        """Name of the config."""
        return "TensorFlow"

    def defaults(self) -> None:
        """Update parameters to defaults."""
        self.jit_compile = (None,)
        self.enable_xla = (None,)


@dataclass
class TensorFlowTensorRTConfig(CustomConfigForFormat):
    """TensorFlow TensorRT custom config used for TensorRT SavedModel export.

    Args:
        precision: TensorRT precision.
        max_workspace_size: Max workspace size used by converter.
        minimum_segment_size: Min size of subgraph.
        trt_profile: TensorRT profile.
    """

    precision: Union[
        Union[str, TensorRTPrecision], Tuple[Union[str, TensorRTPrecision], ...]
    ] = DEFAULT_TENSORRT_PRECISION
    max_workspace_size: Optional[int] = DEFAULT_MAX_WORKSPACE_SIZE
    minimum_segment_size: int = DEFAULT_MIN_SEGMENT_SIZE
    trt_profile: Optional[TensorRTProfile] = None

    def __post_init__(self) -> None:
        """Parse dataclass enums."""
        precision = (self.precision,) if not isinstance(self.precision, (list, tuple)) else self.precision
        self.precision = tuple(TensorRTPrecision(p) for p in precision)

    @property
    def format(self) -> Format:
        """Returns Format.TF_TRT.

        Returns:
            Format.TF_TRT
        """
        return Format.TF_TRT

    @classmethod
    def name(cls) -> str:
        """Name of the config."""
        return "TensorFlowTensorRT"

    def defaults(self) -> None:
        """Update parameters to defaults."""
        self.precision = tuple(TensorRTPrecision(p) for p in DEFAULT_TENSORRT_PRECISION)
        self.max_workspace_size = DEFAULT_MAX_WORKSPACE_SIZE
        self.minimum_segment_size = DEFAULT_MIN_SEGMENT_SIZE
        self.trt_profile = None

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> "TensorFlowTensorRTConfig":
        """Instantiate TensorFlowTensorRTConfig from  adictionary."""
        if config_dict.get("trt_profile") is not None and not isinstance(config_dict["trt_profile"], TensorRTProfile):
            config_dict["trt_profile"] = TensorRTProfile.from_dict(config_dict["trt_profile"])
        return cls(**config_dict)


@dataclass
class TorchConfig(CustomConfigForFormat):
    """Torch custom config used for TorchScript export.

    Args:
        jit_type: Type of TorchScript export.
        strict: Enable or Disable strict flag for tracer used in TorchScript export, default: True.

    """

    jit_type: Union[Union[str, JitType], Tuple[Union[str, JitType], ...]] = (JitType.SCRIPT, JitType.TRACE)
    strict: bool = True

    def __post_init__(self) -> None:
        """Parse dataclass enums."""
        jit_type = (self.jit_type,) if not isinstance(self.jit_type, (list, tuple)) else self.jit_type
        self.jit_type = tuple(JitType(j) for j in jit_type)

    @property
    def format(self) -> Format:
        """Returns Format.TORCHSCRIPT.

        Returns:
            Format.TORCHSCRIPT
        """
        return Format.TORCHSCRIPT

    @classmethod
    def name(cls) -> str:
        """Name of the config."""
        return "Torch"

    def defaults(self) -> None:
        """Update parameters to defaults."""
        self.jit_type = (JitType.SCRIPT, JitType.TRACE)
        self.strict = True


@dataclass
class TorchTensorRTConfig(CustomConfigForFormat):
    """Torch custom config used for TensorRT TorchScript conversion.

    Args:
        precision: TensorRT precision.
        max_workspace_size: Max workspace size used by converter.
        trt_profile: TensorRT profile.
    """

    precision: Union[
        Union[str, TensorRTPrecision], Tuple[Union[str, TensorRTPrecision], ...]
    ] = DEFAULT_TENSORRT_PRECISION
    precision_mode: Optional[Union[str, TensorRTPrecisionMode]] = DEFAULT_TENSORRT_PRECISION_MODE
    trt_profile: Optional[TensorRTProfile] = None
    max_workspace_size: Optional[int] = DEFAULT_MAX_WORKSPACE_SIZE

    def __post_init__(self) -> None:
        """Parse dataclass enums."""
        precision = (self.precision,) if not isinstance(self.precision, (list, tuple)) else self.precision
        self.precision = tuple(TensorRTPrecision(p) for p in precision)
        self.precision_mode = TensorRTPrecisionMode(self.precision_mode)

    @property
    def format(self) -> Format:
        """Returns Format.TORCH_TRT.

        Returns:
            Format.TORCH_TRT
        """
        return Format.TORCH_TRT

    @classmethod
    def name(cls) -> str:
        """Name of the config."""
        return "TorchTensorRT"

    def defaults(self) -> None:
        """Update parameters to defaults."""
        self.precision = tuple(TensorRTPrecision(p) for p in DEFAULT_TENSORRT_PRECISION)
        self.precision_mode = DEFAULT_TENSORRT_PRECISION_MODE
        self.trt_profile = None
        self.max_workspace_size = DEFAULT_MAX_WORKSPACE_SIZE

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> "TorchTensorRTConfig":
        """Instantiate TorchTensorRTConfig from  adictionary."""
        if config_dict.get("trt_profile") is not None and not isinstance(config_dict["trt_profile"], TensorRTProfile):
            config_dict["trt_profile"] = TensorRTProfile.from_dict(config_dict["trt_profile"])
        return cls(**config_dict)


@dataclass
class OnnxConfig(CustomConfigForFormat):
    """ONNX custom config used for ONNX export and conversion.

    Args:
        opset: ONNX opset used for conversion.
        dynamic_axes: Dynamic axes for ONNX conversion.
        onnx_extended_conversion: Enables additional conversions from TorchScript to ONNX.

    """

    opset: Optional[int] = DEFAULT_ONNX_OPSET
    dynamic_axes: Optional[Dict[str, Union[Dict[int, str], List[int]]]] = None
    onnx_extended_conversion: bool = False

    @property
    def format(self) -> Format:
        """Returns Format.ONNX.

        Returns:
            Format.ONNX
        """
        return Format.ONNX

    @classmethod
    def name(cls) -> str:
        """Name of the config."""
        return "Onnx"


@dataclass
class TensorRTConfig(CustomConfigForFormat):
    """TensorRT custom config used for TensorRT conversion.

    Args:
        precision: TensorRT precision.
        max_workspace_size: Max workspace size used by converter.
        trt_profile: TensorRT profile.
        optimization_level: Optimization level for TensorRT conversion. Allowed values are fom 0 to 5. Where default is
                            3 based on TensorRT API documentation.
    """

    precision: Union[
        Union[str, TensorRTPrecision], Tuple[Union[str, TensorRTPrecision], ...]
    ] = DEFAULT_TENSORRT_PRECISION
    precision_mode: Union[str, TensorRTPrecisionMode] = TensorRTPrecisionMode.HIERARCHY
    trt_profile: Optional[TensorRTProfile] = None
    max_workspace_size: Optional[int] = DEFAULT_MAX_WORKSPACE_SIZE
    optimization_level: Optional[int] = None
    compatibility_level: Optional[TensorRTCompatibilityLevel] = None

    def __post_init__(self) -> None:
        """Parse dataclass enums."""
        self.precision_mode = TensorRTPrecisionMode(self.precision_mode)
        precision = (self.precision,) if not isinstance(self.precision, (list, tuple)) else self.precision
        self.precision = tuple(TensorRTPrecision(p) for p in precision)

        if self.optimization_level is not None and (self.optimization_level < 0 or self.optimization_level > 5):
            raise ModelNavigatorConfigurationError(
                f"TensorRT `optimization_level` must be between 0 and 5. Provided value: {self.optimization_level}."
            )

    @property
    def format(self) -> Format:
        """Returns Format.TENSORRT.

        Returns:
            Format.TENSORRT
        """
        return Format.TENSORRT

    @classmethod
    def name(cls) -> str:
        """Name of the config."""
        return "TensorRT"

    def defaults(self) -> None:
        """Update parameters to defaults."""
        self.precision = tuple(TensorRTPrecision(p) for p in DEFAULT_TENSORRT_PRECISION)
        self.precision_mode = DEFAULT_TENSORRT_PRECISION_MODE
        self.trt_profile = None
        self.max_workspace_size = DEFAULT_MAX_WORKSPACE_SIZE
        self.optimization_level = None
        self.compatibility_level = None

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> "TensorRTConfig":
        """Instantiate TensorRTConfig from  adictionary."""
        if config_dict.get("trt_profile") is not None and not isinstance(config_dict["trt_profile"], TensorRTProfile):
            config_dict["trt_profile"] = TensorRTProfile.from_dict(config_dict["trt_profile"])
        return cls(**config_dict)


def map_custom_configs(custom_configs: Optional[Sequence[CustomConfig]]) -> Dict:
    """Map custom configs from list to dictionary.

    Args:
        custom_configs: List of custom configs passed to API method

    Returns:
        Mapped configs to dictionary
    """
    if not custom_configs:
        return {}

    return {config.name(): config for config in custom_configs}


def _custom_configs() -> Dict[str, Type[CustomConfigForFormat]]:
    custom_configs = {}
    custom_configs_formats = {}
    for cls in CustomConfigForFormat.__subclasses__():
        assert cls.name() not in custom_configs
        cls_format = cls().format
        assert cls_format not in custom_configs_formats

        custom_configs_formats[cls_format] = custom_configs_formats
        custom_configs[cls.name()] = cls

    return custom_configs


CUSTOM_CONFIGS_MAPPING = _custom_configs()
