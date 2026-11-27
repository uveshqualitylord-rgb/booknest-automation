import re

from pages.base_page import BasePage

TEST_CARD = "4242424242424242"
TEST_EXPIRY = "12/34"
TEST_CVC = "123"


class StripeCheckoutPage(BasePage):
    def wait_until_open(self):
        self.page.wait_for_url(re.compile(r"checkout\.stripe\.com", re.I), timeout=60_000)
        self.page.locator("#payment-numberInput").wait_for(state="visible")
        return self

    def fill_test_payment(self):
        self.page.locator("#payment-numberInput").fill(TEST_CARD)
        self.page.locator("#payment-expiryInput").fill(TEST_EXPIRY)
        self.page.locator("#payment-cvcInput").fill(TEST_CVC)
        self.page.locator("#billingAddress-nameInput").fill("BookNest Test")
        self.page.locator("#billingAddress-addressLine1Input").fill("123 Test Street")
        return self

    def click_pay(self):
        self.page.get_by_test_id("payment-form-submit-button").click()
        return self

    def wait_for_booking_page(self):
        self.page.wait_for_url(re.compile(r"/bookings/"), timeout=90_000)
        return self
