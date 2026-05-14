"""Compatibility script for basic mode."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from qr_barcode_detector.scanner import run_realtime_scanner


if __name__ == "__main__":
    run_realtime_scanner()
