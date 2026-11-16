class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, path: str = "/"):
        from config.settings import BASE_URL

        normalized = path if path.startswith("/") else f"/{path}"
        self.page.goto(f"{BASE_URL}{normalized}")

    def get_title(self) -> str:
        return self.page.title()
