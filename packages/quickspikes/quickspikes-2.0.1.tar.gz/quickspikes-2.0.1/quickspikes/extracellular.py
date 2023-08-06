# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""specialized functions for extracellular data """
from collections import namedtuple
from typing import Tuple, Optional, Iterator

import numpy as np

Spike = namedtuple(
    "Spike",
    [
        "trough_V",
        "peak1_V",
        "peak1_t",
        "peak2_V",
        "peak2_t",
        "repolarization_slope",
        "recovery_slope",
        "slope_t"
    ],
)
