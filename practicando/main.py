# from typing import Union
from models import Persona, persona_Pydantic, personaIn_Pydantic
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from fastapi import FastAPI, Header, HTTPException



fake_secret_token = "coneofsilence"

#  

app = FastAPI()


# @app.post('/todo/',response_model=persona_Pydantic)
# async def create_person(todo: personaIn_Pydantic):
#     db.append(todo)
#     return todo



# @app.get('/todo/{id}')
# async def get_person(id: int):

#     try:
        
#         return db[id]
    
#     except:
        
#         raise HTTPException(status_code=404, detail="Todo Not Found")


@app.get('/')
async def read_root():
    return {"Hello": "World"}

# @app.get('/items')
# async def get_all():
#     return await persona_Pydantic.from_queryset(Persona.all())


# @app.get("/items/{item_id}", response_model=persona_Pydantic)
# async def read_main(item_id: int) :
#     # if x_token != fake_secret_token:
#     #     raise HTTPException(status_code=400, detail="Invalid X-Token header")
#     # if item_id not in persona_db:
#     #     raise HTTPException(status_code=404, detail="Item not found")
#     return await persona_Pydantic.from_queryset_single(Persona.get(id=item_id))


# @app.post("/items/", response_model=persona_Pydantic)
# async def create_item(item: personaIn_Pydantic, x_token: str = Header()):
#     if x_token != fake_secret_token:
#         raise HTTPException(status_code=400, detail="Invalid X-Token header")
#     obj =   await Persona.create(**item.dict())
#     return await obj

register_tortoise(
    app,
    db_url="sqlite://persona.db",
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)