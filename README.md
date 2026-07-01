# 💰 Finance Tracker API

A REST API to track personal income and expenses — with filtering, monthly summaries, category breakdowns, and spending insights.

Built with **FastAPI** + **Python**

---

### Live Demo- https://finance-tracker-api-wxtr.onrender.com/docs


![Swagger UI](/images/swagger_ui.png)

---

## Features
- Add, edit, and delete transactions
- Filter transactions by type, category, and month
- Monthly income vs expense breakdown (all months)
- Per-category spending breakdown (income or expense)
- Insights — top spending category, average daily spend, biggest expense

## Tech Stack
- FastAPI
- Pydantic (validation + enums)
- Python `datetime`, `uuid`
- JSON file-based storage
- `python-dotenv` for config

---

## Project Structure

```
finance-tracker-api/
├── main.py           # App entry point, router registration
├── transaction.py    # CRUD endpoints
├── summary.py        # Summary endpoints
├── insights.py       # Insights endpoint
├── models.py         # Pydantic models and enums
├── database.py       # JSON read/write helpers
├── db.json           # Database
├── sample_db.json    # Sample data for testing
├── requirements.txt
└── .env              # DB_PATH config (not committed)
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/transactions` | Get all transactions (filter: type, category, month) |
| GET | `/transactions/{id}` | Get a specefic transaction |
| POST | `/transactions` | Add a new transaction |
| PUT | `/transactions/{uid}` | Edit a transaction |
| DELETE | `/transactions/{uid}` | Delete a transaction |
| GET | `/summary` | Total income, expense, and net |
| GET | `/summary/monthly` | Month-by-month breakdown |
| GET | `/summary/by-category?type=expense` | Per-category totals by type |
| GET | `/insights` | Top category, avg daily spend, biggest expense |

---

## Run Locally

```bash
git clone https://github.com/aadarsh-create/finance-tracker-api.git
cd finance-tracker-api
pip install -r requirements.txt
uvicorn main:app --reload
```

API docs → http://127.0.0.1:8000/docs

---

## Note
Uses file-based JSON storage. Data resets on redeploy — intentional for a portfolio project.
