# BookNest Automation

End-to-end UI tests for [BookNest](https://booknest.niraj.shop) — a local-services booking app (customer / provider / admin).

[![E2E](https://github.com/uveshqualitylord-rgb/booknest-automation/actions/workflows/e2e.yml/badge.svg)](https://github.com/uveshqualitylord-rgb/booknest-automation/actions/workflows/e2e.yml)

## Stack

- Python 3.13
- Pytest + Playwright
- Page Object Model (POM)
- GitHub Actions CI on every push / PR

## What is covered

| Suite | Flow |
|--------|------|
| Smoke | Home page loads |
| Auth | Customer, provider, and admin login → role dashboard |
| Booking | Discover → pick open slot → confirm → Stripe Checkout → Paid |

## Layout

```text
booknest-automation/
├── pages/                 # Page objects
├── tests/                 # Pytest specs
├── data/users.py          # Role credentials from env
├── config/settings.py     # BASE_URL
├── conftest.py
└── .github/workflows/e2e.yml
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env
```

Fill `.env` with `BASE_URL` and customer / provider / admin credentials.

## Run locally

```bash
pytest -v
pytest tests/test_booking.py -v
pytest -m booking -v
```

## CI

GitHub Actions runs Chromium E2E on `main` and pull requests. Required repository secrets:

`BASE_URL`, `CUSTOMER_EMAIL`, `CUSTOMER_PASSWORD`, `PROVIDER_EMAIL`, `PROVIDER_PASSWORD`, `ADMIN_EMAIL`, `ADMIN_PASSWORD`
