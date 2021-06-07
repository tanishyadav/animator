# Animator

Animator is a terminal based animation library for python.

## Installation

- Using the package manager pip to install Animator.
```bash
pip install animator
```
or
- Clone this repo with git, cd to the directory and run
```bash
python setup.py install
```

## Usage

```python
import animator as anim
import os

width = os.get_terminal_size().columns
hieght = os.get_terminal_size().lines
anim.expand(width, height)                # makes an expanding animation
anim.contract(width, height)              # makes a contracting animation
```
1. ```expand(width, height, color="\033[0m", print_char="#", time_p_f=0.1)```
- width is the maximum width, the animation will take.
- height is the maximum height, the animation will take.
- color is the ansi code for color of the animation. It deafaults to "\033[0m".
- print_char is the character which will be used to make the animation. It deafauts to "#".
- time_p_f is the time in seconds between every frame. It deafaults to 0.1.

2. ```contract(width, height, color="\033[0m", print_char="#", time_p_f=0.1)```
- width is the maximum width, the animation will take.
- height is the maximum height, the animation will take.
- color is the ansi code for color of the animation. It deafaults to "\033[0m".
- print_char is the character which will be used to make the animation. It deafauts to "#".
- time_p_f is the time in seconds between every frame. It deafaults to 0.1.

## Platform
Animator has been tested to work on Linux and Windows. It should work on MacOS as well.

## Sample
Samples can be found [here](https://github.com/tanishyadav/animator/blob/main/samples).

## Contributing
Animator is open to contribution. You can contribute [here](https://github.com/tanishyadav/animator).

## Maintainers
- [Tanish Yadav](https://github.com/tanishyadav)
## Issues
If you find a bug or issue, you can raise an issue [here](https://github.com/tanishyadav/animator/issues/new).
## License
GNU General Public License v3.0 or later

See COPYING to see the full text.
