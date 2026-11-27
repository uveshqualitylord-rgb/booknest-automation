import os
from pathlib import Path

import pytest

from config.settings import BASE_URL


def pytest_configure():
    Path("reports").mkdir(exist_ok=True)
    Path("test-results").mkdir(exist_ok=True)


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": os.getenv("CI") == "true",
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": False,
    }
