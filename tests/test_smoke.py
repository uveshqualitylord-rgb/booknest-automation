from pages.home_page import HomePage


def test_home_page_loads(page):
    home = HomePage(page)
    home.open_home()

    assert "BookNest" in home.get_title()
    assert home.brand_link().is_visible()
    assert home.browse_services_cta().is_visible()
