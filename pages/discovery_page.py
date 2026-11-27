from pages.base_page import BasePage
from pages.service_details_page import ServiceDetailsPage


class DiscoveryPage(BasePage):
    def open_first_service(self):
        cards = self.page.locator('a[href*="/service-details"]')
        cards.first.wait_for(state="visible")
        cards.first.click()
        return ServiceDetailsPage(self.page)
