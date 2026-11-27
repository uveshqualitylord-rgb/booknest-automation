# BookNest Automation

End-to-end and API checks for [BookNest](https://booknest.niraj.shop) — customer / provider / admin booking flows.

[![E2E](https://github.com/uveshqualitylord-rgb/booknest-automation/actions/workflows/e2e.yml/badge.svg)](https://github.com/uveshqualitylord-rgb/booknest-automation/actions/workflows/e2e.yml)

## Stack

- Python 3.13
- Pytest + Playwright (POM)
- pytest-html reports
- GitHub Actions on every push / PR

## Coverage

| Suite | What it checks |
|--------|----------------|
| Smoke | Home page loads |
| Auth | Customer / provider / admin login → role home |
| Booking | Discover → open slot → Stripe → Paid |
| Negative | Empty login, wrong password, disabled slot, customer blocked from admin, declined card |
| API | Public page status/body, Supabase auth rejection |

## Layout

```text
booknest-automation/
├── pages/
├── tests/
├── data/users.py
├── config/settings.py
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

Fill `.env` with app credentials. Optional for the auth API test: `SUPABASE_URL`, `SUPABASE_ANON_KEY`.

## Run

```bash
pytest -v
pytest -m negative -v
pytest -m api -v
pytest -m booking -v
```

HTML report: `reports/report.html`  
On failure Playwright keeps screenshots and traces under `test-results/`.

## CI

Secrets: `BASE_URL`, role emails/passwords, optional `SUPABASE_URL` / `SUPABASE_ANON_KEY`.

Artifacts: pytest HTML report (always) and failure screenshots/traces.

## Sample report

![pytest-html report](docs/pytest-report.png)
