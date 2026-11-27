from pages.base_page import BasePage


class BookingDetailPage(BasePage):
    def wait_for_paid(self):
        self.page.get_by_text("Paid", exact=True).wait_for(state="visible", timeout=60_000)
        return self

    def paid_badge(self):
        return self.page.get_by_text("Paid", exact=True)
