from setuptools import setup

with open("t3w.py", 'r') as script_file:
    for line in script_file:
        if not line.startswith("__version__ = "): continue
        __version__ = eval(line[14:].rstrip()); break
    else:
        __version__ = '0.0.0'

setup(
    name="t3w",
    version=__version__,
    py_modules=["t3w"],
    install_requires=[
        "jaxtyping",
        "typer[all]",
    ],
    extras_require={
        "common": [
            "aim",
            "tqdm",
        ],
        "all": [
            "aim",
            "tqdm",
        ]
    },
)