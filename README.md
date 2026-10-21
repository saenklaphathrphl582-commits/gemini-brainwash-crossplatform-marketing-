# Recursive Prompt Stress Testing and AI Safety Evaluation Framework

A minimal research scaffold for studying recursive prompting behavior, multi-agent interaction patterns, and safety evaluation boundaries in experimental AI systems.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py --experiment-name demo --recursion-depth 3 --max-turns 4
```

## Overview

This repository provides a lightweight Python foundation for building a research pipeline that:

- creates prompt variants
- simulates recursive feedback loops
- tracks context growth over multiple turns
- evaluates safety and consistency conditions
- logs experiment results in a structured format

## Project goals

- document recursive prompting experiments
- support multi-agent research workflows
- evaluate risk and safety thresholds under controlled conditions
- provide a reproducible scaffold for further extension

## License

This repository is intentionally open and research-oriented. Review the project license before redistribution or reuse.
