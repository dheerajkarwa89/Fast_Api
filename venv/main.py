from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# sample get endpoint
@app.get('/items/{item_id}')   
async def read_item(item_id: int, q: str= None):
    return {"item_id": item_id, "q": q}

# A model to represent the data structure
class Item(BaseModel):
    name: str
    price: float
    description: str = None
   
# In-memory database (dictionary)
items_db = {
    1: {"name": "Foo", "price": 24.0, "description": "First item"},
    2: {"name": "Bar", "price": 48.0,  "description": "Second item"}
}

# sample put endpoint
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id in items_db:
        items_db[item_id] = item.dict()
        return {"message": "Item updated successfully", "item": items_db[item_id]}
    else:
        return {"message": "Item not found"}