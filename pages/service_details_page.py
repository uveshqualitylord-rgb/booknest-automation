import re

from pages.base_page import BasePage


class ServiceDetailsPage(BasePage):
    def date_buttons(self):
        return self.page.get_by_role("listbox", name="Available dates").get_by_role("option")

    def time_buttons(self):
        return self.page.get_by_role(
            "button",
            name=re.compile(r"^\d{1,2}:\d{2}\s?(AM|PM)$", re.IGNORECASE),
        )

    def book_button(self):
        return self.page.get_by_role("button", name=re.compile(r"^Book\s+"))

    def continue_disabled_button(self):
        return self.page.get_by_role("button", name="Select a time to continue")

    def confirm_popup(self):
        return self.page.get_by_role("dialog")

    def pay_and_book_button(self):
        return self.confirm_popup().get_by_role("button", name=re.compile(r"Pay", re.I))

    def wait_for_time_slots(self):
        self.time_buttons().first.wait_for(state="visible")
        return self

    def has_open_time_on_selected_day(self):
        times = self.time_buttons()
        for i in range(times.count()):
            if times.nth(i).is_enabled():
                return True
        return False

    def first_disabled_time(self):
        times = self.time_buttons()
        for i in range(times.count()):
            time_btn = times.nth(i)
            if not time_btn.is_enabled():
                return time_btn
        return None

    def select_first_open_slot(self):
        self.page.get_by_text("Choose a date", exact=False).first.wait_for(state="visible")

        dates = self.date_buttons()
        total_dates = dates.count()

        for date_index in range(total_dates):
            dates.nth(date_index).click()
            self.wait_for_time_slots()

            if not self.has_open_time_on_selected_day():
                continue

            times = self.time_buttons()
            for time_index in range(times.count()):
                time_btn = times.nth(time_index)
                if time_btn.is_enabled():
                    time_btn.click()
                    return self

        raise RuntimeError("No open time slots found on any date. Add availability in the app first.")

    def click_book(self):
        self.book_button().click()
        self.confirm_popup().wait_for(state="visible")
        return self

    def confirm_pay_and_book(self):
        self.pay_and_book_button().click()
        return self
