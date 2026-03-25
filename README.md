# ![patlab-logo](docs/docs/assets/patlab-logo.png)

[![PyPI version](https://img.shields.io/pypi/v/patlab.svg)](https://pypi.org/project/patlab/)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
[![License](https://img.shields.io/github/license/sayampradhan/patlab.svg)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/patlab.svg)](https://pypi.org/project/patlab/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19225415.svg)](https://doi.org/10.5281/zenodo.19225415)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linting: Ruff](https://img.shields.io/badge/linting-ruff-blueviolet.svg)](https://github.com/astral-sh/ruff)
[![Issues](https://img.shields.io/github/issues/sayampradhan/patlab)](https://github.com/sayampradhan/patlab/issues)
[![Stars](https://img.shields.io/github/stars/sayampradhan/patlab)](https://github.com/sayampradhan/patlab/stargazers)
<!-- [![Coverage](https://img.shields.io/codecov/c/github/sayampradhan/patlab)](https://codecov.io/gh/sayampradhan/patlab) -->
<!-- [![Build Status](https://img.shields.io/github/actions/workflow/status/your-username/patlab/ci.yml?branch=main)](https://github.com/your-username/patlab/actions) -->

**Patlab** is a lightweight Python library for generating common text-based patterns such as squares, pyramids, and triangles with clean and customizable APIs.

It’s designed for beginners, educators, and developers who want a simple way to generate patterns programmatically.

## ✨ Features

- Generate common patterns easily:
  - Squares
  - Pyramids (centered, right-aligned, numeric)
  - Right-angled triangles (classic, inverted)
- Support for:
  - Custom characters
  - Hollow patterns
  - Numeric patterns
- Clean, readable API design
- Minimal dependencies

## 📦 Installation

Install via pip:

```bash
pip install patlab
```

## 🚀 Quick Start
```python
from patlab.square import square
from patlab.pyramid import centered
from patlab.right_triangle import classic

print(square(3))
print(centered(4))
print(classic(4))
```

For full documentation, see: https://sayampradhan.github.io/patlab/


## 🧪 Testing
Tests are included using `pytest`.

Run tests locally:
```
pytest
```

## 📜 License
This project is licensed under the terms of the MIT License.

## 🤝 Contributing

Contributions are welcome!

If you’d like to improve patlab:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request
