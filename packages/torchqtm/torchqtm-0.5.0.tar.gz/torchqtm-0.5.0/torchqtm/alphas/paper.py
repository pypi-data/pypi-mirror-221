import torchqtm.op as op
import torchqtm.op.functional as F
from torchqtm.op.functional import *
import pandas as pd
import numpy as np
from abc import ABCMeta, abstractmethod
from torchqtm.tdbt.backtest import BackTestEnv
from torchqtm.base import BaseAlpha, Reversion


class IBS(Reversion):
    def __init__(self, env):
        super().__init__(env)
        self.lag = op.Parameter(5, requires_optim=False, feasible_region=None)

    def forward(self):
        self.data = (self.close - F.ts_min(self.low, self.lag)) / (
                    F.ts_max(self.high, self.lag) - F.ts_min(self.low, self.lag))
        return self.data
