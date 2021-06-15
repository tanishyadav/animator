'''
Animator is a terminal based animation library for python.

Copyright (C) 2020 Tanish Yadav

This file is part of Animator.

Animator is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Animator is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <https://www.gnu.org/licenses/>.
'''

# WARNING: Code is very fragile | Handle with great care

import os
import sys
import time

if sys.platform in ("win32", "cygwin"):
    clear_command = "cls"
else:
    clear_command = "clear"

def contract(width, height, color="\033[0m", print_char="#", time_p_f=0.1, ):
    os.system(clear_command)
    if width%2 != 0:
        width -= 1
    if height%2 != 0:
        height -= 1
    nwidth = width
    nheight = height
    frame_made = 0
    while (frame_made <= width/2) and (frame_made <= height/2):
        print(color, end="")
        line_s = (width - nwidth)/2
        ver_s = (height - nheight)/2
        print(int(ver_s)*"\n", end = "")
        print(int(line_s)*" ", print_char*int(nwidth-2))
        line = (" "*int(line_s)) + print_char + (nwidth-2)*" " + print_char
        no_of_line_printed = 0
        while no_of_line_printed <= nheight-2:
            print(line)
            no_of_line_printed += 1
        print(int(line_s)*" ", print_char*int(nwidth-2), "\033[0m")
        frame_made +=1
        nwidth -= 2
        nheight -= 2
        time.sleep(time_p_f)
        os.system(clear_command)

def expand(width, height, color="\033[0m", print_char="#", time_p_f=0.1, ):
    os.system(clear_command)
    if width%2 != 0:
        width -= 1
    if height%2 != 0:
        height -= 1
    if width >= height:
        nheight = 2
        nwidth = width - (height-2)
    elif height >= height:
        nwidth = 2
        nheight = height - (width-2)
    frame_made = 0
    while (frame_made <= (width/2)-2) and (frame_made <= (height/2)-2):
        print(color, end="")
        line_s = (width - nwidth)/2
        ver_s = (height - nheight)/2
        print(int(ver_s)*"\n", end = "")
        print(int(line_s)*" ", print_char*int(nwidth-2))
        line = (" "*int(line_s)) + print_char + (nwidth-2)*" " + print_char
        no_of_line_printed = 0
        while no_of_line_printed <= nheight-2:
            print(line)
            no_of_line_printed += 1
        print(int(line_s)*" ", print_char*int(nwidth-2), "\033[0m")
        frame_made +=1
        nwidth += 2
        nheight += 2
        time.sleep(time_p_f)
        os.system(clear_command)

"""
  ______            _      ____  __          __           
 /_  __/___ _____  (_)____/ /\ \/ /___ _____/ /___ __   __
  / / / __ `/ __ \/ / ___/ __ \  / __ `/ __  / __ `/ | / /
 / / / /_/ / / / / (__  ) / / / / /_/ / /_/ / /_/ /| |/ / 
/_/  \__,_/_/ /_/_/____/_/ /_/_/\__,_/\__,_/\__,_/ |___/  

WAS HERE
"""
