from animator import contract, expand
import os

contract(os.get_terminal_size().columns, os.get_terminal_size().lines, "\033[32m", "|", 0)
expand(os.get_terminal_size().columns, os.get_terminal_size().lines, "\033[32m", "|", 0)
