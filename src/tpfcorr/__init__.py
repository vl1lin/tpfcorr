"""Correlations — корреляции градиента давления газожидкостного потока в трубах и скважинах.

Публичный API:

* реестр: `get_correlation`, `get_flow_model`, `list_*`, `describe_*`;
* типы: `FlowState`, `FlowPattern`, `FlowPatternResult`, `CorrelationResult`, `BaseOptions`,
  интерфейсы `IFlowModel`, `ICorrelation`;
* ошибки: `ConvergenceError`, `OutOfRangeWarning`, `UnsupportedPatternError`;
* корреляции (`BeggsBrill`, `MukherjeeBrill`, `HasanKabir`, `Ansari`) и модели режима
  с их `*Options`.

Все величины — в СИ.
"""

from importlib.metadata import PackageNotFoundError, version

from tpfcorr.core.errors import ConvergenceError, OutOfRangeWarning, UnsupportedPatternError
from tpfcorr.core.interfaces import ICorrelation, IFlowModel
from tpfcorr.core.options import BaseOptions
from tpfcorr.core.patterns import FlowPattern
from tpfcorr.core.state import CorrelationResult, FlowPatternResult, FlowState
from tpfcorr.flow_models.ansari_fp import AnsariFlowModel, AnsariFlowOptions
from tpfcorr.flow_models.barnea import BarneaModel, BarneaOptions
from tpfcorr.flow_models.beggs_brill_map import BeggsBrillMap, BeggsBrillMapOptions
from tpfcorr.flow_models.hasan_kabir_fp import HasanKabirFlowModel, HasanKabirFlowOptions
from tpfcorr.flow_models.mukherjee_brill_fp import (
    MukherjeeBrillFlowModel,
    MukherjeeBrillFlowOptions,
)
from tpfcorr.flow_models.taitel_dukler import TaitelDuklerModel, TaitelDuklerOptions
from tpfcorr.models.ansari import Ansari, AnsariOptions
from tpfcorr.models.beggs_brill import BeggsBrill, BeggsBrillOptions
from tpfcorr.models.hasan_kabir import HasanKabir, HasanKabirOptions
from tpfcorr.models.mukherjee_brill import MukherjeeBrill, MukherjeeBrillOptions
from tpfcorr.registry import (
    describe_correlation,
    describe_flow_model,
    get_correlation,
    get_flow_model,
    list_correlations,
    list_flow_models,
)

try:
    __version__ = version("tpfcorr")
except PackageNotFoundError:  # пакет не установлен (запуск из исходников без установки)
    __version__ = "0.0.0+unknown"

__all__ = [
    "Ansari",
    "AnsariFlowModel",
    "AnsariFlowOptions",
    "AnsariOptions",
    "BarneaModel",
    "BarneaOptions",
    "BaseOptions",
    "BeggsBrill",
    "BeggsBrillMap",
    "BeggsBrillMapOptions",
    "BeggsBrillOptions",
    "ConvergenceError",
    "CorrelationResult",
    "FlowPattern",
    "FlowPatternResult",
    "FlowState",
    "HasanKabir",
    "HasanKabirFlowModel",
    "HasanKabirFlowOptions",
    "HasanKabirOptions",
    "ICorrelation",
    "IFlowModel",
    "MukherjeeBrill",
    "MukherjeeBrillFlowModel",
    "MukherjeeBrillFlowOptions",
    "MukherjeeBrillOptions",
    "OutOfRangeWarning",
    "TaitelDuklerModel",
    "TaitelDuklerOptions",
    "UnsupportedPatternError",
    "__version__",
    "describe_correlation",
    "describe_flow_model",
    "get_correlation",
    "get_flow_model",
    "list_correlations",
    "list_flow_models",
]
