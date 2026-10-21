from __future__ import annotations

import argparse
from src.app import run_experiment


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a recursive prompt research experiment.")
    parser.add_argument("--experiment-name", default="demo-research-run", help="Name of the experiment")
    parser.add_argument("--recursion-depth", type=int, default=3, help="Depth of recursive prompting loop")
    parser.add_argument("--max-turns", type=int, default=4, help="Maximum number of prompt turns")
    parser.add_argument("--safety-mode", default="strict", choices=["strict", "balanced", "permissive"], help="Safety evaluation mode")
    args = parser.parse_args()

    result = run_experiment(
        experiment_name=args.experiment_name,
        recursion_depth=args.recursion_depth,
        max_turns=args.max_turns,
        safety_mode=args.safety_mode,
    )

    print("\n=== Experiment Result ===")
    print(f"Experiment: {result['experiment_name']}")
    print(f"Safety mode: {result['safety_mode']}")
    print(f"Iteration count: {result['iteration_count']}")
    print(f"Risk score: {result['risk_score']}")
    print(f"Status: {result['status']}")
    for idx, turn in enumerate(result["turns"], start=1):
        print(f"\nTurn {idx}: {turn}")


if __name__ == "__main__":
    main()
