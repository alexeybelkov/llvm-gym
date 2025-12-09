from pathlib import Path

class Benchmark:
	pass

class UnitBenchmark(Benchmark):
	def __init__(self, src_path: Path|str):
		self.src_path = Path(src_path)
	def read_code(self) -> str:
		pass

	class CMakeBenchmark(Benchmark):
		def __init__(self, src_path: Path|str):
			self.src_path = Path(src_path)