from pages.base_page import BasePage
from pages.login_page import LoginPage


class HomePage(BasePage):
    def open_home(self):
        self.open("/")
        return self

    def brand_link(self):
        return self.page.get_by_role("link", name="BookNest home")

    def browse_services_cta(self):
        return self.page.get_by_role("link", name="Browse services")

    def sign_in_link(self):
        return self.page.get_by_role("banner").get_by_role("link", name="Sign in")

    def click_sign_in(self) -> LoginPage:
        self.sign_in_link().click()
        return LoginPage(self.page)
