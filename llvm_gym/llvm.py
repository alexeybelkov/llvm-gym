from pathlib import Path

class LLVMWrapper:
	def __init__(self, llvm_path: Path|str):
		self.llvm_path = Path(llvm_path)
	def run_command(self, command: str):
		pass
	def opt(self, *args):
		pass
	@property
	def version(self) -> str:
		return '15.0.4'