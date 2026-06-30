from fastapi import APIRouter
from database import load_db
from models import TrxnType
from datetime import date

summary_router = APIRouter()


@summary_router.get('/summary')
def get_summary():

    transactions = load_db()['transactions']
    type = ['income','expense']

    summary={}

    for tp in type:
        amount = [ trnx['amount'] for trnx in transactions.values() if trnx['type']==tp]
        summary[tp] = sum(amount)
    
    summary['net'] = summary['income'] - summary['expense']
    return summary


@summary_router.get('/summary/monthly')
def get_monthly_summary():

    transactions = load_db()['transactions']
    y,m,d = str(date.today()).split("-")
    current_month = f'{y}-{m}'

    current_transactions = [transaction for transaction in transactions.values() if current_month in transaction['date' ]]

    type = ['income','expense']
    summary={
        'this month':current_month
    }

    for tp in type:
        amount = [ trnx['amount'] for trnx in current_transactions if trnx['type']==tp]
        summary[tp] = sum(amount)

    summary['net'] = summary['income'] - summary['expense']
    return summary



@summary_router.get('/summary/by-category')
def get_summary_by_category(type: TrxnType):

    transactions = load_db()['transactions']
    category =["food","transport","entertainment","health","education","other"]

    summary={}

    for cat in category:
        amount = [ trnx['amount'] for trnx in transactions.values() if trnx['category']==cat and trnx['type']==type]
        summary[cat] = sum(amount)

    return summary