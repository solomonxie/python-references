# $ uvicorn 11_swagger_ui:app --reload
# $ open http://127.0.0.1:8000/docs      # Swagger UI
# $ open http://127.0.0.1:8000/redoc     # ReDoc
# $ open http://127.0.0.1:8000/openapi.json

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Hello FastAPI",
    description="Playground for the auto-generated Swagger/ReDoc docs.",
    version="1.0.0",
)


class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    price: float = Field(gt=0, examples=[3.5])
    is_offer: Union[bool, None] = None


@app.get(
    "/items/{item_id}",
    tags=["items"],
    summary="Fetch a single item",
    description="Longer explanation shown in the expanded Swagger UI panel.",
    response_description="The requested item",
)
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/", tags=["items"], response_model=Item)
def create_item(item: Item):
    return item


@app.get("/legacy", tags=["items"], deprecated=True)
def legacy_endpoint():
    return {"msg": "still works, but Swagger UI strikes it through"}
