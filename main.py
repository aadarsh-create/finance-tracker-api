from fastapi import FastAPI

from transaction import transaction_router
from summary import summary_router
from insights import insight_router



myapp = FastAPI(title="Finance Tracker API",version='1.0')

myapp.include_router(transaction_router)
myapp.include_router(summary_router)
myapp.include_router(insight_router)