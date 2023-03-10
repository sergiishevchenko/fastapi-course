from enum import Enum
from fastapi import Body, FastAPI, Query, Path
from pydantic import BaseModel, Field, HttpUrl


app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.post("/")
# async def post():
#     return {"message": "Hello from the post route"}


# @app.put("/")
# async def put():
#     return {"message": "Hello from the put route"}


# @app.get("/users")
# async def list_users():
#     return {"message": "list users route"}


# @app.get("/users/{user_id}")
# async def get_user(user_id: int):
#     return {"user_id": user_id}


# @app.get("/users/me")
# async def get_current_user():
#     return {"message": "this is a current user"}


# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dairy"


# @app.get("/foods/{food_name}")
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {"food_name": food_name, "message": "you are healthy"}

#     if food_name.value == "fruits":
#         return {"food_name": food_name, "message": "you are still healthy, but like sweet thing"}

#     return {"food_name": food_name, "message": "I like chocolate milk"}


# fake_item_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items")
# async def list_items(skip: int = 0, limit: int = 10):
#     return fake_item_db[skip: skip + limit]


# @app.get("/items/{item_id}")
# async def list_items(item_id: str, sample_query_param: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "sample_query_param": sample_query_param}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec."}
#         )
#     return item


# @app.get("/users/{user_id}/items/{item_id}")
# async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec."}
#         )
#     return item


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# @app.post("/items")
# async def create_item(item: Item) -> Item:
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict


# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         item.update({"q": q})
#     return result


# @app.get("/items")
# async def read_items(
#     q: str
#     | None = Query(
#         None,
#         min_length=3,
#         max_length=10,
#         title="Sample query string",
#         description="This is a sample query string",
#         deprecated=True,
#         alias="item-query")
# ):
#     results = {"items": [{"item_name": "Foo"}, {"item_name": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# @app.get("/items_hidden")
# async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     return {"hidden_query": "Not found"}


# @app.put("/items_validation/{item_id}")
# async def read_items_validation(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", ge=10, le=100),
#     q: str = "Hello",
#     size: float = Query(..., gt=0, lt=7.75)
# ):
#     results = {"item_id": item_id, "size": size}
#     if q:
#         results.update({"q": q})
#     return results


# Part 7 - Body - Multiple Parameters
# class Item(BaseModel):
#     username: str
#     full_name: str | None = None


# class User(BaseModel):
#     name: str
#     description: str | None = None


# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", ge=10, le=100),
#     q: str | None = None,
#     item: Item = Body(..., embed=True)
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results

## Part 8 - Body - Fields
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(None, title="The description of the item", max_length=300)
#     price: float = Field(..., gt=0, description="The price must be greater than zero")
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results


# Part 9 - Body - Nested Models
class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    image: Image | None = None
    tags: list = []


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/offers")
async def create_offer(offer: Offer = Body(..., embed=True)):
    return offer


@app.post("/images/multiple")
async def create_multiple_images(images: list[Image]):
    return images


@app.post("/blah")
async def create_some_blah(blahs: dict[int, float]):
    return blahs