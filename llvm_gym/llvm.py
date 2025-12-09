from pathlib import Path

class LLVMWrapper:
	def __init__(self, llvm_path: Path|str):
		self.llvm_path = Path(llvm_path)