import os

from contentalchemy.images.sync_api.snapper import HTMLSnapper

headless_url = os.environ.get("CA_HEADLESS_URL", "")
default_html_snapper = HTMLSnapper(browser_endpoint=headless_url)

__version__ = "0.1.0"
__all__ = [
    "headless_url",
    "default_html_snapper",
]
