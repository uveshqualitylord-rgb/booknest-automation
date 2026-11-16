import os

import pytest

from config.settings import BASE_URL


@pytest.fixture(scope="session")
def base_url() -> str:
    """Provide BASE_URL to pytest-playwright / pytest-base-url."""
    return BASE_URL


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        # Headless on CI (GitHub sets CI=true); headed locally for debugging.
        "headless": os.getenv("CI") == "true",
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": False,
    }
