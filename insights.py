from fastapi import APIRouter
from database import load_db
from summary import get_summary_by_category,get_summary,get_monthly_summary
from datetime import date

insight_router = APIRouter()

@insight_router.get('/insights')
def get_insights():
    transactions = load_db()['transactions'].values()

    data = get_summary_by_category(type='expense')
    top_category = [ key for key in data.keys() if data[key] == max(data.values()) ][0]

    amount = get_summary()['expense']
    dates = len(list(set( [t['date'] for t in transactions if t['type']=='expense'] )))
    average_spent_daily = amount/dates

    max_amount = max([t['amount'] for t in transactions if t['type'] == 'expense' ])
    biggest_expense = [t for t in transactions if t['amount'] == max_amount][0]

    insights={
        'top_category':top_category,
        'average_expense_daily':average_spent_daily,
        'biggest_expense':biggest_expense
        }

    return insights