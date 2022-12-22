# from typing import Union
from models import Persona,persona_Pydantic, personaIn_Pydantic
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel



fake_secret_token = "coneofsilence"

class Status(BaseModel):
    message: str


# db={1: {"id": 1, "name": "prueba", "age": "20"}}

app = FastAPI()


@app.get('/')
async def read_root():
    return {"Hello": "World"}

# @app.get('/todo/{id}')
# async def get_person(id: int):

#     try:
        
#         return db[id]
    
#     except:
        
#         raise HTTPException(status_code=404, detail="Todo Not Found")

# @app.post('/todo/',response_model=persona_Pydantic)
# async def create_person(todo: personaIn_Pydantic):
#     db.append(todo)
#     return todo




@app.get('/items')
async def get_all():
    return await persona_Pydantic.from_queryset(Persona.all())


@app.get("/items/{item_id}", response_model=persona_Pydantic)
async def read_main(item_id: int, x_token: str = Header()) :
    # if x_token != fake_secret_token:
    #     raise HTTPException(status_code=400, detail="Invalid X-Token header")
    # if item_id not in persona_db:
    #     raise HTTPException(status_code=404, detail="Item not found")
    return await persona_Pydantic.from_queryset_single(Persona.get(id=item_id))


@app.post("/items/", response_model=persona_Pydantic)
async def create_item(item: personaIn_Pydantic, x_token: str = Header()):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    obj =   await Persona.create(**item.dict())
    return await obj

@app.put("/items/{item_id}", response_model=persona_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update_job(item_id: int, item: persona_Pydantic, x_token: str = Header()):
    await Persona.filter(id=item_id).update(**item.dict())
    return await personaIn_Pydantic.from_queryset_single(Persona.get(id=item_id))

@app.delete("/items/{item_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_job(item_id: int,  x_token: str = Header()):
    deleted_person = await Persona.filter(id=item_id).delete()
    if not deleted_person:
        raise HTTPException(status_code=404, detail=f"Person {item_id} not found")
    return Status(message=f"Deleted person {item_id}")

register_tortoise(
    app,
    db_url="sqlite://persona.db",
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)