from pages.base_page import BasePage
from pages.discovery_page import DiscoveryPage


class CustomerDashboardPage(BasePage):
    def click_book_another_service(self):
        self.page.get_by_role("link", name="Book another service").click()
        return DiscoveryPage(self.page)
