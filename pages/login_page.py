from pages.base_page import BasePage


class LoginPage(BasePage):
    def email_input(self):
        return self.page.locator("#email")

    def password_input(self):
        return self.page.locator("#password")

    def submit_button(self):
        return self.page.get_by_role("button", name="Sign in to BookNest")

    def login(self, email: str, password: str):
        self.email_input().fill(email)
        self.password_input().fill(password)
        self.submit_button().click()
        return self

    def submit_empty(self):
        self.email_input().fill("")
        self.password_input().fill("")
        self.submit_button().click()
        return self

    def email_error(self):
        return self.page.get_by_text("Email is required")

    def password_error(self):
        return self.page.get_by_text("Password is required")

    def invalid_credentials_error(self):
        return self.page.get_by_text(
            "Invalid credentials — check your email and password and try again"
        )
