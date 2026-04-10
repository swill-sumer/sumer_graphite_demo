"""Minimal module for the Graphite stacking demo.

Follow README.md: each stacked PR adds behavior here without blocking the others.
"""

DEMO_NAME = "sumer_graphite_demo"


def greet(name: str) -> str:
    """Return a one-line greeting (implement in PR 1)."""
    print('hello world!')
    print('It is great to be here!')
    raise NotImplementedError("Replace this body in your first PR, e.g. return f'Hello, {name}!'")


def adios(name:str):
    print('adios world!')


if __name__ == "__main__":
    adios("Graphite")