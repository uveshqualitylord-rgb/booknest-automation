import re

import pytest
from playwright.sync_api import expect

from data.users import USERS
from pages.booking_detail_page import BookingDetailPage
from pages.customer_dashboard_page import CustomerDashboardPage
from pages.home_page import HomePage
from pages.stripe_checkout_page import StripeCheckoutPage


@pytest.mark.booking
def test_customer_books_and_pays_with_stripe(page):
    customer = USERS["customer"]

    home = HomePage(page)
    home.open_home()
    login = home.click_sign_in()
    login.login(customer["email"], customer["password"])
    expect(page).to_have_url(re.compile("/customer-dashboard"), timeout=30_000)

    dashboard = CustomerDashboardPage(page)
    discovery = dashboard.click_book_another_service()
    expect(page).to_have_url(re.compile("/service-discovery"))

    details = discovery.open_first_service()
    expect(page).to_have_url(re.compile(r"/service-details\?id="))

    details.select_first_open_slot()
    details.click_book()
    details.confirm_pay_and_book()

    stripe = StripeCheckoutPage(page)
    stripe.wait_until_open()
    stripe.fill_test_payment()
    stripe.click_pay()
    stripe.wait_for_booking_page()


    booking = BookingDetailPage(page)
    booking.wait_for_paid()
    expect(booking.paid_badge()).to_be_visible()
