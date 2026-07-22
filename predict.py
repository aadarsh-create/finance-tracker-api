from fastapi import APIRouter
from models import Description,returnCategory,returnType
from categoryPredict import category_predict
from typePredict import type_predict

predict_router = APIRouter()

@predict_router.post("/predict/category")
def predict_category(desc : Description) -> returnCategory:
    return category_predict(desc.description)

@predict_router.post("/predict/type")
def predict_type(desc : Description) ->returnType :
    return type_predict(desc.description)

# print(type_predict("school fee"))
# print(category_predict("school fee"))