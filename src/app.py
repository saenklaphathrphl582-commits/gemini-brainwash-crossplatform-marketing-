from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List


@dataclass
class Service:
    name: str
    description: str


@dataclass
class AppConfig:
    project_name: str = "Documentation and Policy Repository"
    version: str = "1.0.0"
    root_dir: str = "."
    services: List[Service] = field(default_factory=list)


class App:
    def __init__(self, config: AppConfig | None = None) -> None:
        self.config = config or AppConfig(
            services=[
                Service(
                    name="documentation",
                    description="Stores project documentation, design notes, and governance guidance.",
                ),
                Service(
                    name="automation",
                    description="Contains source logic and scripts for automation or processing tasks.",
                ),
                Service(
                    name="configuration",
                    description="Stores configuration artifacts and operational policy definitions.",
                ),
            ]
        )

    def get_project_root(self) -> Path:
        return Path(self.config.root_dir).resolve()

    def list_services(self) -> List[str]:
        return [service.name for service in self.config.services]

    def render_summary(self) -> str:
        root = self.get_project_root()
        lines = [
            f"Project: {self.config.project_name}",
            f"Version: {self.config.version}",
            f"Root: {root}",
            "",
            "Available services:",
        ]
        for service in self.config.services:
            lines.append(f"- {service.name}: {service.description}")
        return "\n".join(lines)

    def run(self) -> None:
        print(self.render_summary())


def main() -> None:
    app = App()
    app.run()


if __name__ == "__main__":
    main()
