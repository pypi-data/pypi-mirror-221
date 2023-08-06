# `t3w.py` - Typed Thin (Py)Torch Wrapper

T3W is a lightweight framework for training PyTorch models written by Yuyao Huang during his PhD at Tongji University.
- T3W is "typed". It leverages a stronger and static type compared to normal python code for clearer architecture and less bugs. The programming model is object-oriented. Users (you) are required to implement interfaces as subclasses and inject them as dependencies.
- T3W is "thin". With the philosophy "less is more" in mind, it leverages a minimal codebase with an extensible plugin system under interface `ISideEffect`. Its core codebase only requires PyTorch to run.
- T3W stands with "PyTorch".

See the concise example [mnist_example.py](https://github.com/tjyuyao/t3w/blob/main/mnist_example.py).

If you feel like using `t3w.py`, you can install it with `pip install t3w`, `pip install t3w[common]`, or `pip install t3w[all]`, where the latter will install common side effects dependencies like `tqdm` etc. Note that the mnist example requires installing `t3w[common]`.

Detailed documentation will come in the future.