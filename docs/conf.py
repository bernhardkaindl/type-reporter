"""Sphinx configuration."""

project = "Type Reporter"
author = "Bernhard Kaindl"
copyright = "2024, Bernhard Kaindl"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
