from __future__ import annotations

from src.pipeline import ResearchPipeline


def run_experiment(experiment_name: str, recursion_depth: int, max_turns: int, safety_mode: str) -> dict:
    """Run a minimal experiment pipeline and return a result summary."""
    pipeline = ResearchPipeline(
        experiment_name=experiment_name,
        recursion_depth=recursion_depth,
        max_turns=max_turns,
        safety_mode=safety_mode,
    )
    return pipeline.run()
