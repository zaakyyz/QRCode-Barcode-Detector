"""QR and barcode detection project package."""

from .authorization import load_authorized_codes
from .scanner import run_realtime_scanner

__all__ = ["load_authorized_codes", "run_realtime_scanner"]
