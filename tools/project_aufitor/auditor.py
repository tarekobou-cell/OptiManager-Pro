from pathlib import Path

from scanner import ProjectScanner
from statistics import ProjectStatistics
from report_generator import ReportGenerator


class ProjectAuditor:
    """
    Lance un audit complet du projet.
    """

    def __init__(
        self,
        root: str,
    ) -> None:

        self.root = Path(root)

    def run(
        self,
    ) -> None:

        scanner = ProjectScanner(
            self.root,
        )

        files = scanner.scan()

        statistics = ProjectStatistics(
            files,
        )

        report = ReportGenerator(
            self.root / "PROJECT_AUDIT.md",
        )

        report.generate(
            statistics,
        )

        print(
            "Audit terminé."
        )


if __name__ == "__main__":

    ProjectAuditor(
        ".",
    ).run()