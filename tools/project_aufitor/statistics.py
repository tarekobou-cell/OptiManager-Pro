from pathlib import Path


class ProjectStatistics:
    """
    Calcule les statistiques du projet.
    """

    def __init__(
        self,
        files: list[Path],
    ) -> None:

        self.files = files

    def total_files(
        self,
    ) -> int:

        return len(self.files)

    def python_files(
        self,
    ) -> int:

        return len(
            [
                f
                for f in self.files
                if f.suffix == ".py"
            ]
        )

    def markdown_files(
        self,
    ) -> int:

        return len(
            [
                f
                for f in self.files
                if f.suffix == ".md"
            ]
        )