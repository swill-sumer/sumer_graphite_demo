"""Minimal module for the Graphite stacking demo.

Follow README.md: each stacked PR adds behavior here without blocking the others.
"""

DEMO_NAME = "sumer_graphite_demo"


def greet(name: str) -> str:
    """Return a one-line greeting (implement in PR 1)."""
    print('hello Steve!')
    raise NotImplementedError("Replace this body in your first PR, e.g. return f'Hello, {name}!'")

def adios(name: str) -> str:
    """Return a one-line goodbye (implement in PR 2)."""
    print('adios Steve!')
    raise NotImplementedError("Replace this body in your second PR, e.g. return f'Goodbye, {name}!'")
