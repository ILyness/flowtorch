"""Sphinx configuration for FlowTorch documentation."""

project = "FlowTorch"
copyright = "2026, FlowTorch contributors"
author = "FlowTorch contributors"
release = "0.1.0"

extensions: list[str] = []
templates_path = ["_templates"]
exclude_patterns = ["_build"]

html_theme = "alabaster"
