import motor.motor_asyncio
from beanie import Document
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase
from config import MONGO_HOST, MONGO_PORT


DATABASE_URL = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"
client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client["database_name"]

# Create a MongoDB client
# client = AsyncMongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")

# Create a MongoDB asyncclient
# client = AsyncMongoClient()

# get database
# db = client[MONGO_DB]

# # get collection
# col_tasks = db["tasks"]
# col_users = db["users"]


# # @app.on_event("startup")
# async def startup_db_client():
#     app.mongodb_client = AsyncMongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
#     app.database = app.mongodb_client[config["DB_NAME"]]
#     print("Connected to the MongoDB database!")


# # @app.on_event("shutdown")
# async def shutdown_db_client():
#     await client.close()
