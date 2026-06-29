from fastapi import APIRouter
from models import TrxnCreate, TrxnResponse, TrxnUpdate, TrxnCategory, TrxnType
from database import load_db, save_db
from fastapi import HTTPException

transaction_router = APIRouter()


@transaction_router.get('/')
def root():
    return{
        'Project':'Finance Tracker API',
        'Version':'1.0'
    }


@transaction_router.get('/transactions')
def get_all_transactions(limit: int= None, type: TrxnType=None, category: TrxnCategory=None) -> list[ TrxnResponse ]:

    data = load_db()
    transactions = data["transactions"]

    if type:
        transactions = {k: v for k, v in transactions.items() if v["type"] == type}
    if category:
        transactions = {k: v for k, v in transactions.items() if v["category"] == category}
    if limit:
        return list(transactions.values())[:limit]

    return list(transactions.values())


@transaction_router.get('/transactions/{id}')
def get_transaction(id: int) -> TrxnResponse:

    data = load_db()
    transactions = data["transactions"]

    if str(id) not in transactions.keys():
        raise HTTPException(
            status_code=404,
            detail='Transaction not found'
        )

    return transactions[str(id)]


@transaction_router.post('/transactions')
def create_transaction(trxn : TrxnCreate):

    data = load_db()
    transactions = data["transactions"]

    id = max((int(k) for k in transactions.keys()), default=0) + 1
    transactions[ str(id) ] = {
        'uid':id,
        'amount':trxn.amount,
        'type': trxn.type,
        'category': trxn.category,
        'note':trxn.note
    }
    save_db(data)
    return transactions[ str(id) ]


@transaction_router.put('/transactions/{id}')
def update_transaction(id: int, trxn: TrxnUpdate) -> TrxnResponse:

    data = load_db()
    transactions = data['transactions']

    if str(id) not in transactions.keys():
        raise HTTPException(
            status_code=404,
            detail='Transaction not found'
        )

    transaction = transactions[ str(id) ]
    updates = trxn.model_dump(exclude_none=True)
    transaction.update(updates)

    save_db(data)
    return transaction


@transaction_router.delete('/transactions/{id}')
def delete_transaction(id: int) -> TrxnResponse:

    data = load_db()
    transactions = data['transactions']

    if str(id) not in transactions.keys():
        raise HTTPException(
            status_code=404,
            detail='Transaction not found'
        )
    
    deleted_trxn = transactions.pop( str(id) )
    save_db(data)
    return deleted_trxn
