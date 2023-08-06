import os


headless_url = os.environ.get("CA_HEADLESS_URL", "")

__version__ = "0.1.0"
__all__ = [
    "headless_url",
]
