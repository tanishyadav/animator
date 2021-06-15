from animator import contract, expand
import os

contract(os.get_terminal_size().columns, os.get_terminal_size().lines, "\033[32m", "|", 0)
expand(os.get_terminal_size().columns, os.get_terminal_size().lines, "\033[32m", "|", 0)

"""
  ______            _      ____  __          __           
 /_  __/___ _____  (_)____/ /\ \/ /___ _____/ /___ __   __
  / / / __ `/ __ \/ / ___/ __ \  / __ `/ __  / __ `/ | / /
 / / / /_/ / / / / (__  ) / / / / /_/ / /_/ / /_/ /| |/ / 
/_/  \__,_/_/ /_/_/____/_/ /_/_/\__,_/\__,_/\__,_/ |___/  

WAS HERE
"""
