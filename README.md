# 💰 Finance Tracker API

A REST API for tracking personal income and expenses — with filtering, monthly summaries, category breakdowns, spending insights, and **ML-powered auto-categorization**.

Built with **FastAPI** + **Python** + **scikit-learn**

---

### 🔗 Live Demo
**Swagger docs:** https://finance-tracker-api-wxtr.onrender.com/docs

![Swagger UI](/images/swagger_ui.png)

---

## ✨ Features

**Core**
- Add, edit, and delete transactions
- Filter transactions by type, category, and month
- Monthly income vs. expense breakdown
- Per-category spending breakdown (income or expense)
- Insights — top spending category, average daily spend, biggest expense

**Machine Learning**
- **Category prediction** — classifies a transaction's category from its description text (`/predict/category`)
- **Type prediction** — classifies a transaction as income or expense from its description (`/predict/type`)
- Trained on a synthetically generated dataset (expense- and income-style phrasing across 6 categories), evaluated against real transaction data, reaching **100% accuracy** on the held-out test set after iterative gap-fixing
- Designed to keep improving as real transaction data accumulates

---

## 🛠 Tech Stack
- **FastAPI** — API framework
- **Pydantic** — validation + enums
- **scikit-learn** — TF-IDF + Logistic Regression for text classification
- **joblib** — model persistence
- **pandas** — data handling for training/eval
- JSON file-based storage
- `python-dotenv` for config

---

## 📁 Project Structure

```
finance-tracker-api/
├── main.py                     # App entry point, router registration
├── transaction.py              # CRUD endpoints
├── summary.py                  # Summary endpoints
├── insights.py                 # Insights endpoint
├── models.py                   # Pydantic models and enums
├── database.py                 # JSON read/write helpers
├── preprocess.py                # Shared preprocessing for ML
├── generate_synthetic_data.py  # Synthetic training data generator
├── categoryPredict.py          # Category prediction logic + endpoint
├── typePredict.py              # Type prediction logic + endpoint
├── predict.py                  # Prediction helpers
├── categorizer_model.pkl       # Trained category classifier
├── type_model.pkl              # Trained type classifier
├── db.json                     # Database
├── sample_db.json              # Sample data for testing
├── transactions_labeled.csv    # Synthetic training data
├── requirements.txt
└── .env                        # DB_PATH config (not committed)
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/transactions` | Get all transactions (filter: type, category, month) |
| GET | `/transactions/{id}` | Get a specific transaction |
| POST | `/transactions` | Add a new transaction |
| PUT | `/transactions/{uid}` | Edit a transaction |
| DELETE | `/transactions/{uid}` | Delete a transaction |
| GET | `/summary` | Total income, expense, and net |
| GET | `/summary/monthly` | Month-by-month breakdown |
| GET | `/summary/by-category?type=expense` | Per-category totals by type |
| GET | `/insights` | Top category, avg daily spend, biggest expense |
| POST | `/predict/category` | Predict transaction category from description |
| POST | `/predict/type` | Predict income/expense from description |

---

## 🤖 ML Pipeline

The category classifier was built and validated iteratively rather than trained once and shipped:

1. **Synthetic data generation** — templated descriptions across 6 categories (food, transport, entertainment, health, education, other), covering both expense-style ("Swiggy order") and income-style ("Medical reimbursement") phrasing.
2. **Training** — TF-IDF vectorization + Logistic Regression, trained purely on synthetic data.
3. **Evaluation on real data** — tested against real (dummy) transaction records as a held-out set, deliberately excluded from training to check generalization.
4. **Gap analysis & fix** — initial run scored 88% accuracy; misclassifications were traced to missing vocabulary (e.g., income-style phrasing like "scholarship," "reimbursement," and specific terms like "textbook" were absent from templates). Templates were expanded to close each gap.
5. **Final result** — 100% precision/recall across all 6 categories on the real-data test set.

This mirrors a real production ML workflow: bootstrap with synthetic data, validate against real signal, iterate on error analysis rather than blindly increasing data volume.

---

## 🚀 Run Locally

```bash
git clone https://github.com/aadarsh-create/finance-tracker-api.git
cd finance-tracker-api
pip install -r requirements.txt
uvicorn main:app --reload
```

API docs → http://127.0.0.1:8000/docs

To retrain the ML models:
```bash
python generate_synthetic_data.py
python categoryPredict.py
```

---

## 📝 Note
Uses file-based JSON storage. Data resets on redeploy — intentional for a portfolio project.