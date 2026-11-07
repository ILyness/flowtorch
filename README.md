# FlowTorch

FlowTorch is a desktop workbench for visually designing, configuring, training,
and inspecting deep learning models. It is built with PySide6 and PyTorch.

The current version is a project bootstrap with a minimal application window;
the model editor and training workflow are planned in [PROJECT_SPEC.md](PROJECT_SPEC.md).

## Requirements

- Python 3.10 or later
- [uv](https://docs.astral.sh/uv/)

## Setup and run

```bash
uv sync --group docs
uv run flowtorch
```

## Test

```bash
uv run python -m unittest discover -s tests -v
```

## Build the documentation

```bash
uv run --group docs sphinx-build -b html docs docs/_build/html
```