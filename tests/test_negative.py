import re

import pytest
from playwright.sync_api import expect

from data.users import USERS
from config.settings import BASE_URL
from pages.customer_dashboard_page import CustomerDashboardPage
from pages.home_page import HomePage
from pages.stripe_checkout_page import StripeCheckoutPage


@pytest.mark.negative
def test_login_shows_errors_when_fields_empty(page):
    home = HomePage(page)
    home.open_home()
    login = home.click_sign_in()
    login.submit_empty()

    expect(login.email_error()).to_be_visible()
    expect(login.password_error()).to_be_visible()
    expect(page).to_have_url(re.compile(r"/sign-up-login-screen"))


@pytest.mark.negative
def test_login_rejects_wrong_password(page):
    customer = USERS["customer"]

    home = HomePage(page)
    home.open_home()
    login = home.click_sign_in()
    login.login(customer["email"], "definitely-wrong-password")

    expect(login.invalid_credentials_error()).to_be_visible(timeout=15_000)
    expect(page).to_have_url(re.compile(r"/sign-up-login-screen"))


@pytest.mark.negative
def test_customer_cannot_open_admin_dashboard(page):
    customer = USERS["customer"]

    home = HomePage(page)
    home.open_home()
    home.click_sign_in().login(customer["email"], customer["password"])
    expect(page).to_have_url(re.compile(r"/customer-dashboard"), timeout=30_000)

    page.goto(f"{BASE_URL}/admin-dashboard")
    expect(page).to_have_url(re.compile(r"/customer-dashboard"), timeout=15_000)


@pytest.mark.negative
def test_disabled_slot_keeps_book_button_disabled(page):
    customer = USERS["customer"]

    home = HomePage(page)
    home.open_home()
    home.click_sign_in().login(customer["email"], customer["password"])
    expect(page).to_have_url(re.compile(r"/customer-dashboard"), timeout=30_000)

    details = CustomerDashboardPage(page).click_book_another_service().open_first_service()
    details.page.get_by_text("Choose a date", exact=False).first.wait_for(state="visible")
    details.date_buttons().first.click()
    details.wait_for_time_slots()

    disabled = details.first_disabled_time()
    if disabled is None:
        pytest.skip("No disabled slot available to assert against")

    expect(disabled).to_be_disabled()
    expect(details.continue_disabled_button()).to_be_disabled()


@pytest.mark.negative
@pytest.mark.booking
@pytest.mark.stripe_fill
def test_stripe_declined_card_shows_error(page):
    customer = USERS["customer"]

    home = HomePage(page)
    home.open_home()
    home.click_sign_in().login(customer["email"], customer["password"])
    expect(page).to_have_url(re.compile(r"/customer-dashboard"), timeout=30_000)

    details = CustomerDashboardPage(page).click_book_another_service().open_first_service()
    details.book_until_stripe()

    stripe = StripeCheckoutPage(page)
    stripe.wait_until_open()
    stripe.fill_declined_card()
    stripe.click_pay()

    expect(stripe.card_error()).to_be_visible(timeout=30_000)
    expect(page).to_have_url(re.compile(r"checkout\.stripe\.com", re.I))
