# FlowTorch project specification

## Purpose

FlowTorch is a desktop, LabVIEW-style visual workbench for people who want to
build and train deep learning models without hand-writing every model
definition. Users should be able to assemble a model as a connected graph,
configure its components, run training, and inspect results in one application.

## Product requirements

1. **Visual model design**
   - Provide a canvas for adding, moving, connecting, and removing model nodes.
   - Represent connections and node parameters in a structured, serializable
     model graph.
   - Validate incomplete or incompatible graphs before model construction.
2. **Model configuration**
   - Expose supported PyTorch layers and their relevant parameters through
     discoverable controls.
   - Provide clear validation feedback for invalid parameters and connections.
3. **Training**
   - Let users configure datasets, loss, optimizer, metrics, and training
     settings through the interface.
   - Execute training without blocking the GUI and report progress and errors.
   - Support reproducible configuration and safe cancellation.
4. **Visualization**
   - Show model structure and useful training metrics, including loss over time.
   - Make training state, failures, and completion visible to the user.
5. **Persistence and reliability**
   - Save and reopen model graphs and training configuration in a documented,
     versioned format.
   - Keep UI, graph validation, model construction, and training responsibilities
     separated and testable.
   - Work without a GPU; GPU acceleration may be used when available.
6. **Documentation and quality**
   - Document installation, graph concepts, training, and supported workflows
     with Sphinx.
   - Test graph validation, model construction, and training behavior without
     requiring a graphical display or GPU.

## Technical direction

- Distribution and import package: `flowtorch`
- Supported Python: 3.10+
- Desktop UI: PySide6 (Essentials distribution)
- Machine-learning framework: PyTorch
- Build and dependency management: `uv` with a committed lockfile
- Documentation: Sphinx
- Package layout: `src/flowtorch`; tests live under `tests/`

## Acceptance criteria

### Bootstrap milestone

- `uv sync --group docs` resolves the project and installs the runtime and
  documentation dependencies.
- `uv run flowtorch` starts a desktop window titled FlowTorch.
- `uv run python -m unittest discover -s tests -v` passes from a clean checkout.
- `uv run --group docs sphinx-build -b html docs docs/_build/html` builds HTML
  documentation without warnings treated as errors.
- The package declares Python 3.10+ and uses PySide6 and PyTorch as its runtime
  dependencies.

### Product milestone

- A user can create a valid model graph with the visual editor, configure node
  parameters, and receive actionable feedback for invalid graphs.
- A valid graph can be translated into a PyTorch model and saved/reopened
  without losing its structure or configuration.
- A user can configure and run training without freezing the interface, observe
  progress and metrics, and cancel a run safely.
- Tests cover graph validation, model generation, persistence, and training
  control paths without requiring a GPU.
