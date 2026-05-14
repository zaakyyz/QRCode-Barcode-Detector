from pathlib import Path


def load_authorized_codes(file_path: Path) -> set[str]:
    """Load authorized code values from text file (one code per line)."""
    if not file_path.exists():
        raise FileNotFoundError(
            f"Authorized codes file was not found: {file_path.resolve()}"
        )

    with file_path.open("r", encoding="utf-8") as file:
        return {line.strip() for line in file if line.strip()}
