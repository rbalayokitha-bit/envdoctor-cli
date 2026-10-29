import os
import zipfile

# Create directory structure for the project
project_dir = "cli_diagnostics_tool"
os.makedirs(os.path.join(project_dir, "src", "cli_diagnostics"), exist_ok=True)
os.makedirs(os.path.join(project_dir, "tests"), exist_ok=True)

# 1. pyproject.toml
pyproject_content = """[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "cli-diagnostics"
version = "0.1.0"
description = "A distributable command-line tool that inspects a machine and produces a deterministic developer-environment health report."
readme = "README.md"
requires-python = ">=3.8"
authors = [
    { name = "Developer", email = "dev@example.com" }
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = []

[project.scripts]
cli-diagnostics = "cli_diagnostics.cli:main"

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
"""

with open(os.path.join(project_dir, "pyproject.toml"), "w") as f:
    f.write(pyproject_content)

# 2. README.md
readme_content = """# CLI Diagnostics Tool

A distributable command-line tool built with Python that inspects a machine and generates a deterministic developer-environment health report.

## Features
- **System Diagnostics**: Inspects Python runtime version, available disk space, key environment variables (`PATH`, `SHELL`, `HOME`/`USERPROFILE`, `VIRTUAL_ENV`), and essential dev tools (`git`, `docker`, `python3`, `node`, `npm`, `pip`, `gcc`, `make`).
- **Deterministic Output**: Ensures reproducible report keys, ordered dictionaries, and normalized paths/values.
- **Dual Output Modes**: Standard human-readable terminal output and structured `--json` output.
- **Exit Codes**: Returns `0` on success/healthy environment and `1` on missing critical tools/checks or errors.
- **Custom Config**: Supports specifying custom paths or settings via `--config` file.

## Installation & Setup

### Local Installation (Editable Mode)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -e .