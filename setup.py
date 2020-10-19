import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="animator",
    version="0.1",
    author="Tanish Yadav",
    description="Animator is a terminal based animation library for python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tanishyadav/animator",
    packages=["animator"],
    maintainer="Tanish Yadav",
    keywords=["python", "animation", "terminal", "console", "transistion"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers"
        "Development Status :: 5 - Production/Stable",
    ],
)
