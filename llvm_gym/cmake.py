from pathlib import Path

class CMakeWrapper:
	def __init__(self, cmake_path: Path|str):
		self.cmake_path = cmake_path