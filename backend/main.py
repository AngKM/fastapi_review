from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
app = FastAPI()

fake_item_db = [{"item_name": "Buger", "price": 10.99}, {"item_name": "Pizza", "price": 15.99}, {"item_name": "Ice Cream", "price": 5.99}, {"item_name": "Cake", "price": 20.99}, {"item_name": "Pasta", "price": 12.99}]

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/")
async def root():
    return({"message":"Hello World"})

@app.get("/items")
async def read_items(skip:int = 0, limit:int =3):
    return {"items": fake_item_db[skip: skip+limit]}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q:str|None = None, short:bool|None = None):
    item={"item_id": item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description": "This is an amazing long description"})
    return item



@app.get("/me")
async def read_me():
    return{"user_id": "001", "username":"AngKM", "email":"angang.km@gmail.com"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return{"user_id": user_id}

@app.get("/users/{user_id}/posts/{post_id}")
async def read_user_post(user_id: str, post_id: str, q:str|None = None, short:bool|None = None):
    user_post={"user_id": user_id, "post_id": post_id}
    if q:
        user_post.update({"q":q})
    if not short:
        user_post.update({"description": "This is an amazing long description"})
    return user_post


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return{'file_path': file_path}

class Item(BaseModel):
    item_name: str
    price: float
    tax: float|None = None
    description: str|None = None

@app.post("/items/")
async def create_item(item: Item):
    return item
