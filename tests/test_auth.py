import re

import pytest
from playwright.sync_api import expect

from data.users import USERS
from pages.home_page import HomePage

#runs full auth flow
@pytest.mark.parametrize("role", ["customer", "provider", "admin"])
def test_login_from_home_redirects_to_role_home(page, role):
    user = USERS[role]

    home = HomePage(page)
    home.open_home()
    login = home.click_sign_in()
    login.login(user["email"], user["password"])

    expect(page).to_have_url(re.compile(re.escape(user["home"])))
