from fastapi import FastAPI
from transaction import router

myapp = FastAPI(title="Finance Tracker API",version='1.0')
myapp.include_router(router)