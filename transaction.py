from fastapi import APIRouter
from models import TrxnCreate, TrxnResponse, TrxnUpdate
from database import load_db, save_db
from fastapi import HTTPException

router = APIRouter()


@router.get('/')
def root():
    return{
        'Project':'Finance Tracker API',
        'Version':'1.0'
    }


@router.get('/transactions')
def get_all_transactions(limit: int= None) -> list[ TrxnResponse ]:

    data = load_db()
    transactions = data["transactions"]
    if limit:
        return list(transactions.values())[:limit]
    return list(transactions.values())


@router.get('/transactions/{id}')
def get_transaction(id: int) -> TrxnResponse:

    data = load_db()
    transactions = data["transactions"]

    if str(id) not in transactions.keys():
        raise HTTPException(
            status_code=404,
            detail='Transaction not found'
        )

    return transactions[str(id)]


@router.post('/transactions')
def create_transaction(trxn : TrxnCreate):

    data = load_db()
    transactions = data["transactions"]

    id = max((int(k) for k in transactions.keys()), default=0) + 1
    transactions[ str(id) ] = {
        'uid':id,
        'amount':trxn.amount,
        'note':trxn.note
    }
    save_db(data)
    return transactions[ str(id) ]


@router.put('/transactions/{id}')
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




@router.delete('/transactions/{id}')
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
