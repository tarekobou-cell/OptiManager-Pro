from pathlib import Path


class ReportGenerator:
    """
    Génère le rapport Markdown.
    """

    def __init__(
        self,
        output: Path,
    ) -> None:

        self.output = output

    def generate(
        self,
        statistics,
    ) -> None:

        report = f"""# PROJECT AUDIT

## Statistics

Total files : {statistics.total_files()}

Python files : {statistics.python_files()}

Markdown files : {statistics.markdown_files()}
"""

        self.output.write_text(
            report,
            encoding="utf-8",
        )