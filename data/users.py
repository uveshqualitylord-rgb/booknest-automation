import os

# Ensures .env is loaded before reading credentials.
from config.settings import BASE_URL  # noqa: F401


def _require(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required env var: {name}")
    return value


USERS = {
    "customer": {
        "email": _require("CUSTOMER_EMAIL"),
        "password": _require("CUSTOMER_PASSWORD"),
        "home": "/customer-dashboard",
    },
    "provider": {
        "email": _require("PROVIDER_EMAIL"),
        "password": _require("PROVIDER_PASSWORD"),
        "home": "/provider-dashboard",
    },
    "admin": {
        "email": _require("ADMIN_EMAIL"),
        "password": _require("ADMIN_PASSWORD"),
        "home": "/admin-dashboard",
    },
}
