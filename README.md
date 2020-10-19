# Animator

Animator is a terminal based animation library for python.

## Installation

- Using the package manager pip to install Animator.

```bash
pip install animator
```
- Or you can install using the [zip file](https://github.com/tanishyadav/animator/archive/main.zip). Go to the directory where you extracted the zip and run
```bash
python setup.py install
```

## Usage

```python
import Animator as anim

anim.expand() # makes a expanding animation
anim.contract() # makes a contracting animation
```
1. ```expand(width, height, color="\033[0m", print_char="#", time_p_f=0.1)```
- width is the width of the console which you can give as os.get_terminal_size().columns
- height is the height of the console which you can give as os.get_terminal_size().lines
- color is the ansi code for color of the animation. It deafaults to "\033[0m".
- print_char is the character which will be used to make the animation. It deafauts to "#".
- time_p_f is the time in seconds between every frame. It deafaults to 0.1.

2. ```contract(width, height, color="\033[0m", print_char="#", time_p_f=0.1)```
- width is the width of the console which you can give as os.get_terminal_size().columns
- height is the height of the console which you can give as os.get_terminal_size().lines
- color is the ansi code for color of the animation. It deafaults to "\033[0m".
- print_char is the character which will be used to make the animation. It deafauts to "#".
- time_p_f is the time in seconds between every frame. It deafaults to 0.1.

## Platform
Animator is OS Independent.

## Sample
Samples can be found [here](https://github.com/tanishyadav/animator/blob/main/samples).

## Contributing
Animator is open to contribution. You can contribute [here](https://github.com/tanishyadav/animator).

## Maintainers
- [Tanish Yadav](https://github.com/tanishyadav)
## Issues
If you find a bug or issue, you can raise an issue [here](https://github.com/tanishyadav/animator/issues/new).
## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
