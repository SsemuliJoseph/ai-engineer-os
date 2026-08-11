# Day 05: Python Environments and Dependency Management

## Overview
Today focused on moving away from loose dependency lists (requirements.txt) and mastering deterministic, reproducible environments using uv **lockfiles**. I also updated our custom environment-checking utility to inspect installed package versions dynamically.

### What I Did
Added _Dev Dependencies_: Installed development and code-quality tools (pytest, ruff, and black) as development dependencies using uv add --dev.

**Tracked Lockfiles:** Committed the automatically generated uv.lock file alongside pyproject.toml to Git to ensure exact version consistency.

**Proved Reproducibility:** Tested a fresh environment rebuild by completely deleting the local .venv directory and running uv sync to reconstruct the environment exclusively from the lockfile.

**Extended `check_env.py`:** Integrated Python's standard library importlib.metadata to programmatically verify and print the installed versions of key packages _(pytest, ruff, and black)_.

**Resolved Git Workflow Scenarios:** Handled uncommitted index states, switched branches safely, and synchronized local changes with the remote main branch via `git pull --rebase` and fast-forward merges.
