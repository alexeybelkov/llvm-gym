from typing import Any
import numpy as np

class Reward:
	def __init__(self, init: float = 0.0): self.init = init
	def step(self, state: Any): return 1