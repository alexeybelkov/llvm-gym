from typing import Optional, Any
import numpy as np
import gymnasium as gym
from pathlib import Path
from gymnasium.core import ObsType
from llvm_gym.benchmark import Benchmark, UnitBenchmark
from llvm_gym.llvm import LLVMWrapper

class LLVMEnv(gym.Env):
	def __init__(self, llvm_wrapper: LLVMWrapper):
		self._llvm_wrapper = llvm_wrapper
	@property
	def llvm_wrapper(self) -> LLVMWrapper: return self._llvm_wrapper
	@llvm_wrapper.setter
	def llvm_wrapper(self, llvm_wrapper: LLVMWrapper):
		self._llvm_wrapper = LLVMWrapper
		# full env restart
	def reset(
			self, benchmark: Optional[Benchmark] = None, seed: Optional[int] = None,
			options: Optional[dict[str, Any]] = None,
    ) -> tuple[ObsType, dict[str, Any]]:
		pass