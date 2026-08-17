from pathlib import Path


class ProjectScanner:
    """
    Analyse l'arborescence d'un projet.
    """

    def __init__(
        self,
        root: Path,
    ) -> None:

        self.root = root

    def scan(self):
        """
        Retourne tous les fichiers du projet.
        """

        return [
            path
            for path in self.root.rglob("*")
            if path.is_file()
        ]