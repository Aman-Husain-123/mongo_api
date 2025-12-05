from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient     # Its a async driver 
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
db = client["euron"]
euron_data = db["euron_coll"]

app = FastAPI()

class eurondata(BaseModel):
    name: str
    phone: int
    city: str
    course: str
    
@app.post("/euron/insert")    
async def euron_data_insert_helper(data:eurondata):         # async :- Non blocking function,if this function is trying to execute it wont block other processes 
    result  = await euron_data.insert_one(data.dict())      # await :- Submit the request and leave a path for other so that they didnt get blocked in high traffic API 
    return str(result.inserted_id)


def euron_helper(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc


@app.get("/euron/getdata")
async def get_euron_data():
    iterms = []
    cursor = euron_data.find({})
    async for document in cursor:
        iterms.append(euron_helper(document))
    return iterms
    
    
@app.get("/euron/showdata")
async def show_euron_data():
    iterms = []
    cursor = euron_data.find({})
    async for document in cursor:
        iterms.append(euron_helper(document))
    return iterms
    
