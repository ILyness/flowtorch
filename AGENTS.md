# Agent and contributor guide

## Build, test, run, and documentation commands

- Create/update the environment: `uv sync --group docs`
- Run the desktop starter: `uv run flowtorch`
- Run tests: `uv run python -m unittest discover -s tests -v`
- Build HTML documentation: `uv run --group docs sphinx-build -b html docs docs/_build/html`
- Refresh the lockfile after an approved dependency change: `uv lock`

## Directory structure

```text
.
├── docs/                 # Sphinx source documentation
├── src/
│   └── flowtorch/        # Installable Python package
│       ├── app.py        # Desktop application entry point
│       └── __init__.py
├── tests/                # Automated tests
├── AGENTS.md             # Contributor and agent instructions
├── PROJECT_SPEC.md       # Product requirements and acceptance criteria
├── pyproject.toml        # Project metadata, dependencies, and build config
└── uv.lock               # Reproducible dependency resolution
```

As the product grows, keep model graph/editor, training, and visualization
features in focused subpackages under `src/flowtorch/`, with corresponding
tests under `tests/`.

## Coding conventions

- Support Python 3.10 and later; use standard-library typing and clear public APIs.
- Follow PEP 8, use four-space indentation, and keep lines at or below 88
  characters where practical.
- Keep GUI code separate from model construction and training logic.
- Add or update tests for behavior changes; tests must not require a GPU.
- Keep user-facing and developer documentation current with behavior changes.
- Use `uv` for dependency and environment management; commit `uv.lock`.

## Hard prohibitions

- Do not add runtime or development dependencies without explicit user approval.
- Do not modify `uv.lock` by hand; regenerate it with `uv lock`.
- Do not touch generated output, virtual environments, credentials, or files
  outside the requested change scope.
- Never commit secrets, user datasets, model checkpoints, or generated build
  artifacts.
