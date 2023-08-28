from datetime import date
from fastapi import APIRouter
from database.database import db
from models.data import DataModel

router = APIRouter()


@router.get("/")
async def fetchData():
    collection = db.db["records"]

    data = list(collection.find())

    for document in data:
        document["_id"] = str(document["_id"])

    return data


@router.post(path="/")
async def addData(body: DataModel) -> dict[str, str]:
    body.date_created = date.today().strftime("%d-%b-%y")

    chart_type_str = body.chart_type.value

    data_dict = body.dict()
    data_dict["chart_type"] = chart_type_str

    collection = db.db["records"]
    result = collection.insert_one(data_dict)

    return {"message": "Data added", "id": str(result.inserted_id)}
