import os

import pytest

from config.settings import BASE_URL


@pytest.mark.api
def test_home_page_returns_200(playwright):
    api = playwright.request.new_context(ignore_https_errors=True)
    response = api.get(f"{BASE_URL}/")
    assert response.status == 200
    body = response.text()
    assert "BookNest" in body
    api.dispose()


@pytest.mark.api
def test_service_discovery_returns_200(playwright):
    api = playwright.request.new_context(ignore_https_errors=True)
    response = api.get(f"{BASE_URL}/service-discovery")
    assert response.status == 200
    body = response.text()
    assert "BookNest" in body
    api.dispose()


@pytest.mark.api
def test_supabase_auth_rejects_bad_password(playwright):
    supabase_url = os.getenv("SUPABASE_URL", "").rstrip("/")
    anon_key = os.getenv("SUPABASE_ANON_KEY", "")
    if not supabase_url or not anon_key:
        pytest.skip("Set SUPABASE_URL and SUPABASE_ANON_KEY for this API test")

    api = playwright.request.new_context(
        ignore_https_errors=True,
        extra_http_headers={
            "apikey": anon_key,
            "Content-Type": "application/json",
        },
    )
    response = api.post(
        f"{supabase_url}/auth/v1/token?grant_type=password",
        data={
            "email": "nobody@example.com",
            "password": "wrong-password",
        },
    )
    assert response.status in (400, 401)
    body = response.json()
    assert "error" in body or "msg" in body or "error_description" in body
    api.dispose()
