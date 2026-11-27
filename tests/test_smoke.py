import os

from config.settings import BASE_URL
from pages.home_page import HomePage


def _api(playwright):
    # Opt-in only (e.g. corporate SSL intercept). Leave unset in CI.
    ignore = os.getenv("IGNORE_HTTPS_ERRORS") == "1"
    return playwright.request.new_context(ignore_https_errors=ignore)


def test_home_page_loads(page):
    home = HomePage(page)
    home.open_home()

    assert "BookNest" in home.get_title()
    assert home.brand_link().is_visible()
    assert home.browse_services_cta().is_visible()


def test_home_http_returns_200(playwright):
    api = _api(playwright)
    response = api.get(f"{BASE_URL}/")
    assert response.status == 200
    assert "BookNest" in response.text()
    api.dispose()


def test_service_discovery_http_returns_200(playwright):
    api = _api(playwright)
    response = api.get(f"{BASE_URL}/service-discovery")
    assert response.status == 200
    assert "BookNest" in response.text()
    api.dispose()
