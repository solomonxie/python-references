# $ uvicorn 12_advanced_swagger:app --reload
# $ open http://127.0.0.1:8000/custom-docs   # our own Swagger UI, not FastAPI's built-in one
# $ curl http://127.0.0.1:8000/openapi.json
# $ curl http://127.0.0.1:8000/items/-1       # see the documented 422 example

from fastapi import FastAPI, status
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

# docs_url/openapi_url=None turns off FastAPI's built-in /docs and /openapi.json —
# useful when docs should live behind auth, or be served from a custom path/style.
app = FastAPI(docs_url=None, openapi_url=None)


class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    price: float = Field(gt=0, examples=[3.5])


class ErrorResponse(BaseModel):
    code: int
    message: str


# Documenting every status code a route can actually return, each with its own
# example, gives Swagger UI a response tab per code instead of one generic 200.
ITEM_RESPONSES = {
    status.HTTP_200_OK: {"model": Item},
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorResponse,
        "content": {"application/json": {"example": {"code": 404, "message": "Item not found"}}},
    },
    status.HTTP_422_UNPROCESSABLE_ENTITY: {
        "model": ErrorResponse,
        "content": {"application/json": {"example": {"code": 422, "message": "item_id must be >= 0"}}},
    },
}


@app.get("/items/{item_id}", responses=ITEM_RESPONSES)
def read_item(item_id: int):
    if item_id < 0:
        return JSONResponse(status_code=422, content={"code": 422, "message": "item_id must be >= 0"})
    return Item(name="Foo", price=3.5)


@app.get("/openapi.json", include_in_schema=False)
def custom_openapi():
    return get_openapi(title="Hello FastAPI (advanced)", version="1.0.0", routes=app.routes)


@app.get("/custom-docs", include_in_schema=False)
def custom_docs():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Hello FastAPI (advanced) — Swagger UI",
        # REF: https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
        swagger_ui_parameters={
            "defaultModelsExpandDepth": -1,  # hide the "Schemas" section
            "tryItOutEnabled": True,  # "Try it out" is on by default
        },
    )
