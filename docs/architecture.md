# Architecture Overview

## Purpose

This repository provides a minimal yet extensible scaffold for a research system focused on recursive prompt evaluation, multi-agent interaction studies, and safety boundary analysis.

## Core components

### 1. Entry point
The root `main.py` file provides a simple CLI interface for running an experiment. It parses arguments such as:

- experiment name
- recursion depth
- maximum turns
- safety mode

This keeps the system accessible while maintaining a clear entry point for research automation.

### 2. Application layer
The `src/app.py` module defines the public interface used by the CLI. It creates a `ResearchPipeline` instance and returns a structured result dictionary.

### 3. Pipeline layer
The `src/pipeline.py` module contains the logic for:

- constructing prompt variants
- simulating recursive depth
- tracking turn count
- scoring risk levels
- evaluating safety outcomes

This is the operational core of the project and is intended to be extended with more advanced evaluation logic.

### 4. Package boundary
The `src/__init__.py` file marks the package boundary and exposes the research module cleanly for imports.

## Execution flow

1. CLI parses environment or user arguments.
2. `main.py` invokes `run_experiment(...)` in `src/app.py`.
3. `ResearchPipeline.run()` generates recursive prompts and evaluates safety risk.
4. The result is returned as a structured dictionary and printed to the console.

## Example runtime model

```text
CLI / main.py
    -> src.app.run_experiment()
        -> ResearchPipeline.run()
            -> prompt generation
            -> recursion modeling
            -> risk scoring
            -> safety classification
            -> JSON-like result summary
```

## Design goals

- keep dependencies minimal
- remain immediately runnable
- support extensibility for future model adapters and evaluators
- preserve a clear distinction between experiments, safety checks, and results

## Recommended extensions

The scaffold is deliberately small so it can grow into a fuller research project. Recommended next additions include:

- prompt registry and templates
- agent orchestration layer
- evaluation metrics module
- structured logging and output storage
- result export to JSON or CSV
- model-provider abstraction
- multi-agent simulation environment

## Research orientation

This architecture deliberately separates:

- script execution
- pipeline logic
- safety assessment
- reporting output

This separation makes the system easier to test, audit, and extend as the project evolves from a prototype into a larger research framework.

## Summary

This minimal architecture gives the repository a runnable foundation without overengineering the system. It supports controlled experimentation and provides a clear base for future research modules and policy-aware evaluation flows.

